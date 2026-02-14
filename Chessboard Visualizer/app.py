# This program overlays a mathematical surface on top of a chessboard pattern using matplotlib library.

#Importing Libaries
import matplotlib.pyplot as plt
import numpy as np

#Creating the grid (X and Y values)

#defining resolution (step size)
dx, dy = 0.015, 0.05 #(small step for smoother image, big step)

#creating numbers frim -4 to 4 with step dx
x = np.arange(-4.0, 4.0, dx)

#creating numbers frim -4 to 4 with step dy
y = np.arange(-4.0, 4.0, dy)

#creating coordinate matrices (combining every x value with every y value)
X, Y = np.meshgrid(x, y)

#mapping image over this coordinate range
extent = np.min(x), np.max(x), np.min(y), np.max(y)


#Creating the chessboard pattern

#creating an 8 x 8 matrix where each element is i + j 
# pattern: 0 1 2 3 4 5 6 7, 1 2 3 4 5 6 7 8...
#creating alternating squares of 0s and 1s
z1 = np.add.outer(range(8), range(8)) % 2

#plotting it
plt.imshow(z1, cmap="binary_r", interpolation="nearest", extent=extent, alpha=1)


#Creating mathematical function (wavy surface that fades toward the edges)
def chess(x, y):
    return (1 - x / 2 + x ** 5 + y ** 6) * np.exp(-(x ** 2 + y ** 2))

#evaluating the function
z2 = chess(X, Y)


#Overlaying the Surface on the Chessboard
img = plt.imshow(z2, cmap="plasma", alpha=0.7, interpolation="bilinear", extent=extent)
plt.colorbar(img)
plt.title("Chess Board Visualisation using Python")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.show