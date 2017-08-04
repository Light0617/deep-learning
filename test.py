#!usr/bin/python
import math
def z(x):
	return 1 / (1 + math.exp(-x))
def zz(x):
	return math.exp(-x)
def zzz(x):
	return (1 + math.exp(-x)) ** (-2)
h0 = z(3.5)
h1 = z(1 - h0)
h2 = z(-2- h1)
print '3...'
print h0, h1, h2
print '3-2: y=', -0.7 * h1
print '4...'
h0 = z(-1.8 + 0.4)
z2 = -0.1 * (-8) + 0.5 * 0.4 + 0.4 
print 0.1 * zzz(z2) * zz(z2)

h = z(1)
for i in range(3):
	h = z(1 - 2 * h)
print h

