#                           ---------
#                           VARIABLES
#                           ---------

#num is a variable also called identifier

'''num = 10 #initialization
print(num)
print(type(num)) # to find the data type
print(id(10))''' #id tells the memory location

'''rules for naming variables'''
# variable name should not start with number or any special character other than underscore
# we cannot use python keywords as variable names
# special characters cannot be used in variable name
# only alpha numeric characters
# variable name is case sensitive
# white space is not allowed in variable name


'''import keyword
print(keyword.kwlist) '''# to find python keywords

# explanation of memory storage in python

'''
a = 10
b = 10
c = 11
print(id(a))
print(id(b))
print(id(c))
b += 2
print(id(b))
print(b)
'''
#                            ---------   
#                            OPERATORS
#                            ---------

# 1 - Arithmatic operators

# +, -, *, /, // (floor division), % (reminder), ** (exponential)

'''
a = 2
b = 3
print(a , b)
print("substraction ",a - b)
print("additon ",a + b)
print("multiplication ",a * b)
print("division ",a / b)
print("floor division ",a // b) # in floor division decimal part is not given
print("reminder ",a % b)
print("exponential ", a ** b)
'''

# 2 - Assignment operators

# =, =+, -=, *=, /=, //=, %=, **=

'''
a = 10 #assignment operator
print(a)

a += 2 # a = a+2
print(a)

a -= 2 # a = a-2
print(a)

a *= 2 # a = a*2
print(a)

a /= 2 # a = a/2
print(a)

a //= 2 # a = a//2
print(a)

a = 3
a %= 2 # a = a%2
print(a)

a = 3
a **= 2 # a = a**2
print(a)

a = 10
b = 20
c = 5
d = 7

result = ( ( a + b ) * c) + d
print(result)
'''

# 3 - Comparison operators

# >, <, <=, >=, == (equals to ), != (not equals to )

'''
a = int(input("enter the number = "))
b = int(input("enter the number = "))

# These are boolean operators
# Output is always True or False

print(a > b) 

print(a < b)

print(a >= b)

print(a <= b)

print(a == b)

print(a != b)
'''

# 4 - Logical operator

# and , not , or
'''
print((5 > 10) and (10 > 7)) # both condition should be true to get final output as true, othervise its false alwys

print((5 > 10) or (10 > 7)) # only one condition need be true to get final output as true, othervise its false alwys

x = True
print(not x)

print(not 5>10)
print(not 5<10)

y = False
print(not y)  # gives true when the statement is false and viseversa
'''

# 5 - bitwise operators ( operations on the bitwise values)


# & , | , ~  , ^ , << , >>

'''
a = 10
b = 15
print(bin(a))
print(bin(b))

print(a & b) # and

print(a | b) # or

print(~a) # not (-a-1)

print(a ^ b) # xor

print(a >> 2) # right shift (if x >> y , ie, x / 2^y)

print(a << 2) # left shift (if x << y , ie, x * 2^y)
'''

#ACTIVITY
'''
x = int(input("enter two numbers "))
y = int(input())

print("addition ", x + y)
print("substraction ", x - y)
print("multiplication ", x * y)
print("division", x / y)
print("floor division ", x // y)
print("exponential ",x ** y)
'''

# Multiple assignment
'''
a,b = 10,11
print(a)
print(b)

x = y =76
print(x,y)
'''

# 6 - Identity Operator

# is , is not
'''
a = 10
b = a
print(id(a))
print(id(b))
print(a is b)
print(a is not b)
b = 20
print(a is not b)
'''
# 7 - Membership Operator

# in , not in
'''
string1 = "edubridge"
print("edu" in string1)
print("Edu" not in string1)
'''
































