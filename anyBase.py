"""
AnyBase
Write a function that converts from any base to any other base.
String convertBase(String input, int oldBase, int newBase);
oldBase, newBase = 2 .. 36, use digits 0..9A..Z
input 8,10,2 = output: 1000
"""

def convertBase10(val, oldBase):
	power = 0
	value = 0
	for i in range(len(val)-1, -1, -1):
		num = val[i]
		if num != '0':
			if num.isalpha():
				num = ord(num.upper())-ord('A')
			else:
				num = int(num)
			if num > oldBase-1:
				raise ValueError("input is not valid")
			value = value + (num-1)*oldBase**power
		power += 1
	return value

def convert10ToBase(num, newBase):
	result = []
	while num > 0:
		reminder = num%newBase
		if reminder > 9:
			char = chr(ord(A)+reminder)
		else:
			char = str(reminder)
		result = [char] + result
		num = num/newBase
	return ''.join(result)

def validBase(base):
	if base < 2 or base > 36:
		return False
	else:
		return True

def anyBase(val, oldBase, newBase):
	if not validBase(oldBase) or not validBase(newBase):
		raise ValueError("Base is not valid")

	if oldBase == newBase:
		return val

	# convert to base 10
	if oldBase != 10:
		num = convertBase10(val, oldBase)
	else:
		num = int(val)

	return convert10ToBase(num, newBase)

print anyBase('1030',4,11)
