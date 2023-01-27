import math

class RecVec:
    """Creates a class for making rectangle vectors"""
    def __init__(self,x = 2,y = 2):
        """Initializes our object with x and y coordinates."""
        self.x = x
        self.y = y

    def __add__(self, other):
        return (self.x + other.x, self.y + other.y)

    def __sub__(self,other):
        return(self.x - other.x, self.y - other.y)

    def __str__(self):
        """Converts the default string behavior into a readable output with the proper formatting"""
        return f"RecVec(x = {self.x} y = {self.y})"

    def pol(self):
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
        return int(math.degrees(math.atan(self.y/self.x)))

class PolVec:
    """Creates a class for making polar vectors"""
    def __init__(self,mag=1, ang=50):
         self.mag = mag
         self.ang = ang