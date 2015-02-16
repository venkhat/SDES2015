import text_plot
import math
import sys
def test_gcd():
	test_gen_sin_values()
	test_space_matrix()
	test_resize()
	test_gen_xaxis()
	test_gen_yaxis()
	test_superimpose()
	test_print_imagearray()
	test_plot()

def test_gen_sin_values():	
	'''checks whether x and their corresponding y values match
	checks whether returned tuple is in the required (list_x,list_y) format '''
	assert text_plot.gen_sin_values(2)==([0,math.pi],[math.sin(0),math.sin(math.pi)])
	assert text_plot.gen_sin_values(4)==([0,math.pi/2,math.pi,3*math.pi/2],[math.sin(0),math.sin(math.pi/2),math.sin(math.pi),math.sin(3*math.pi/2)])
def test_space_matrix():
	'''Checks whether a character matrix with spaces is generated
	Checks for different m by n corresponding to square and rectangular matrix'''
	assert text_plot.space_matrix(2,2)==[[' ',' '],[' ',' ']]
	assert text_plot.space_matrix(3,2)==[[' ',' '],[' ',' '],[' ',' ']]
def test_resize():
	'''Checks whether the given points are resized to cover the entire plot  
	Checks the resize functionality for image size other than 30 by 80'''
	assert text_plot.resize([0,1],[0,1])==([0,79],[0,29])
	assert text_plot.resize([0,1],[0,1],3,5)==([0,4],[0,2])
	assert text_plot.resize([-1,0,1],[-1,0,1])==([0,39,79],[0,14,29])

def test_gen_xaxis():
	'''Checks whether the generated xaxis co-ordinates are resized and are of correct length
	Checks for rectangular and square matrix dimensions as well'''
	assert text_plot.gen_xaxis([-1,0,1],[-1,0,1],3,3)==([0,1,2],[1,1,1])
	assert text_plot.gen_xaxis([-1,0,1],[-1,0,1],3,4)==([0,1,2,3],[1,1,1,1])
def test_gen_yaxis():
	'''Checks whether the generated yaxis co-ordinates are resized and are of correct length
	Checks for rectangular and square matrix dimensions as well'''
	assert text_plot.gen_yaxis([-1,0,1],[-1,0,1],3,3)==([1,1,1],[0,1,2])
	assert text_plot.gen_yaxis([-2,0,1],[-1,0,1],3,4)==([2,2,2],[0,1,2])
def test_superimpose():
	'''Checks whether the given character is placed in the given position
	Checks in a rectangular and Square matrix'''
	assert text_plot.superimpose([[1,2],[3,4]],[0,1],[0,1],'-')==[[1,'-'],['-',4]]
	assert text_plot.superimpose([[1,2,3],[4,5,6]],[0,2],[0,0],'*')==[[1,2,3],['*',5,'*']]
def test_print_imagearray():
	'''Checking whether rows of character matrix is printed first 
	Both sqaure matrix and rectangular is checked.'''
	import StringIO
	s = sys.stdout
	#test case1
	sys.stdout = output = StringIO.StringIO()# stdout will be redirected onto the required 'output'object 
	text_plot.print_imagearray([['1','2'],['3','4']])
	assert output.getvalue()=='12\n34\n'	#output.getvalue() has the stdout content in the form of string
	output.close() #closing that object
	#test case 2
	sys.stdout = output2 = StringIO.StringIO()# stdout will be redirected onto the required 'output'object 
	text_plot.print_imagearray([[' ',' ','*'],[' ',' ','*']])
	assert output2.getvalue()=='  *\n  *\n'	#output.getvalue() has the stdout content in the form of string
	output2.close() #closing that object

	sys.stdout = s #restoring the sys.stdout as the terminal screen

def test_plot():
	'''Checking for proper rescaling, axis geneartion, plotting 1 points, plotting lines in different quadrants''' 
	assert text_plot.plot([0],[0],2,2)==[['|',' '],['*','_']] #checking single point plot
	assert text_plot.plot([-1],[-1],3,3)==[['_','_','|'],[' ',' ','|'],['*',' ','|']] #checking single point plot in third quadrant
	assert text_plot.plot([0,1,2],[1,1,1],3,3)==[['*','*','*'],['|',' ',' '],['|','_','_']]#checking for a line y=1 paralel to x axis
	assert text_plot.plot([1,1,1],[0,1,2],3,4)==[['|',' ',' ','*'],['|',' ',' ','*'],['|','_','_','*']]#checking for a line x=1 paralel to y axis
	assert text_plot.plot([0,0],[1,2],2,3)==[['*',' ',' '],['*','_','_']]#checking for a line on y axis, with x=0
	assert text_plot.plot([0,0,0],[-1,0,1],3,3)==[['*',' ',' '],['*','_','_'],['*',' ',' ']]#checking for a line on y axis, but with positive and negative co-ordinates

if __name__ == '__main__':
	test_gcd()
	

