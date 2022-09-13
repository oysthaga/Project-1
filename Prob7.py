import numpy as np
import matplotlib.pyplot as plt

# Plot from Problem 2; The
f = np.loadtxt('Prob2.txt')
x = f[:,0]; u = f[:,1]
plt.figure()
plt.plot(x, u, label='exact')
plt.xlabel('x'); plt.ylabel('u(x)')


# Problem 7
f = np.loadtxt('Prob7.txt')
x = f[:,0]; v = f[:,1]
plt.plot(x, v, '.', label='n_steps=1000')
plt.xlabel('x'); plt.ylabel('v(x)')
plt.legend()