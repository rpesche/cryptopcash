from pathlib import Path


def get_package_path():
    import cryptopcash
    cryptopcash_path = Path(cryptopcash.__file__)
    return cryptopcash_path.parents[1]


def get_resource_path():
    return get_package_path() / 'resources'
