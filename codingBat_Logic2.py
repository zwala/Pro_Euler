def make_brick(small,big,goal):
    if goal<=small+5*big:
        if goal%(5) <=small:
            return True
        else:
            return False
    else:
        return False
    
def lone_sum(a,b,c):
    sum=0
    if a in (b,c):
        sum+=0
    else:
        sum+=a
    if b in (a,c):
        sum+=0
    else:
        sum+=b
    if c in (a,b):
        sum+=0
    else:
        sum+=c
    return sum

def lucky_sum(a,b,c):
    sum=0
    if a!=13:
        sum+=a
    else:
        return sum
    if b!=13:
        sum+=b
    else:
        return sum
    if c!=13:
        sum+=c
    else:
        return sum
    return sum

def fix_teen(n):
    if n in (13,14,17,18,19):
        return 0
    else:
        return n
def no_teen_sum(a,b,c):
    a=fix_teen(a)
    b=fix_teen(b)
    c=fix_teen(c)
    return a+b+c

def round10(num):
    if num%10<5:
        num=(num//10)*10
    else:
        num=((num//10)+1)*10
    return num
def round_sum(a,b,c):
    a=round10(a)
    b=round10(b)
    c=round10(c)
    return a+b+c
    
def close_far(a,b,c):
    while not (abs(a-b)<=1 and abs(a-c)<=1):
        if abs(a-b)<=1:
            if abs(a-c)>=2 and abs(b-c)>=2:
                return True
            else:
                return False
        else:
            if abs(a-b)>=2 and abs(b-c)>=2:
                return True
            else:
                return False
    else:
        return False


def make_chocolate(small,big,goal):   
    consider_big=big
    while consider_big*5 >goal:
        consider_big-=1
    num=goal-(consider_big*5)
    if num<=small:
        return num
    else:
        return -1



















