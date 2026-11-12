import json
import yaml
import xml.etree.ElementTree as ET
import os
from configuration_errors import *

class ConfigurationManager:
    """Manages robot configurations from files."""

    def __init__(self, config_file: str):
        """Initialize with configuration file path."""
        self.config_file = config_file
        self.config = {}
        self.load()

    def verify_file(self):
        """Check if file exists."""

        try:
            open(self.config_file, "r")
        except:
            raise ConfigFileNotFoundError

    def parse_json(self):
        """Parse JSON formatted files."""

        with open(self.config_file, "r") as file:
            self.config = json.load(file)
            file.close()

    def parse_yaml(self):
        """Parse YAML formatted files."""
        pass

    def parse_xml(self):
        """Parse XML formatted files."""
        pass

    def load(self):
        """Load configuration from file (auto-detect format)."""

        # Check if file exists
        self.verify_file()

        # Determine format from file extension
        extension = self.config_file.split(".")[1]

        # Parse appropriate format and save in config
        try:
            if extension == "json":
                self.parse_json()
            elif extension == "yaml":
                self.parse_yaml()
            elif extension == "xml":
                self.parse_xml()
            else:
                raise ConfigurationError
        except:
            raise ConfigParseError

    def get(self, key, default=None):
        """Safely retrieve configuration value.

        Supports dot notation: get('sensors.ir_count')
        Returns default if key not found.
        """

        if "." in key:
            primary_key = key.split(".")[0]
            secondary_key = key.split(".")[1]

            if primary_key in self.config:
                return self.config[primary_key][secondary_key]

        if key in self.config:            
            return self.config[key]
        else:
            return default

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