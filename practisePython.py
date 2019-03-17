def exc_1():
    name=input("Give me your name: ")
    age=int(input("..and your age?!: "))
    year=100-age
    future=2019+year
    print ("Hi "+name+"! \n Do you know your are going to turn 100 on:"+str(future))
    
def exc_2():
    print ("The folloring has 2 segments:")
    print ("SEGMENT 1:")
    number=int(input("Please enter a number: "))
    if number%4==0:
        print ("Hey!! Its a multiple of 4!!")
    else:
        print ("Boo!! Its not a multiple of 4.")
    
    print ("SEGMENT 2:")
    num=int(input("Enter a number: "))
    check=int(input("Enter a divisor to check: "))
    if num%check==0:
        print ("Its a divisor!!")
    else:
        print ("Its not a divisor!!")
        
def exc_7():
    a=[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    new=[]
    for each in a:
        if each%2==0:
            new.append(each)
    print (new)