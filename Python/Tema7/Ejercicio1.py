#Imports
import math

print("It's math! It has type {}".format(type(math)))
print(dir(math))
print("pi to 4 significant digits = {:.4}".format(math.pi))
print(math.log(32, 2))
help(math.log)
help(math)
import math as mt
print(mt.pi)

from math import *
print(pi, log(32, 2))

from math import log, pi
from numpy import asarray