from module import get_player
import numpy as np


def stat():
  weights = []
  heights = []
  names = []

  for i in range(1, 10):
    player = get_player(i)
    for j in player:
      value = j[1].weight
      value2 = j[1].height
      name = j[1].first_name
      inch, feet = (value2).split("-")
      feet = int(feet)
      # coverting to inches
      inch = int(inch) * 12
      # converting to cm
      height = ((feet + inch) * 2.54)

      value = int(value)
      weights.append(value)
      heights.append(height)
      names.append(name)

  return weights, heights, names

def statistics():
  mean = 0
  median = 0
  weight, height, name = stat()
  mean = np.mean(weight)
  median = np.median(weight)
  return mean, median
  
