"""
Given an array, print the values of the array in a "spiral".
Start from top left
"""

import numpy

def assignLayer(upperX, upperY, offsetX, offsetY, spiral, num, index):
	
	# top
	counterX = offsetX
	while upperX > counterX:
		if index >= len(num):
			return None

		spiral[offsetY][counterX] = num[index]
		index += 1
		counterX += 1

	# right
	counterY = offsetY+1
	counterX -= 1

	while upperY > counterY:
		if index >= len(num):
			return None

		spiral[counterY][counterX] = num[index]

		index += 1
		counterY += 1

	# bottom
	counterX -= 1
	counterY -= 1
	while counterX >= offsetX:
		if index >= len(num):
			return None

		spiral[counterY][counterX] = num[index]
		index += 1
		counterX -= 1

	# left
	counterY -= 1
	counterX += 1
	while counterY > offsetY:
		if index >= len(num):
			return None

		spiral[counterY][counterX] = num[index]
		index += 1
		counterY -= 1

	return index

def spiralMethod (n,m,num):
	"""
	n - width of the matrix
	m - height of the matrix
	"""
	if n == 0 or m == 0:
		return None
	# Generate a NxM array
	#spiral = [['' for i in xrange(m)] for j in xrange(n)]
	spiral = numpy.zeros(shape=(m,n))

	lowerX, lowerY = 0,0
	index = 0 
	while lowerX <= n or lowerY <= m:
		index = assignLayer(n, m, lowerX, lowerY, spiral, num, index)
		
		if not index:
			break

		n -= 1
		m -= 1
		lowerX += 1
		lowerY += 1

	print spiral

l = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]

spiralMethod(3,3,l)
print ''
spiralMethod(3,5,l)
