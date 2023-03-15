# For use with Python3
import math

# Input
waistMeasurement = 34.0 # inches
desiredCircle = 220.0  # degrees of circle desired
seamAllowance = 3.0/8 # inches
fabricWidth = 56 # inches
desiredLength = 23 # inches

print(f'seamAllowance = {seamAllowance}')

# Constants
fullCircle = 360 # degrees

# Maths (See By Hand London, Circle Maths Explained!)
circumference = (fullCircle/desiredCircle) * waistMeasurement
radius = ((circumference + (4 * seamAllowance))/(2 * math.pi)) - seamAllowance

print(f'radius = {radius:.2f}')
