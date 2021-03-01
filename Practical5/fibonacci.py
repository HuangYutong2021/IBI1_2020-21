# set the first number as a pointer too.
a = 1
# set the second number as the next pointer
b = 1                     
print(a)
print(b)
# cycle from 3 to 13 to caculate the following number.
for i in range(3,14):
# create a number to restore the sum of the first two numbers.
    c = a+b
# let the pointer move to the next
    a = b
# the latter pointer move to the next number as the sum of the first two 
    b = c                 
    print(c)

print (" the 13th number is " ,c)
