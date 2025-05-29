import math

def calculate_area(radius):
  """
  Calculates the area of a circle given its radius.

  Args:
    radius: The radius of the circle (integer or float).

  Returns:
    The area of the circle (float). Returns 0 if the radius is negative.
  """
  if radius < 0:
    return 0
  else:
    return math.pi * (radius ** 2)