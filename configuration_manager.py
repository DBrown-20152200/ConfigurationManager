class ConfigurationManager:
    """Manages robot configurations from files."""

    def __init__(self, config_file):
        """Initialize with configuration file path."""
        self.config_file = config_file
        self.config = {}
        self.load()

    def load(self):
        """Load configuration from file (auto-detect format)."""
        # Determine format from file extension
        # Parse appropriate format
        # Store in self.config

    def get(self, key, default=None):
        """Safely retrieve configuration value.

        Supports dot notation: get('sensors.ir_count')
        Returns default if key not found.
        """

    def save(self, output_file=None):
        """Save current configuration to file."""
        # Save to file (auto-detect format from extension)

    def validate(self) -> None:
        """Validate configuration data.

        Raises:
            ConfigValidationError: If any validation checks fail.
        """
        # Check required fields exist
        # Check data types are correct
        # Check values are in valid ranges
        # Raise ConfigValidationError with all errors if any fail