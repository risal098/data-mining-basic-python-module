import math


def entropy(*args):
	sums=sum(args)
	result=0
	for p in args:
		result-=(p/sums)*math.log2((p/sums))
	return result
