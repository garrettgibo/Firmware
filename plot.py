from matplotlib import pyplot as plt
import numpy as np

my_data = np.genfromtxt('build/px4_sitl_default/tmp/data.csv', delimiter=',')
plt.title("Roll")
plt.xlabel("Time")
plt.plot(my_data[:,0], marker='o')
plt.figure()
plt.title("Pitch")
plt.xlabel("Time")
plt.plot(my_data[:,1], marker='o')
plt.show()
