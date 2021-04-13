#List-2 > count_evens

def count_evens(nums):
  
  counter = 0
  
  for i in nums:
    if i % 2 == 0:
      counter += 1
  return counter
    

#List-2 > big_diff

def big_diff(nums):
  return max(nums) - min(nums)
 

#List-2 > centered_average

def centered_average(nums):
  nums.sort()
  sum = 0
  maxv = nums[-1]
  minv = nums[0]
  #can use max() and min() instead of sorting too.
  for i in range(0, len(nums)):
    sum += nums[i]
  
  return (sum - maxv - minv) / (len(nums) -2) 
  
  #return (sum(nums) - max(nums) - min(nums)) / (len(nums) -2)


#List-2 > sum13

def sum13(nums):
  
  sum = 0
  
  if len(nums) > 0 and nums[0] != 13:
    sum = nums[0]
  
  
  for i in range(1, len(nums)):
    if nums[i] != 13 and nums[i-1] != 13:
      sum+=nums[i]
  
  return sum


#List-2 > sum67

def sum67(nums):
  
  flag = True
  
  sum = 0
  
  for i in range(0, len(nums)):
    
    if nums[i] == 6:
      flag = False
    elif nums[i] == 7 and flag == False:
      flag = True
    elif flag == True:
      sum+=nums[i]
    
  return sum


#List-2 > has22

def has22(nums):
  
  for i in range(0, len(nums)-1):
    if 2 == nums[i] and 2 == nums[i+1]:
      return True
  return False
