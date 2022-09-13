import numpy as np
import matplotlib.pyplot as plt

# Plot from Problem 2


f1 = np.loadtxt('Prob8_10.txt')
f2 = np.loadtxt('Prob8_100.txt')
f3 = np.loadtxt('Prob8_1000.txt')

x1 = f1[1:-1, 0]; v1 = f1[1:-1, 1]
u1 = 1 - (1-np.exp(-10))*x1 - np.exp(-10*x1)
x2 = f2[1:-1, 0]; v2 = f2[1:-1, 1]
u2 = 1 - (1-np.exp(-10))*x2 - np.exp(-10*x2)
x3 = f3[1:-1, 0]; v3 = f3[1:-1, 1]
u3 = 1 - (1-np.exp(-10))*x3 - np.exp(-10*x3)

logdel1 = np.log10( abs(u1-v1) ); logdel2 = np.log10( abs(u2-v2) )
logdel3 = np.log10( abs(u3-v3) )

plt.figure()
plt.subplot(311)
plt.xlabel('x'); plt.ylabel('$\log_{10}(\Delta_i)_{n_{steps}=10}$')
plt.plot(x1, logdel1)
plt.subplot(312)
plt.xlabel('x'); plt.ylabel('$\log_{10}(\Delta_i)_{n_{steps}=100}$')
plt.plot(x2, logdel2)
plt.subplot(313)
plt.xlabel('x'); plt.ylabel('$\log_{10}(\Delta_i)_{n_{steps}=1000}$')
plt.plot(x3, logdel3)

logeps1 = np.log10( abs( (u1-v1)/u1 ) ); logeps2 = np.log10( abs( (u2-v2)/u2 ) )
logeps3 = np.log10( abs( (u3-v3)/u3 ) )

plt.figure()
plt.subplot(311)
plt.xlabel('x'); plt.ylabel('$\log_{10}(\epsilon_i)_{n_{steps}=10}$')
plt.plot(x1, logeps1)
plt.subplot(312)
plt.xlabel('x'); plt.ylabel('$\log_{10}(\epsilon_i)_{n_{steps}=100}$')
plt.plot(x2, logeps2)
plt.subplot(313)
plt.xlabel('x'); plt.ylabel('$\log_{10}(\epsilon_i)_{n_{steps=1000}$')
plt.plot(x3, logeps3)




'''
f4 = np.loadtxt('Prob8_10000.txt')
f5 = np.loadtxt('Prob8_100000.txt')
f6 = np.loadtxt('Prob8_1000000.txt')
f7 = np.loadtxt('Prob8_10000000.txt')
'''
