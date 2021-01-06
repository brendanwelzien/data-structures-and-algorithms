​def findDivisible(array, n):
  total = 0

  for a in range(0, n):
    for b in range(a+1, n):
      if (array[a] % array[b] == 0 or array[b] % array[a] == 0:
        total +=1
  return total



if __name__ =='__main__':
  array = [2, 3, 6, 7, 4]
  n = len(array)
  print(findDivisible(array, n))
