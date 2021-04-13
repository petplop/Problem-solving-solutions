#Logic-2 > make_bricks

def make_bricks(small, big, goal):
  # Think about ways to fail
  
  #Fail #1
  if (goal > big*5+small):
    return False
  
  # If they amount of inches the bricks can make aren't
  # larger or = goal, then there's no way for it to cover
  # the length.
  
  #Fail #2
  # If there aren't enough small bricks to finish up the last bit
  # you would exceed the goal brick length.
  if (goal % 5 > small):
    return False
  
  return True
  

#Logic-2 > lone_sum

def lone_sum(a, b, c):
  
  sum = 0
  if a != b and a != c:
    sum+=a
  if b != a and b != c:
    sum+=b
  if c !=a and c != b:
    sum+=c
  return sum
  
  
#  if (a == c) and (a == b):
#     return 0
#   elif a == b:
#     return c
#   elif a == c:
#     return b
#   elif c == b:
#     return a
#   else:
#     return a+b+c
    
  
#Logic-2 > lucky_sum


def lucky_sum(a, b, c):
  sum = 0
  if a == 13:
    return sum
  sum+=a
  if b == 13:
    return sum
  sum+=b
  if c == 13:
    return sum
  sum+=c
  return sum


#Logic-2 > no_teen_sum


def no_teen_sum(a, b, c):
  return fix_teen(a) + fix_teen(b) + fix_teen(c)
  
def fix_teen(n):
  if n == 13 or n == 14 or n == 17 or n == 18 or n == 19:
    return 0
  else:
    return n


#Logic-2 > round_sum

def round10(num):
  if num % 10 >= 5:
    return num + 10 - num % 10
  else:
    return num - num % 10


def round_sum(a, b, c):
  return round10(a) + round10(c) + round10(b)
  

#Logic-2 > close_far

def close_far(a, b, c):
  cond1 = abs(a-b) <= 1 and abs(b-c) >= 2 and abs(a-c) >= 2
  cond2 = abs(a-c) <= 1 and abs(a-b) >= 2 and abs(c-b) >= 2
  if cond1 == True or cond2 == True:
    return True
  return False


#Logic-2 > make_chocolate

def make_chocolate(small, big, goal):
  
  smallNeeded = goal - big*5
  if (goal > big*5+small):
    return -1
  if (smallNeeded <= small and smallNeeded >= 0):
    return smallNeeded
  if (smallNeeded < 0 and goal % 5 <= small):
    return goal % 5
  return -1