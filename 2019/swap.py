a=5
b=6

# temp = a
# a=b
# b = temp
#
# print(a)
# print(b)


##In Python there is a way of doing this without using temp variable

# a = a + b
# b = a - b
# a = a - b
#
# print(a)
# print(b)


## there is one more way using bitwise XOR operator

# a = a ^ b
# b = a ^ b
# a = a ^ b
# 
# print(a)
# print(b)


## or simply swap:

a,b = b,a
print(a)
print(b)

