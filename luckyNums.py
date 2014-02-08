"""
Are they Luck Compatible?
Two numbers are considered to be Luck Compatible, if they have the same "lucky digit". 
To calculate lucky digit, you are expected to add all the digits of the given number. 
If the result is not a single digit, then add all its digits, and keep doing this till 
you are left with a single digit response.
 
For example, 45 and 63 are compatible, as their lucky digits are 9.
 
if Input is 98765, you add up the digits 35, the you add up 3 and 5 to get 8.
 
Write the function boolean luckCompatible(int a, int b) return true if they are 
compatible, and false if they are not.
"""

def getToSingleNum(num):
	lucky = 0
	while num > 0:
		lucky += num%10
		num = num/10

	if lucky > 10:
		return getToSingleNum(lucky)
	else:
		return lucky

def luckyDigit(a, b):
	luckyA = getToSingleNum(a)
	luckyB = getToSingleNum(b)

	return luckyA == luckyB

print luckyDigit(45,63)
print luckyDigit(98765,98)
print luckyDigit(99,49)

""""
Forward String triangle.
Given a long string with words [a-z ], you are expected to split the string 
in N strings, so that first string is one word long, and each subsequent string 
s longer than the previous one.

if input is "this is a very good question that has some nice test data"
output =
this
is a very
good question
that has some nice test data
"""

def forwardStringTriangle(words):
	# convert to list
	wordList = words.split()

	limit = 0
	line = ''
	for word in wordList:
		line = line + word
		if len(line) > limit:
			# Don't want a newline               in the first line
			if limit > 0:
				print ''
			print line,
			limit = len(line)
			line = ''
		else:
			line += ' '
	# if there is any remaining words
	if line:
		print line
	else:
		# print something so it adds a newline
		print ''



forwardStringTriangle('this is a very good question that has some nice test data')
forwardStringTriangle('this')
forwardStringTriangle('really long realllllly loong long long loooooooong')