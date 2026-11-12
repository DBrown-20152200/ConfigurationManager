class ConfigurationError(Exception):
    """Base exception for all configuration errors
    
    All ConfigurationManager exceptions inherit from this,
    allowing for catching broad errors or specialising into specific errors.
    """
    pass