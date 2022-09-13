import numpy as np
import matplotlib.pyplot as plt

f = np.loadtxt('Prob2.txt')
x = f[:,0]; u = f[:,1]
plt.figure()
plt.plot(x, u, '.')
plt.xlabel('x'); plt.ylabel('u(x)')