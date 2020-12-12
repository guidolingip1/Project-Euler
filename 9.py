#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
from math import sqrt

for a in range(1,1000):
	for b in range(1,1000):
		if b > a:
			c = a*a + b*b
			c = sqrt(c)
			if a + b + c == 1000:
				print("({},{},{}) = {} ".format(a,b,c, a*b*c))