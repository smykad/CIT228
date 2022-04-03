from random import Random
import matplotlib.pyplot as plt
from random_walk import RandomWalk

# Make a random walk
rw = RandomWalk()
rw.fill_walk()

#plot the points in the walk
plt.style.use('classic')
fig, ax = plt.subplots(figsize=(15, 9))

point_numbers = range(rw.num_points)
ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, s=15)

# Emphasize the first and last points
ax.scatter(0,0, c='green', edgecolors='none', s=100)
ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)
plt.show()

# Hands on 15-3

"""
*************************
*   Commented out 15-3  *
*************************
plt.style.use('classic')

fig, ax = plt.subplots(figsize=(15,9))
point_numbers = range(rw.num_points)
ax.plot(rw.x_values, rw.y_values, linewidth=1)
plt.show()
"""