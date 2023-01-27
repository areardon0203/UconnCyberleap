import math

class RecVec:
    """Creates a class for making rectangle vectors"""
    def __init__(self,x = 2,y = 2):
        """Initializes our object with x and y coordinates."""
        self.x = x
        self.y = y

    def __add__(self,v1,v2):
        return (v1[0] + v2[0], v1[1] + v2[1])

    def __sub__(self,v1,v2):
        return(v1[0] - v2[0], v1[1] - v2[1])

    def __str__(self):
        """Converts the default string behavior into a readable output with the proper formatting"""
        return f"RecVec(x = {self.x} y = {self.y})"
        
    def mag(self):
        """Returns the magnitude based off of the x and y coordinates created in the initialization phase."""
        # return  (self.x**2 + self.y**2)*(0.5**2)
        return math.sqrt(self.x**2 + self.y**2)

class PolVec:

    def __init__(self,mag=1, angle=2):
        self.mag = mag
        self.angle = angle