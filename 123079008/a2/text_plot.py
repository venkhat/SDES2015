import sys
import math

# All functions are described below
def plot(x,y,m=30,n=80):
	'''Generates a plot with the given points list_x,list_y. Default plot size is 30 by 80
	Scales the points to cover the entire plot size. 
	Draws x axis and y axis'''
	# Genarate a background image matrix initialized with space ' '.
	img=space_matrix(m,n)		
	# resize the given points to cover the entire plot size
	x_resized,y_resized=resize(x,y,m,n)
	# Generates x axis co-ordinates
	xaxis_x,xaxis_y=gen_xaxis(x,y,m,n)
	# Superimposes '_' on image to show the xaxis in the respective coordinates
	img_xaxis=superimpose(img,xaxis_x,xaxis_y,'_')
	#Generates y axis co-ordinates
	yaxis_x,yaxis_y=gen_yaxis(x,y,m,n)
	# Superimposes '|' on the previous image to indicate y axis
	img_xyaxis=superimpose(img_xaxis,yaxis_x,yaxis_y,'|')
	# Superimposes '*' onto the image, in the given coordinates 
	img_final=superimpose(img_xyaxis,x_resized,y_resized,'*')
	#prints the image matrix
	print_imagearray(img_final)
	return img_final

def space_matrix(m=30,n=80):
	'''Generates a character matrix of given m by n size with all characters initialised to space. 
	This will act as the backround image for the plot. Arguments: m,n -size of matrix; Returns- the matrix'''
	img=[]
	for i in range(m):
		img.append([])
		img[i]=n*[' ']#each row is initialized with n spaces ' '.
	return img

def resize(x,y,m=30,n=80):
	'''the given points are resized to cover the entire plot.
	Takes in image size m, n as arguments with default being 30 by 80 '''
	  
	xmin=min(x+[0])#i'm adding 0,0 to the set of points , to have 0,0 as refernce
	xmax=max(x+[0])
	x_range=xmax-xmin
	ymin=min(y+[0])
	ymax=max(y+[0])
	y_range=ymax-ymin
	x1=[]
	y1=[]
	if x_range==0:#when all x values are zero
		x1=x1+len(x)*[0]
	else:
		for x_i in x:
			temp=(n-1)*(x_i-xmin)/(xmax-xmin)
			x1=x1+[int(round(temp))]
	
	if y_range==0:# when all y values are zero
		y1=y1+len(y)*[0]
	else:
		for y_i in y:
			temp=(m-1)*(y_i-ymin)/(ymax-ymin)
			y1=y1+[int(round(temp))]
	return x1,y1	
	
def superimpose(img,x,y,c):
	'''replaces the (x_i,y_i) position with character c. 
	Arguments: (list_x,list_y) with possible x in [0,m-1] and y in [0,n-1]; Returns the superimposed matrix'''
	m=len(img)
	for i in range(len(x)):#row is yaxis, component y=0 means last row m-1
		img[m-1-y[i]][x[i]]=c
	return img
	

def gen_xaxis(x,y,m=30,n=80):#produces n points
	'''Generates points for x axis
	Xaxis is represented as y=0 for every x.
	So, generates x=[0,1..,n-1] and for each x, y is same --resized of y=0''' 
	ymin=min(y+[0])
	ymax=max(y+[0])
	y_range=ymax-ymin
	x1=range(n)
	if y_range==0:#if all points are  y=0
		y1=n*[0]
	else:
		temp=(m-1)*(0-ymin)/(ymax-ymin)
		y1=n*[int(round(temp))]
	return x1,y1
	
def gen_yaxis(x,y,m=30,n=80):#produces m points 
	'''Generates points for y axis
	Yaxis is represented as x=0 for every y.
	So, generates y=[0,1..,m-1] and for each y, same x i.e. resized of x=0''' 
	xmin=min(x+[0])
	xmax=max(x+[0])
	x_range=xmax-xmin
	#yaxis generation
	y1=range(m)
	if x_range==0:#if all points have x=0
		x1=m*[0]
	else:
		temp=(n-1)*(0-xmin)/(xmax-xmin)
		x1=m*[int(round(temp))]
	return x1,y1

def gen_sin_values(n=30):#n is precision for [0,360] n=30
	'''Generates argument 'n' length of sine values between 0,2*pi and returns the x_list,y_list '''
	x=[]
	y=[]
	for i in range(n):
		x=x+[(i*2*math.pi)/n]
		y=y+[math.sin((i*2*math.pi)/n)]
	return x,y


def print_imagearray(img):#img contains a m*n character array
	'''Prints the given character matrix on to stdout'''
	for line in img:
		for i in line:
			sys.stdout.write(i)
		sys.stdout.write('\n')

##
if __name__ == '__main__':	
	m=30
	n=80
	value_len=80
	x,y=gen_sin_values(value_len)
	plot(x,y,m,n)
## this is the executing main code.

