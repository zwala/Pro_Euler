"""By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?"""

#primelist
#find the nth prime number in the list

prime_list=[]
gen_list=range(1,11)
for each in gen_list:
    for i in (2,each):
        if each%i==0:
            break
    else:
        prime_list.append(each)

print prime_list
        
