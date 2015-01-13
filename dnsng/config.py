"Read configuration information from config file"

import platform

if platform.python_version() < '3':
    from ConfigParser import SafeConfigParser
else:
    from configparser import SafeConfigParser


def read_config(config_filename='/etc/dnsng/dnsng.ini'):
    """
    Read configuration from given config filename and return config parser
    
    :param config_filename: Name of the configuration file
    :returns: The config parser object with configuration from the file loaded
    """
    
    config = SafeConfigParser()
    config.read(config_filename)

    return config
