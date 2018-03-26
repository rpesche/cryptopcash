import os
import shutil
import xdg
import pytest
import tempfile
import json
from configparser import ConfigParser

from cryptopcash.storage import LocalStorage


@pytest.fixture(autouse=True)
def locale_storage(monkeypatch):
    config_dir = tempfile.mkdtemp()
    cryptopcash_config = os.path.join(config_dir,
                                      LocalStorage.PREFIX_DIRECTORY_NAME)
    os.mkdir(cryptopcash_config)

    data_dir = tempfile.mkdtemp()
    cryptopcash_data = os.path.join(data_dir,
                                    LocalStorage.PREFIX_DIRECTORY_NAME)
    os.mkdir(cryptopcash_data)

    monkeypatch.setattr(xdg, "XDG_CONFIG_HOME", config_dir)
    monkeypatch.setattr(xdg, "XDG_DATA_HOME", data_dir)

    os.mknod(os.path.join(cryptopcash_data, LocalStorage.WALLET_FILENAME))
    os.mknod(os.path.join(cryptopcash_config, LocalStorage.CONFIG_FILENAME))

    yield LocalStorage.LocalStorage()

    shutil.rmtree(config_dir)
    shutil.rmtree(data_dir)


@pytest.fixture()
def data_file(locale_storage, request):
    content = request.param
    data_filename = locale_storage.get_locale_data_filename()
    with open(data_filename, 'w') as fd:
        json.dump(content, fd)


@pytest.fixture()
def config_file_sample(locale_storage):

    config = ConfigParser()

    config['theme'] = {'text': 'black'}

    config['api'] = {'currency': 'YEN'}

    config_filename = locale_storage.get_locale_config_filename()
    with open(config_filename, 'w') as fd:
        config.write(fd)
