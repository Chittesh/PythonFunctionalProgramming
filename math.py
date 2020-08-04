import math
import decimal
#print(help(math))

print(math.fabs(4.5))           #Return the absolute value of the float x.
print(math.sin(90))
print(math.gcd(24,76))
print(math.pi)
print(math.e)
print(math.ceil(4.5))           #This is the smallest integer >= x.
print(math.ceil(-5.5))

#Decimal operations decimal.Decimal
# If we are using finical calculation
value1=decimal.Decimal('34.5')
value2=decimal.Decimal('21.3')
value3 = value1 - value2
print(value3)