class Battery:
    """A battery component
    
    Args:
        level: current battery level (int)
        capacity: maximum charge (int)"""
    
    def __init__(self, level: float, capacity: float):
        self.capacity = capacity
        self.level = level

    def drain(self, amount: float):
        """Drain battery level by amount"""
        self.level = max(0, self.level - amount)
        if self.level == 0:
            print("Battery is depleted")
 
    def charge(self, amount: float):
        """Charge battery by amount"""
        self.level = min(self.capacity, self.level + amount)
        if self.level == self.capacity:
            print("Battery fully charged")

    def charge_percentage(self):
        """Returns battery level as percentage"""
        return (self.level/self.capacity) * 100

    def __str__(self):
        return (f"Battery charge at {self.charge_percentage():.2f}%")

class Motor:
    """A motor component

    Args:
        speed: motor's current speed (int)
        is_running: is the motor running (bool)"""
    
    def __init__(self, speed: float):
        self.set_speed(speed)
        if (speed != 0):
            self.is_running = True
        else:
            self.is_running = False

    def move_forward(self, distance:float):
        """Moves the robot forward a set distance"""
        self.distance = distance
        self.is_running = True

    def move_backward(self, distance:float):
        """Moves backward a set distance"""
        self.distance = 0 - distance
        self.is_running = True

    def stop(self):
        """Stops movement"""
        self.set_speed(0)
        self.is_running = False

    def set_speed(self, speed:float):
        """Set specific robot speed"""
        self.speed = speed
        if (speed == 0):
            self.is_running = False

    def __str__(self):
        """Prints user friendly string"""
        return (f"Motor speed: {self.speed} m/s")

class Sensor:
    """Sensor component
    
    Args:
        sensor_type: Name of the sensor (str)"""
    def __init__(self, sensor_type: str):
        self.type = sensor_type
        self.reading = self.read_data()

    def read_data(self):
        """Read sensor input"""
        return f"{self.type} reading"

    def get_reading(self):
        """Return sensor readings"""
        return f"Sensor reading: {self.reading}"

    def __str__(self):
        return (f"Sensor: {self.type}, {self.get_reading()}")

class RobotBase:
    """A class of robot controls."""

    def __init__(self, name: str, battery: Battery, motor: Motor, sensor: Sensor):
        """Initialise a robot base
        
        Args:
            _name: Robot name (str)
            _battery: (level: int, capacity: int)
            _motor: (speed: int, is_running: bool)
            _sensor: (sensor_type: str)
        """
        self._name = name
        self._battery = battery
        self._motor = motor
        self._sensor = sensor

    @property
    def name(self):
        """Get robot name"""        
        return self._name
    
    def move(self, distance):
        if self._motor.speed > 0:
            self._sensor.read_data()
            self._motor.move_forward(distance)
            self._battery.drain(2 * distance)
        elif self._motor.speed < 0:
            self._motor.move_backward(distance)
            self._battery.drain(2 * distance)
        else:
            self._motor.is_running = True
            self._motor.set_speed(1)
            self.move(distance)

    def __str__(self):
        """User-friendly report of the robot's status"""
        return(f"Robot Name: {self.name}, " +
              f"{self._battery}, " +
              f"{self._motor}, "
              f"{self._sensor}")
    def __repr__(self):
        """Dev-friendly report of all variables"""
        pass

# Tests RobotBase class if this is the main file
if __name__ == "__main__":
    robot = RobotBase("Bingus", Battery(24,50), Motor(10, True), Sensor("LIDAR"))
    print(robot)

    robot._motor.set_speed(34)
    robot.move(5)
    robot._sensor.sensor_type = "Camera"
    print(robot)