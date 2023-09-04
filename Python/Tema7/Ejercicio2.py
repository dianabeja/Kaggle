#Submodules
import numpy
print("numpy.random is a", type(numpy.random))
print("it contains names such as...",
      dir(numpy.random)[-15:]
     )

# Roll 10 dice
rolls = numpy.random.randint(low=1, high=6, size=10)
print(rolls)

#Three tools for understanding strange objects
type(rolls)

print(dir(rolls))

# If I want the average roll, the "mean" method looks promising...
rolls.mean()

# Or maybe I just want to turn the array into a list, in which case I can use "tolist"
rolls.tolist()

# That "ravel" attribute sounds interesting. I'm a big classical music fan.
help(rolls.ravel)

# Okay, just tell me everything there is to know about numpy.ndarray
# (Click the "output" button to see the novel-length output)
help(rolls)