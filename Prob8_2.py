# Should probably have done this in C++, but it's late and I have to finish 
# the report. 
import numpy as np

# n_steps from 10^1 to 10^7
'''
f1 = np.loadtxt('Prob8_10.txt')
f2 = np.loadtxt('Prob8_100.txt')
f3 = np.loadtxt('Prob8_1000.txt')
f4 = np.loadtxt('Prob8_10000.txt')
f5 = np.loadtxt('Prob8_100000.txt')
f6 = np.loadtxt('Prob8_1000000.txt')
f7 = np.loadtxt('Prob8_10000000.txt')
'''
def u(x):
    return ( 1-(1-np.exp(-10))*x - np.exp(-10*x) ) # Exact solution

'''
# Find the maximum value of the logarithm of the relative error: 
epsmax1 = -100
for line in f1[1:-1]:
    if np.log10(abs( (u(line[0])-line[1])/u(line[0]) ) ) > epsmax1:
        epsmax1 = np.log10(abs( (u(line[0])-line[1])/u(line[0]) ) )
        
epsmax2 = -100
for line in f2[1:-1]:
    if np.log10(abs( (u(line[0])-line[1])/u(line[0]) ) ) > epsmax2:
        epsmax2 = np.log10(abs( (u(line[0])-line[1])/u(line[0]) ) )

epsmax3 = -100
for line in f3[1:-1]:
    if np.log10(abs( (u(line[0])-line[1])/u(line[0]) ) ) > epsmax3:
        epsmax3 = np.log10(abs( (u(line[0])-line[1])/u(line[0]) ) )

epsmax4 = -100
for line in f4[1:-1]:
    if np.log10(abs( (u(line[0])-line[1])/u(line[0]) ) ) > epsmax4:
        epsmax4 = np.log10(abs( (u(line[0])-line[1])/u(line[0]) ) )
        
epsmax5 = -100
for line in f5[1:-1]:
    if np.log10(abs( (u(line[0])-line[1])/u(line[0]) ) ) > epsmax5:
        epsmax5 = np.log10(abs( (u(line[0])-line[1])/u(line[0]) ) )

epsmax6 = -100
for line in f6[1:-1]:
    if np.log10(abs( (u(line[0])-line[1])/u(line[0]) ) ) > epsmax6:
        epsmax6 = np.log10(abs( (u(line[0])-line[1])/u(line[0]) ) )
        
epsmax7 = -100
for line in f7[1:-1]:
    if np.log10(abs( (u(line[0])-line[1])/u(line[0]) ) ) > epsmax7:
        epsmax7 = np.log10(abs( (u(line[0])-line[1])/u(line[0]) ) )
'''
epsmax = [epsmax1, epsmax2, epsmax3, epsmax4, epsmax5, epsmax6, 
          epsmax7]
for e in epsmax:
    print(e) 
# I print the maximum values, then copy them into a textfile and 
# round them of by hand. 
