import unittest
import os
import json
import yaml
import xml.etree.ElementTree as ET
from configuration_errors import *
from configuration_manager import ConfigurationManager
from RobotBase import Battery, Motor, Sensor, RobotBase

class TestConfigurationManagerLoad(unittest.TestCase):

    def setUp(self):
        """Create a minimal valid config file for use in tests."""
        self.valid_file = 'test_valid_config.json'
        self.test_data = {'robot_id': 'test_robot', 'battery_level': 100}
        with open(self.valid_file, 'w') as f:
            json.dump(self.test_data, f)

        self.corrupt_file = "test_corrupt_config.json"
        self.invalid_data = ['robot_id', 'test_robot', 'battery_level', 100]

        with open(self.corrupt_file, "w") as cf:
            cf.write(f"{self.invalid_data}")

        self.config_test = ConfigurationManager(self.valid_file)

    def tearDown(self):
        """Remove test files created during tests."""
        if os.path.exists(self.valid_file):
            os.remove(self.valid_file)
        if os.path.exists(self.corrupt_file):
             os.remove(self.corrupt_file)

    def test_load_valid_json(self):
        """ConfigurationManager loads a valid JSON file without error."""

        self.assertEqual(self.config_test.config, self.test_data)

    def test_load_missing_file_raises_error(self):
        """ConfigFileNotFoundError raised when file does not exist."""

        with self.assertRaises(ConfigFileNotFoundError):
            ConfigurationManager("invalid_file.json")

    def test_load_corrupted_file_raises_error(self):
        """ConfigParseError raised when file contains invalid JSON/XML/YAML."""

        with self.assertRaises(ConfigParseError):
            self.config_test = ConfigurationManager(self.corrupt_file)


class TestConfigurationManagerGet(unittest.TestCase):

    def setUp(self):
        self.valid_file = 'test_get_config.json'
        with open(self.valid_file, 'w') as f:
            json.dump({
                'robot_id': 'test_robot',
                'sensors': {'ir_count': 4, 'threshold': 0.5}
            }, f)
        self.config_file = ConfigurationManager(self.valid_file)

    def tearDown(self):
        if os.path.exists(self.valid_file):
            os.remove(self.valid_file)

    def test_get_simple_key(self):
        """get() returns correct value for a top-level key."""
        
        self.assertEqual(self.config_file.get("robot_id"), "test_robot")

    def test_get_nested_key_dot_notation(self):
        """get() returns correct value for a nested key using dot notation."""
        self.assertEqual(self.config_file.get('sensors.ir_count'), 4)

    def test_get_missing_key_returns_default(self):
        """get() returns the provided default when key does not exist."""
        self.assertEqual(self.config_file.get("default_test"), None)


class TestConfigurationManagerValidate(unittest.TestCase):

    def setUp(self):
        self.valid_file = 'test_valid_config.json'
        self.test_data = {'robot_name': 'test_robot', 
                          'battery': Battery(100,100), 
                          'motor':Motor(0), 
                          'sensor':Sensor('ir sensor')}
        with open(self.valid_file, 'w') as f:
            json.dump(self.test_data, f)

        self.config_file = ConfigurationManager(self.valid_file)

    def tearDown(self):
        if os.path.exists(self.valid_file):
            os.remove(self.valid_file)

    def test_valid_config_passes_validation(self):
        """validate() does not raise when config data is valid."""

        self.config_file.validate()

    def test_missing_required_field_raises_validation_error(self):
        """ConfigValidationError raised when a required field is absent."""
        # YOUR CODE HERE — create a config missing a required field
        pass

    def test_invalid_field_type_raises_validation_error(self):
        """ConfigValidationError raised when a field has the wrong type."""
        # YOUR CODE HERE
        pass


if __name__ == '__main__':
    unittest.main()