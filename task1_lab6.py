from module_lab6 import *

ti_pw1, yi_pw1 = np.genfromtxt('PW1.dat', delimiter=',', skip_header=1).T
ti_pw2, yi_pw2 = np.genfromtxt('PW2.dat', delimiter=',', skip_header=1).T
ti_iw1, yi_iw1 = np.genfromtxt('IW1.dat', delimiter=',', skip_header=1).T

tj = np.arange(1980, 2015, 0.5)

# TODO - your code here

yj = interpolate_linear(ti_iw1, yi_iw1, tj, default=None)
print(yj)

[1980.4583, 1980.5417]