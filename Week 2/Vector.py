import math

class Vector:
    def __init__(self, *args):
        raise NotImplementedError

    def __add__(self, other):
        """Adds together two different rectangular vector coordinates."""
        return (self.x + other.x, self.y + other.y)

    def __sub__(self,other):
        """Adds together two different rectangular vector coordinates."""
        return(self.x - other.x, self.y - other.y)

    def __eq__(self, other):
        """Checks to make sure two coordinate systems are identical"""
        return(self.x == other.x, self.y == other.y)

    def pol(self):
        """Returns a polar vector from rectangular coordinates"""
        if RecVec:
            mag = int(math.sqrt(self.x**2 + self.y **2))
            ang = int(math.degrees(math.atan(self.y/self.x)))
            return (mag, ang)
        elif PolVec:
            return (mag, ang)
 

class RecVec(Vector):
    """Creates a class for making rectangle vectors"""
    def __init__(self,x = 2,y = 2):
        """Initializes our object with x and y coordinates."""
        self.x = x
        self.y = y

    def __str__(self):
        """Converts the default string behavior into a readable output with the proper formatting"""
        return f"RecVec(x = {self.x} y = {self.y})"

    def pol(self):
        """Returns a polar vector from rectangular coordinates"""
        mag = int(math.sqrt(self.x**2 + self.y **2))
        ang = int(math.degrees(math.atan(self.y/self.x)))
        return (mag, ang)

    def rectangular(self):
        """Returns the rectangular coordinates in a tuple"""
        return (self.x, self.y)

    def get_x(self):
        """Gets the x value from the initialized object"""
        return self.x

    def get_y(self):
        """Gets the y value from the initialized object"""
        return self.y

    def mag(self):
        """Returns the magnitude based off of the x and y coordinates created in the initialization phase."""
        return math.sqrt(self.x**2 + self.y**2)

    def ang(self):
        """Returns the angle from a rectangular vector"""
        return int(math.degrees(math.atan(self.y/self.x)))

class PolVec(Vector):
    """Creates a class for making polar vectors"""
    def __init__(self,mag=1, ang=50):
        self.x = mag
        self.y = ang

    def __str__(self):
        """Converts the default string behavior into a readable output with the proper formatting"""
        return f"PolVec(x = {self.x} y = {self.y})"

    def rectangular(self):
        """First converts y coordinate from degrees to radians and the converts to rectangular coordinates."""
        dToR = math.radians(self.y)
        x = round(self.x * math.cos(dToR))
        y = round(self.x * math.sin(dToR))
        return (x,y)

    def get_x(self):
        """Gets the x value from the initialized object"""
        return self.x

    def get_y(self):
        """Gets the y value from the initialized object"""
        return self.y

    def mag(self):
        """Returns the magnitude based off of the x and y coordinates created in the initialization phase."""
        return (self.x)

    def ang(self):
        """Returns the angle from a rectangular vector"""
        return (self.y)
