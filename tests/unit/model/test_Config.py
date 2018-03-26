from cryptopcash.model.Config import Config


def test_config(config_file_sample):
    config = Config()
    config.load()

    assert config.currency == 'YEN'
    assert config.text == 'black'

    assert config.banner == 'yellow'
    assert config.banner_text == 'black'

    assert not config.monetary
