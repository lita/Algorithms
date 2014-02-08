def findSum(arr, largestSum):
  if largestSum in arr:
    return True
  elif len(arr) < 2:
    return False
  else:
    for i in range(len(arr)):
      for j in range(i+1,len(arr)):
        arr2 = arr[:]
        sum = arr[i]+arr[j]
        if largestSum == sum:
          return True
        else:
          arr2.remove(arr[i])
          arr2.remove(arr[j])
          arr2.append(sum)
          return findSum(arr2, largestSum)
        
def ArrayAddition(arr): 

  # code goes here
  # find largest num
  largestSum = 0
  for num in arr:
    if num > largestSum:
      largestSum = num
  
  arr.remove(largestSum)
  findSum(arr, largestSum)
  
  return text + more 


print findSum([1,2,3],100)
















  