# Define a function that will add up your power_level and stop once it is at or above 9000

def over_nine_thousand(lst):
  power_level = 0
  for num in lst:
    power_level += num
    if power_level >= 9000:
      break
  return power_level

print(over_nine_thousand([8000, 900, 120, 5000]))