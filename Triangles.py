

def triangles(a,b,c):
	if a <= 0 or b <= 0 or c <= 0:
		# Sides are 0 or less. Can't form a triangle.
		print "Not a triangle. Bad values"
		return
	
	if b >= a+c or a >= c+b or c >= a+b:
		print "Not a triangle. One side is too big"
		return

	if a == b == c:
		print "Equilateral"
	elif a == b or b == c or c == a:
		print "Isosceles"
	else:
		print "Scalene"

triangles(5,5,10)
triangles(-1,-1,-1)
triangles(0,10,10)
triangles(0,0,0)