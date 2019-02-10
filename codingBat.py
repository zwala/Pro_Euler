
"""
#WarmUp-1
def sleep_in(weekday, vacation):
  if (weekday==False or vacation==True):
    return True
  else:
    return False
print(sleep_in(False, False)) #→ True
print(sleep_in(True, False)) #→ False
print(sleep_in(False, True) )#→ True
########
def monkey_trouble(a_smile, b_smile):
  if a_smile and b_smile:
    return True
  if a_smile or b_smile:
    return False
  else:
    return True
print (monkey_trouble(True,True))
print (monkey_trouble(False,False))
print (monkey_trouble(True,False))
########
def sum_double(a, b):
  if(a==b):
    return (2*(a+b))
  else:
    return (a+b)
#########

def diff21(n):
  if (n>21):
    return (2*(n-21))
  else:
    return abs(21-n)
    
##########

def parrot_trouble(talking, hour):
  if talking==True and (hour<7 or hour>20):
      return True
  else:
      return False

print (parrot_trouble(True,6))
print (parrot_trouble(True,7))
print (parrot_trouble(False,6))
############
def makes10(a, b):
  if (a==10 or b==10 or (a+b)==10):
    return True
  else:
    return False


def near_hundred(n):
    if 90<=n<=110:
        return True
    elif 190<=n<=210:
        return True
    else:
        return False
print (near_hundred(93))
print (near_hundred(90))
print (near_hundred(89))

#########
def pos_neg(a, b, negative):
  if (negative== True):
    if(a<0 and b<0):
      return True
    else:
      return False
  else:
    if(a<0 and b<0):
      return False
    elif(a<0 or b<0):
      return True
    else:
      return False
############

str='not candy'
def not_string(str):
    if 'not' in str[0:3]:
        return str
    else:
        return 'not '+str
print(not_string(str))
############

def missing_char(str, n):
  new_str=''
  for each in range(0,len(str)):
    if(each!=n):
        new_str+=str[each]
  return new_str

############


def front_back(str):
  if (len(str)<=1):
    return str
  elif len(str)==2 or len(str)==3:
    return str[::-1]
  else:
    front=str[0]
    mid=str[1:(len(str)-1)]
    back=str[len(str)-1]
    newStr=back+mid+front
    return newStr   
print (front_back('code'))
print (front_back('ab'))
"""
############

def front3(str):
  if len(str)>=3:
    return str[0:3]*3
  else:
    return str*3
print (front3('Java'))
print (front3('abc'))
print (front3('ca'))
