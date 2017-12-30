# Convert Binary to Decimal number [0,1,1,0] => 6
def binary_array_to_number(arr):
  # your code
  exp = 0
  decimal = 0
  for i in range(len(arr)-1, -1, -1):
      if arr[i] == 1:
          decimal+=2**exp
      exp+=1
      
  return decimal

# Optimal Soltn:

def binary_array_to_number2(arr):
  return int("".join(map(str, arr)), 2)