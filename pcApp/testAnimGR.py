# Importing libraries
import matplotlib.pyplot as plt
import numpy as np
import math
plt.figure(figsize=(15, 6))
# Placing the plots in the plane
plot1 = plt.subplot2grid((2, 5), (0, 1), rowspan=1, colspan=10)
plot2 = plt.subplot2grid((2, 5), (1, 1), rowspan=1, colspan=10)
# plot3 = plt.subplot2grid((3, 3), (1, 0), rowspan=2)

# Using Numpy to create an array x
x = np.arange(1, 100000000)

# Plot for square root
plot2.plot(x, x**0.5)
plot2.set_title('Square Root')

# Plot for exponent
plot1.plot(x, x**0.5)
plot1.set_title('Exponent')

# Plot for Square
# plot3.plot(x, x*x)
# plot3.set_title('Square')

# Packing all the plots and displaying them
plt.tight_layout()
plt.show()
