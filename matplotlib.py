import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)
fig = plt.figure()
plt.plot(x, np.sin(x), '-')
plt.plot(x, np.cos(x), '--')
plt.show()


p_x = np.random.rand(100)
p_y = np.random.rand(100)
plt.scatter(p_x, p_y)
plt.show()

data = np.random.randn(10000)
plt.hist(data)
plt.show()

x = np.linspace(0, 10, 100)
fig = plt.figure()
plt.plot(x, np.sin(x), '-')
plt.plot(x, np.cos(x), '--')
plt.show()
fig.savefig('test.png')