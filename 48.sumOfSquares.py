"""The series, 11 + 22 + 33 + ... + 1010 = 10405071317.

Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.
"""
sum=0
for each in range(1,1001):
    sum=sum+(each**each)

sum=str(sum)
sum=sum[::-1]
sum=sum[0:10]
sum=sum[::-1]
print sum
