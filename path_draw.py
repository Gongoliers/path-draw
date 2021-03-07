import turtle
from simple_path import SimplePath
from draw_utils import *
import maps

# Enter your path code here
path = SimplePath()

# Bounce
# path.addRotation(-61)
# path.addStraightAway(5.59)
# path.addRotation(117)
# path.addStraightAway(11.67)
# path.addRotation(-139)
# path.addStraightAway(10.98)
# path.addRotation(161)
# path.addStraightAway(10.98)
# path.addRotation(-81)
# path.addStraightAway(4.2)
# path.addRotation(-86)
# path.addStraightAway(10.05)
# path.addRotation(136)
# path.addStraightAway(5.55)

# Slalom
# path.addRotation(-43)
# path.addStraightAway(7.33)
# path.addRotation(47)
# path.addStraightAway(10)
# path.addRotation(47)
# path.addStraightAway(7.33)
# path.addRotation(-78)
# path.addStraightAway(5.58)
# path.addRotation(-93)
# path.addStraightAway(4.54)
# path.addRotation(-90)
# path.addStraightAway(6.5)
# path.addRotation(36)
# path.addStraightAway(12)
# path.addRotation(37)
# path.addStraightAway(10.19)

# Barrel Racing
path.addRotation(12)
path.addStraightAway(7)
path.addRotation(38)
path.addStraightAway(2)
path.addRotation(90)
path.addStraightAway(2.5)
path.addRotation(135)
path.addStraightAway(13)
path.addRotation(-45)
path.addStraightAway(3)
path.addRotation(-135)
path.addStraightAway(6)
path.addRotation(-120)
path.addStraightAway(3)
path.addRotation(-90)
path.addStraightAway(20)

# Galactic search A (red)
# path.addStraightAway(5)
# path.addRotation(27)
# path.addStraightAway(5.59)
# path.addRotation(-99)
# path.addStraightAway(7.91)
# path.addRotation(71)
# path.addStraightAway(13.5)

# Galactic search A (blue)
# path.addStraightAway(12.5)
# path.addRotation(-71)
# path.addStraightAway(7.91)
# path.addRotation(96)
# path.addStraightAway(5.59)
# path.addRotation(-33)
# path.addStraightAway(6)

# Galactic search B (red)
# path.addRotation(-27)
# path.addStraightAway(5.59)
# path.addRotation(74)
# path.addStraightAway(7.07)
# path.addRotation(-95)
# path.addStraightAway(7.07)
# path.addRotation(50)
# path.addStraightAway(10.69)

# Galactic search B (blue)
# path.addRotation(10)
# path.addStraightAway(12.75)
# path.addRotation(-56)
# path.addStraightAway(7.07)
# path.addRotation(91)
# path.addStraightAway(7.07)
# path.addStraightAway(3.64)


# Your start position
start = (5, 7.5)

maps.draw_map(maps.barrel_racing)
turtle.tracer(True)
draw_path(start[0], start[1], path)


turtle.done()
