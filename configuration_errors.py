class ConfigurationError(Exception):
    """Base exception for all configuration errors
    
    All ConfigurationManager exceptions inherit from this,
    allowing for catching broad errors or specialising into specific errors.
    """
    def __init__(self):
        super().__init__()

class ConfigFileNotFoundError(ConfigurationError):
    """Exception for when file does not exist."""

    def __init__(self):
        super().__init__()

class ConfigParseError(ConfigurationError):
    """Exception for reading invalid data."""

    def __init__(self):
        super().__init__()

class ConfigValidationError(ConfigurationError):
    """Exception for failed validation checks."""