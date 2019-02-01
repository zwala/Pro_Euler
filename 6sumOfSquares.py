#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
#Sum of squares of 1 to 100
sumOfSquares=0
sumOfNumbers=0
for each in range(1,101):
    sumOfSquares+=each**2
    sumOfNumbers+=each
sumOfNumbers=sumOfNumbers**2
print sumOfSquares
print sumOfNumbers
diff=sumOfSquares-sumOfNumbers
print abs(diff)

