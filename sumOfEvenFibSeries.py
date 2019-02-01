def main():
    first=0
    second=1
    third=first+second
    num=4000000
    sum=0
    print "The Fibonocci Series is:\n"
    print first ,second,
    while (third<=num):
        print third,
        if(third%2==0):
            sum+=third
            
        first=second
        second=third
        third=first+second    
    print "\nThe Sum of even numbers in the series is:",sum
    
if(__name__=="__main__"):
    main()
    