#Logic-1 > cigar_party

def cigar_party(cigars, is_weekend):
  if is_weekend and cigars >= 40:
    return True
  else:
    if cigars in range(40, 61):
      return True
    return False


#Logic-1 > date_fashion

def date_fashion(you, date):
  if you <= 2 or date <= 2:
    return 0
  elif you >= 8 or date >= 8:
    return 2
  else:
    return 1


#Logic-1 > squirrel_play

def squirrel_play(temp, is_summer):
  if is_summer and temp in range(60, 101):
      return True
  else:
    if not is_summer and temp in range(60, 91):
      return True
    return False


#Logic-1 > caught_speeding

def caught_speeding(speed, is_birthday):
  if is_birthday == True:
    if speed <= 65:
      return 0
    elif speed in range(65, 86):
      return 1
    else:
      return 2
  elif is_birthday == False:
    if speed <= 60:
      return 0
    elif speed in range(60,81):
      return 1
    else:
      return 2


#Logic-1 > sorta_sum

def sorta_sum(a, b):
  if a+b in range(10, 20):
    return 20
  else:
    return a+b


#Logic-1 > alarm_clock

def alarm_clock(day, vacation):
  if not vacation:
    if day in range(1,6):
      return "7:00"
    if day == 0 or day == 6:
      return "10:00"
  else:
    if day in range(1,6):
      return "10:00"
    if day == 0 or day == 6:
      return "off"


#Logic-1 > love6

def love6(a, b):
  if a == abs(6) or b == abs(6):
    return True
  
  elif (a-b == 6 or b-a == 6) or a+b == 6:
    return True
    
  else:
    return False


#Logic-1 > in1to10

def in1to10(n, outside_mode):
  if outside_mode == True:
    if n <= 1 or n >= 10:
      return True
    else:
      return False
  
  else:
    if n in range(1,11):
      return True
    return False
  

#Logic-1 > near_ten

def near_ten(num):
  if num%10 == 8 or num%10 == 9 or num%10==0 or num%10==1 or num%10 == 2:
    return True
  return False