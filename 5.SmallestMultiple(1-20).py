"""2520 is the smallest number that can be divided by each of the numbers 
from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the 
numbers from 1 to 20?"""

#list=[11,13,14(7*2),16(4*4)(8*2),17,18(9*2)(3*3),19,20(5*4)]
for num in range(20,999999999,20):
    if all(num%n==0 for n in range(2,20)):
        print num
        break
        
