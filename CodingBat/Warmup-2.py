#Warmup-2 > string_times

def string_times(str, n):
  if n >= 0:
    return n*str


#Warmup-2 > front_times

def front_times(str, n):
  front = 3
  if front > len(str):
    front = len(str)
  front = str[:front]
  
  result = ""
  for element in range(n):
    result += front
  return result


#Warmup-2 > string_bits

def string_bits(str):
  third = str[::2]
  return third


#Warmup-2 > string_splosion

def string_splosion(str):
  result = ""
  for c in range(len(str)):
    result += str[:c+1]
  return result


#Warmup-2 > last2

def last2(str):
  
  if len(str) <= 2:
    return 0

  substring = str[-2:]
  
  count = 0
  
  for i in range(len(str)-2):
    test = str[i:i+2]
    if test == substring:
      count += 1
    
  return count


#Warmup-2 > array_count9

def array_count9(nums):
  
  count = 0
  
  for i in nums:
    if i == 9:
      count += 1
      
  return count
      

#Warmup-2 > array_front9

def array_front9(nums):
  
  if len(nums) < 4:
    for i in nums:
      if i == 9:
        return True
  
  for i in nums:
    if 9 in nums[:4]:
      return True
  
  else:
    return False


#Warmup-2 > array123

def array123(nums):
  # Note: iterate with length-2, so can use i+1 and i+2 in the loop
  for i in range(len(nums)-2):
    if nums[i]==1 and nums[i+1]==2 and nums[i+2]==3:
      return True
  return False


#Warmup-2 > string_match

def string_match(a, b):
  # Figure which string is shorter.
  shorter = min(len(a), len(b))
  count = 0
  
  # Loop i over every substring starting spot.
  # Use length-1 here, so can use char str[i+1] in the loop
  for i in range(shorter-1):
    a_sub = a[i:i+2]
    b_sub = b[i:i+2]
    if a_sub == b_sub:
      count = count + 1

  return count

