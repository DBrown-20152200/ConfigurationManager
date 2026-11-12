import json
import yaml
import xml.etree.ElementTree as ET
import os
from configuration_errors import *
from RobotBase import Battery, Motor, Sensor, RobotBase

class ConfigurationManager:
    """Manages robot configurations from files."""

    def __init__(self, config_file: str):
        """Initialize with configuration file path."""
        self.config_file = config_file
        self.config = {}
        self.extension = str
        self.load()

    def verify_file(self, file):
        """Check if file exists."""

        try:
            open(file, "r")
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
        self.verify_file(self.config_file)

        # Determine format from file extension
        self.extension = self.config_file.split(".")[1]

        # Parse appropriate format and save in config
        try:
            if self.extension == "json":
                self.parse_json()
            elif self.extension == "yaml":
                self.parse_yaml()
            elif self.extension == "xml":
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

        self.verify_file(output_file)

        if self.extension == "json":
            with open(output_file, "w") as f:
                json.dump(self.config, f)

    def validate(self) -> None:
        """Validate configuration data.

        Raises:
            ConfigValidationError: If any validation checks fail.
        """
        required_fields = {"robot_name":str, "battery":Battery, "motor":Motor, "sensor":Sensor}

        # Check required fields exist
        for key in self.config.keys():
            if key not in required_fields:
                raise ConfigValidationError

        # Check data types are correct'
        for key in self.config.keys():
            if type(self.config[key]) != type(required_fields):
                raise ConfigValidationError
            
        # Check values are in valid ranges
        for item in required_fields:
            pass