"""
Given a sequence, find the length of the longest palindromic subsequence in it.
For example, if the given sequence is "BBABCBCAB", then the output should be 7 
as "BABCBAB" is the longest palindromic subseuqnce in it.
"""

"""
Dynamic Programing Problem
"""
def findLongestPalindrome(n):

	# varaible to store subproblems
	L = [[[]]*len(n)]*len(n)

	for i in range(len(n)):
		#initalize same indexes to 1
		L[i][i] = 1

	for c in range(2, len(n)+1):
		for i in range(0, len(n)-c+1):
			j = i + c-1
			if n[i] == n[j] and c == 2:
				L[i][j] = 2
			elif n[i] == n[j]:
				L[i][j] = L[i+1][j-1]+2
			else:
				L[i][j] = max(L[i][j-1], L[i+1][j])
	print L
	return L[0][len(n)-1]

n = "BBABCBCAB"

result = findLongestPalindrome(n)
print result