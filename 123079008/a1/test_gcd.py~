from gcd import gcd
def test_gcd():
''' tests for diff gcd test cases. Also checks whether appropriate exception is raised'''
	assert gcd(48, 64) == 16
	assert gcd(44, 19) == 1
	assert gcd(2,2)==2

	try:
		a=0
		gcd(-5,-5)
		
	except ValueError:
		a=1
	if a==0:
		raise AssertionError, 'Value Error did not happen, argument was negative'
	try:
		a=0
		gcd(-5,-5)
		
	except ValueError:
		a=1
	if a==0:
		raise AssertionError, 'Value Error did not happen, argument was negative'
	try:
		a=0
		gcd('adadasd',10)
		
	except TypeError:
		a=1
	if a==0:
		raise AssertionError, 'TypeError did not happen, test case argument was a string'
	try:
		a=0
		gcd(5.678,10)
		
	except TypeError:
		a=1
	if a==0:
		raise AssertionError, 'TypeError did not happen- test case argument was a float'	
if __name__ == '__main__':
	test_gcd()
