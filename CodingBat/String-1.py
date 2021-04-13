#String-1 > hello_name

def hello_name(name):
  return "Hello " + name + "!"


#String-1 > make_abba

def make_abba(a, b):
  return a+b+b+a


#String-1 > make_tags

def make_tags(tag, word):
  
  return "<"+tag+">"+word+"</"+tag+">"


#String-1 > make_out_word

def make_out_word(out, word):
  
  half_str = len(out) // 2
  
  return out[:half_str] + word + out[half_str:]


#String-1 > extra_end

def extra_end(str):
  return str[-2:] * 3


#String-1 > first_two

def first_two(str):

  if str < 0:
    return str
  
  else:
    return str[:2]


#String-1 > first_half

def first_half(str):
  
  half_str = len(str) / 2 # Can you // too cus even length
  

  return str[:half_str]
  
  
#String-1 > without_end

def without_end(str):
  
  return str[1:-1]


#String-1 > combo_string

def combo_string(a, b):
  
  if len(b) < len(a):
    return b + a + b
  else:
    return a + b + a


#String-1 > non_start

def non_start(a, b):
  
  a_a = a[1:]
  b_b = b[1:]
  
  return a_a+b_b


#String-1 > left2

def left2(str):
  
  first_2 = str[:2]
  mid = str[2:]
  
  return str[2:] + str[:2]