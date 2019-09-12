from pkg_resources import get_distribution, DistributionNotFound


try:
    __version__ = get_distribution("cryptopcash").version
except DistributionNotFound:
    __version__ = "Unknown version"
