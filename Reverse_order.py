# def reversed_list(lst1, lst2):
#  lst3 = reversed(lst2)
#  for index in range(len(lst1)):
#    if lst1[index] == lst3[index]:
#      if lst1[index] == lst3[index]:
#        if lst1[index] == lst3[index]:
#          return True
#  else:
#    return False

# Make a function that works out if the two lists are the same when one is reversed

def reversed_list(lst1, lst2):
    for index in range(len(lst1)):
        if lst1[index] != lst2[len(lst2) - 1 - index]:
            return False
    return True


print(reversed_list([1, 2, 3], [3, 2, 1]))

print(reversed_list([1, 5, 3], [3, 2, 1]))