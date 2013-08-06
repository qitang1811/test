def pow(num, e):
	"""
	calculate the pow of num
	"""

	if e < 0:
		return -1
	base = 1
	for i in range(e):
		base *= num
	return base

def main():
	num = 2
	e = 2
	print pow(num, e)

if __name__=="__main__":
	main()