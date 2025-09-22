#!/usr/bin/env python3
from task_01_duck_typing import Circle, Rectangle, shape_info

circle = Circle(radius=5)
rectangle = Rectangle(width=4, height=7)

circle = Circle(5)
rectangle = Rectangle(4, 7)

shape_info(circle)
shape_info(rectangle)