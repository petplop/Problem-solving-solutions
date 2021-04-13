#Warmup-1 > sleep_in

def sleep_in(weekday, vacation):
  if weekday == True and vacation == False:
    return False
  else:
    return True
    
# a better solution for cornered tests
def sleep_in(weekday, vacation):
  if (weekday == False and vacation == False) or (weekday == False and vacation == True) or (weekday == True and vacation == True):
    return True
  else:
    return False


#Warmup-1 > monkey_trouble

def monkey_trouble(a_smile, b_smile):
  if a_smile == b_smile:
    return True
  else:
    return False


#Warmup-1 > sum_double

def sum_double(a, b):
  if a == b:
    return (a+b)*2
  else:
    return a+b


#Warmup-1 > diff21

def diff21(n):
  if n > 21:
    return abs(n-21)*2
  else:
    return abs(n-21)


#Warmup-1 > parrot_trouble

def parrot_trouble(talking, hour):
  if talking and (hour < 7 or hour > 20):
    return True
  else:
    return False


#Warmup-1 > makes10

def makes10(a, b):
  if (a == 10 or b == 10) or (a+b == 10):
    return True
  else:
    return False


#Warmup-1 > near_hundred

def near_hundred(n):
  if n in range(90, 111) or n in range(190, 211):
    return True
  else:
    return False


#Warmup-1 > pos_neg

def pos_neg(a, b, negative):
  if negative:
    if a > 0 or b > 0:
      return False
    else:
      return True
      
  elif (a < 0 and b > 0) or (a > 0 and b < 0):
    return True
  
  else:
    return False
    
    
#Warmup-1 > not_string

def not_string(str):
  if not "not" in str[:3]:
    return "not " + str

  else:
    return str
    
    
#Warmup-1 > missing_char

def missing_char(str, n):
  new_str= ""
  
  for letter in str:
    if letter == str[n]:
      pass
  
    else:
      new_str += letter
  
  return new_str


#Warmup-1 > front_back

def front_back(str):
  if len(str) <= 1:
    return str
    
  else:
    return str[-1] + str[1:-1] + str[0]


#Warmup-1 > front3

def front3(str):
  front_end = 3
  if len(str) < front_end:
    front_end = len(str)
  front = str[:front_end]
  return front + front + front
