def cigar_party(cigars, is_weekend):
  if is_weekend:#Weekend=True
    if (cigars>=40):
      return True
    else:
      return False
  else:#Weekend=False
    if (40<=cigars<=60):
      return True
    else:
      return False
  
def date_fashion(you,date):
    if you<=2 or date<=2:
        return 0
    else:
        if you>=8 or date>=8:
            return 2
        else:
            return 1
        
def squirrel_play(temp,is_summer):
    if is_summer:
        if(60<=temp<=100):
            return True
        else:
            return False
    else:
        if(60<=temp<=90):
            return True
        else:
            return False
        
def caught_speeing(speed,is_birthday):
    def check_speed(speed):
        if speed<=60:
            return 0
        elif 61<=speed<=80:
            return 1
        else:
            return 2
    if is_birthday:
        return check_speed(speed-5)
    else:
        return check_speed(speed)
    
def sorta_sum(a,b):
    s=a+b
    if 10<=s<=19:
        return 20
    else:
        return s

def alarm_clock(day,vacation):
    early="7:00"
    late="10:00"
    off="off"
    if vacation:
        if 1<=day<=5:
            return late
        else:
            return off
    else:
        if 1<=day<=5:
            return early
        else:
            return late

def love6(a,b):
    if a==6 or b==6 or a+b==6 or abs(a-b)==6:
        return True
    else:
        return False
    
def in1to10(n, outside_mode):
    if not (outside_mode):
        if 1<=n<=10:
            return True
        else:
            return False
    else:
        if n>=10 or n<=1:
            return True
        else:
            return False

def near_ten(num):
    r=num%10
    if r in [8,9,0,1,2]:
        return True
    else:
        return False
        













