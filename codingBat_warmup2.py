
st='abcd'
new=''
for each in range(len(st)+1):
    new+=st[:each]
print (new)
################
str='xaxxaxaxx'
def last2(str):
    word=str[(len(str)-2):len(str)]
    count=0
    for i in range(len(str)):
        if str[i:(i+2)] == word:
            count+=1
    return count-1

##############

re=[1,1,1,1,2,3,4,5]
se=[1,2,3]
check=0
for i in range(0,len(re)):
    if  re[i:i+3]== [1,2,3]:
        check+=1
if check==0:
    print ("False")
else:
    print ("True")
    
###############
"""   
p=len(a)
q=len(b)
count=0
for i in range(max(p,q)-1):
    if a[i:i+2]==b[i:i+2]:
        count+=1
return count"""
##############
def hello_name(name):
    return 'Hello ' +name+'!'

def make_abba(a,b):
    return a+b+b+a
   
def make_tags(tag,word):
    return '<'+tag+'>'+word+'</'+tag+'>'

def make_out_word(out,word):
    if len(out)==4:
        front=out[:2]
        back=out[2:]
    return front+word+back

def extra_end(str):
    return str[(len(str)-2):]*3

def first_two(str):
  if len(str)>=2:
    return str[:2]
  else:
    return str

def first_half(str):
    l=len(str)
    if l%2==0:
        return str[:int(l/2)]
    else:
        print ("The length is not even")
        
def without_end(str):
    return str[1: (len(str)-1)]

def combo_string(a,b):
    if (len(a)>len(b)):
        long=a
        short=b
    else:
        long=b
        short=a
    return short+long+short

def non_start(a,b):
    return a[1:]+b[1:]

def left2(str):
    first2=str[0:2]
    last=str[2:]
    return last+first2