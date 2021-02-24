from matplotlib import pyplot as plt
import numpy as np

my_data = np.genfromtxt('build/px4_sitl_default/tmp/data.csv', delimiter=',')
plt.title("Roll")
plt.xlabel("Iteration")
plt.plot(my_data[:,0], marker=',')
plt.plot(my_data[:,1], marker=',')
plt.figure()
plt.title("Force")
plt.xlabel("Iteration")
plt.plot(my_data[:,2], marker=',')
plt.show()
