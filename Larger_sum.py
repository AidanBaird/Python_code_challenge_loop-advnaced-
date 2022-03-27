# Define a function that returns the list with the highest sum

def larger_sum(lst1, lst2):
  sum1 = 0
  sum2 = 0
  for num in lst1:
    sum1 += num
  for num in lst2:
    sum2 += num
  #print(sum1)
  #print(sum2)
  if sum1 >= sum2:
    return lst1
  else:
    return lst2

print(larger_sum([1, 9, 5], [2, 3, 7]))