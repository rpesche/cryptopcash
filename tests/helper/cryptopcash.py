import pytest

from cryptopcash.cryptopcash import CryptopCash


@pytest.fixture(autouse=True)
def cleared_instance():
    CryptopCash.instance = None
