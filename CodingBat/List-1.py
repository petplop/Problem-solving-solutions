#List-1 > first_last6

def first_last6(nums):
  if 6 == nums[0] or 6 == nums[-1]:
    return True
  else:
    return False


#List-1 > same_first_last

def same_first_last(nums):
  if len(nums) >= 1 and (nums[0] == nums[-1]):
    return True
  else:
    return False


#List-1 > make_pi

def make_pi():
  a = [3, 1, 4]
  return a


#List-1 > common_end

def common_end(a, b):
  if (a[0] == b[0]) or (a[-1] == b[-1]):
    return True
  else:
    return False


#List-1 > sum3

def sum3(nums):
  
  counter = 0
  
  for i in nums:
    counter += i
  return counter


#List-1 > rotate_left3

def rotate_left3(nums):

  array = [nums[1], nums[2], nums[0]]
  return array


#List-1 > reverse3

def reverse3(nums):

  return nums[::-1]

#List-1 > max_end3

def max_end3(nums):
  
  array = []
  M = max(nums[0], nums[-1])
  array.append(M) 
  return array * len(nums)
  
  
  
  #bad solution
  #array = []
  #
  #if nums[-1] < nums[0]:
  #  array.append(nums[0])
  #  array.append(nums[0])
  #  array.append(nums[0])
  #
  #elif nums[0] < nums[-1]:
  #  array.append(nums[-1])
  #  array.append(nums[-1])
  #  array.append(nums[-1])
  #
  #elif nums[0] == nums[-1]:
  #  array.append(nums[0])
  #  array.append(nums[0])
  #  array.append(nums[0]) 
  #
  #return array

#List-1 > sum2

def sum2(nums):
  if len(nums) == 1:
    return nums[0]
  else:
    return sum(nums[:2])
  

#List-1 > middle_way

def middle_way(a, b):
  
  array = []
  
  m = len(a) // 2
  mid = a[m]
  n = len(b) // 2 
  midb = b[n]
  
  array.append(a[m])
  array.append(b[n])
  
  return array
  
  # array = []

  # array.append(a[1])
  # array.append(b[1])

  # return array


#List-1 > make_ends

def make_ends(nums):
  
  array = []
  array.append(nums[0])
  array.append(nums[-1])
  return array


#List-1 > has23

def has23(nums):
  if 2 in nums or 3 in nums:
    return True
  
  else:
    return False
