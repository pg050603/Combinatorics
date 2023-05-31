from module_lab6 import *

ti_pw1, yi_pw1 = np.genfromtxt('PW1.dat', delimiter=',', skip_header=1).T
ti_pw2, yi_pw2 = np.genfromtxt('PW2.dat', delimiter=',', skip_header=1).T
ti_iw1, yi_iw1 = np.genfromtxt('IW1.dat', delimiter=',', skip_header=1).T

tj = np.arange(1980, 2015, 0.5)

# TODO - your code here

yj_iw1, tj_interpolated_iw1 = interpolate_linear(ti_iw1, yi_iw1, tj, default=0)

# yj_pw1 = interpolate_linear(ti_pw1, yi_pw1, tj, default=None)
# yj_pw2 = interpolate_linear(ti_pw2, yi_pw2, tj, default=None)

# print(yj_iw1)
# print(tj_interpolated_iw1)
