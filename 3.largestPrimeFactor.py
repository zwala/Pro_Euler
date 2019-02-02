"""The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?"""

def get_factors(num):
    prime_list=[]
    d=2
    while num>1:
        while num%d==0:
            prime_list.append(d)
            num=num/d
        d=d+1
    return prime_list


gen_list=get_factors(600851475143)
max_factor=max(gen_list)
print max_factor