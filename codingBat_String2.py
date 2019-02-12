def double_char(str):
    new=''
    for each in str:
        new+=each*2
    return new

def count_hi(str):
    count=0
    for i in range(len(str)):
        if str[i:i+2]=='hi':
            count+=1
    return count

def cat_dog(str):
    cat_count=str.count('cat')
    dog_count=str.count('dog')
    if cat_count==dog_count:
        return True
    else:
        return False
    
def count_code(str):
    count_co=0
    for each in range(len(str)-3):
        if str[each:each+2]=='co' and str[each+3]=='e':
            count_co+=1
    return count_co

def end_other(a,b):
    small=min(len(a),len(b))
    a=a.lower()
    b=b.lower()
    diff=abs(len(a)-len(b))
    if small == len(a):       
        if (a in b) and b[diff:]==a :
            return True
        else:
            return False
    else:
        if b in a and a[diff:]==b:
            return True
        else:
            return False
        
def xyz_there(str):
    count=0
    if ('xyz' in str):
        for i in range(len(str)):
            if str[i:i+3]=='xyz' and str[(i-1)]!='.':
                count+=1
        if count>0:
            return True
        else:
            return False
    else:
        return False