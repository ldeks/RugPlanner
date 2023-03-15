# For use with Python3
import math

# Input
waistMeasurement = 34.0 # inches
desiredCircle = 180.0  # degrees of circle desired
seamAllowance = 3.0/8 # inches
fabricWidth = 56 # inches
desiredLength = 23 # inches

print(f'seam allowance = {seamAllowance} inches')

# Constants
fullCircle = 360 # degrees

# Maths (See By Hand London, Circle Maths Explained!)
circumference = (fullCircle/desiredCircle) * waistMeasurement
radius = ((circumference + (4 * seamAllowance))/(2 * math.pi)) - seamAllowance

print(f'waist radius = {radius:.2f} inches')

# Fabric calculations.
#          w/2
#  - +--------------------+
#  | |\                   |
#  | | \  r               |
#  r |--\                 |
#  | | @ \                |
#  | |   /\               |
#  - |---  \              |
#  | |      \             |
#  | |       \            |
#  L |        \           |
#  | |-- w' ---\ |-- d ---|
#  | |         /          |
#  - |---------           |
#  l |   /\               |
#  - |---  \              |
#    |      \             |
#    |       \            |
#    |        \           |
#    |         \          |
#    |         /          |
#    +--------------------+

asciiArt = '''
           w/2
   - +--------------------+
   | |\                   |
   | | \  r               |
   r |--\                 |
   | | @ \                |
   | |   /\               |
   - |---  \              |
   | |      \             |
   | |       \            |
   L |        \           |
   | |-- w' ---\ |-- d ---|
   | |         /          |
   - |---------           |
   l |   /\               |
   - |---  \              |
     |      \             |
     | cut   \            |
     |   on   \           |
     |  fold   \          |
     |         /          |
     +--------------------+
'''
print(asciiArt)

# This assumes a front and a back piece with the 4 seam allowances above.
angleDegrees = desiredCircle/4
angle = math.radians(angleDegrees)
totalRadius = radius + desiredLength
patternWidth = totalRadius * math.sin(angle)
halfWidthRemaining = (fabricWidth/2) - patternWidth
waistCurveRise = radius * (1 - math.cos(angle))
waistCurveRun = radius * math.sin(angle)
angleAtPatternInterface = math.atan(waistCurveRun/totalRadius) # radians
skirtLengthRise = totalRadius * (1 - math.cos(angleAtPatternInterface))
wasteLength = waistCurveRise - skirtLengthRise
fabricLengthRequired = (2 * desiredLength) + wasteLength
absHalfWidth = math.fabs(halfWidthRemaining)

print(f'skirt pattern angle = {angleDegrees:.0f} degrees')
print(f'waist radius + skirt length = {totalRadius:.2f} inches')
print(f'pattern width at widest = {patternWidth:.2f} inches')
print(f'half width of fabric leftover = {halfWidthRemaining:.2f} inches')
print(f'height of waste piece between the two skirt panels = {wasteLength:.2f} inches')
print(f'fabric length required = {fabricLengthRequired:.2f} inches')

if halfWidthRemaining < 0.0:
    print(f'***************** Warning: pattern width exceeds folded fabric width by {absHalfWidth} inches.')

