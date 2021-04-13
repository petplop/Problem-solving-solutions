#String-2 > double_char

def double_char(str):
  
  this = ""
  
  for c in str:
    this += c*2
  return this


#String-2 > count_hi

def count_hi(str):
  counter = 0
  
  for i in range(len(str)):
    if "hi" == str[i:i+2]:
      counter+=1
  
  return counter


#String-2 > cat_dog

def cat_dog(str):
  
  cat_count = 0
  dog_count = 0
  
  #Checking for elements in range of the length of our string
  
  for i in range(len(str)):
    if "cat" == str[i:i+3]: #since "cat" & "dog"  is are 
      cat_count += 1        #3 letter string we increment
    if "dog" == str[i:i+3]: #i by 3 for every iteration
      dog_count += 1        #then add to count
  
  if cat_count == dog_count: #check if they have the same value
    return True
  else:
    return False


#String-2 > count_code

def count_code(str):
  
  counter = 0
  for i in range(len(str)-3):
      if "co" == str[i:i+2] and "e" == str[i+3]:
        counter += 1
  return counter
  

#String-2 > end_other

def end_other(a, b):
  
  a = a.lower()
  b = b.lower()
  
  if a.endswith(b):
    return True
  if b.endswith(a):
    return True
  return False


#String-2 > xyz_there

def xyz_there(str):
  if len(str) >= 3 and "xyz" == str[0:3]:
    return True
  
  for i in range(1, len(str)):
    if "xyz" == str[i:i+3] and "." != str[i-1]:
      return True
  return False