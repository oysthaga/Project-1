import numpy as np
import matplotlib.pyplot as plt

f1 = np.loadtxt('Prob10_10.txt')
f2 = np.loadtxt('Prob10_100.txt')
f3 = np.loadtxt('Prob10_1000.txt')
f4 = np.loadtxt('Prob10_10000.txt')
f5 = np.loadtxt('Prob10_100000.txt')
f6 = np.loadtxt('Prob10_1000000.txt')

general = np.array([np.mean(f1[:,0]), np.mean(f2[:,0]), np.mean(f3[:,0]),
                    np.mean(f4[:,0]), np.mean(f5[:,0]), np.mean(f6[:,0])])
special = np.array([np.mean(f1[:,1]), np.mean(f2[:,1]), np.mean(f3[:,1]),
                    np.mean(f4[:,1]), np.mean(f5[:,1]), np.mean(f6[:,1])])
power = np.array([1, 2, 3, 4, 5, 6])

plt.figure()
plt.plot(power, general, '.', label='general')
plt.plot(power, special, '.', label='special')
plt.xlabel('$\log_{10}(n_{steps})$'); plt.ylabel('runtime (seconds)')
plt.legend()