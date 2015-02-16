def gcd(a, b):
	"""Returns the Greatest Common Divisor of the
	two integers passed as arguments.
	Args:
	a: a positive integer
	b: positive integer
	Returns: Greatest Common Divisor of a and b
	"""
	if (type(a)==int or type(a)==long) and (type(b)==int or type(b)==long):
		pass
	else:
		raise TypeError
		
		
		
	if a <= 0 or b <= 0:
		raise ValueError
		
	
	while b != 0:
		a, b = b, a % b
	return a
