"""
4: Largest Palindrome number that can be formed out of a product of two  3 digit numbers
"""
a=range(100,1000)
b=range(100,1000)
make_list=[]
for p in a:
    for q in b:
        c=p*q
        if str(c)==(str(c))[::-1]:
          make_list.append(c)

print max(make_list)
