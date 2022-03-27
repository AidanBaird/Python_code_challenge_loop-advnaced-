#def same_values(lst1, lst2):
#  lst3 = []
#  for num in lst1:
#    for num1 in lst2:
#      if num1 in lst1 == num in lst2:
#        lst3.append([num, num1])
#  return lst3

# Definte a variable that matches two corresponding list indexes and returns them into a seperate list

def same_values(lst1, lst2):
  lst3 = []
  for index in range(len(lst1)):
    #print(index)
    if lst1[index] == lst2[index]:
      lst3.append(index)
  return lst3


print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))