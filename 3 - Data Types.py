#                               ----------
#                               DATA TYPES
#                               ----------
'''
text type - str
numeric types - int , float , complex
mapping type - dictionary
boolean type - bool
set types - set, frozenset
binary types - bytes,bytearray,memoryview
sequence types - list,tuple,range
'''

# 1 - numeric types
'''
integer is the whole number
float is the number with decimal 
complex number has real and imaginary numbers(only j or J)
'''
#
'''
a = 10
b = 10.2
c = 3+4j # 3 is the real part and 4j is the imaginary part 
print(type(a))
print(type(b))
print(type(c))
print(c.real)
print(c.imag)
'''

# 1.1 - Type Casting

#changing the type

# CONVERSION OF INTEGER
'''
print(' CONVERTION OF INTERGER TO OTHER TYPES')
a = 10
print('\n integer value = ',a)
print(type(a))

#int to float

print('\n int to float')
b = float(a)
print(b)
print(type(b))

#int to complex

print('\n int to complex')
c = complex(a)
print(c)
print(type(c))

#int to binary

print('\n int to binary')
print(bin(a)) #0b in the output is the notation for binary number

b =0b1010
print(b) #python store binary as integer
print(type(b))

#int to octagonal and hexagonal form

print('\n int to oct and hex')
print(oct(a)) #0o stands for octagonal notation
print(hex(a)) #0x stands for hexagonal notation

#int to str

print('\n INTEGER TO STRING')
x = 10
print('\n',x)
print(type(x))
y = str (x)
print(y)
print(type(y))

#int to bool

print('\n INTEGER TO BOOL')
x = 10
print('\n',x)
print(bool(x))

x = -10
print('\n',x)
print(bool(x))

x = 0
print('\n',x)
print(bool(x))
'''
# CONVERTION OF FLOAT
'''
print('\n CONVERTION OF FLOAT TO ANOTHER TYPES')
b = 10.99
print('\n float value = ',b)
print(type(b))

#float to int

print('\n float to int')
print(int(b))

#float to complex

print('\n float to complex')
print(complex(b))

#float to binary,oct,hex

print('\n float to binary,oct,hex(not possible)')
#print(bin(b))
# not possible.. only integer can be converted into binary,octa and hexa


#float to str
print('\n FLOAT TO STRING')
x = 10.22 
print('\n',x)
print(type(x))
y = str (x)
print('\n',y)
print(type(y))

#float to bool
print('\n FLOAT TO BOOL')
x = 10.22
y = 0.0
print('\n',x)
print(type(x))
print(bool(x))
print('\n',y)
print(bool(y))
'''
# CONVERSION OF COMPLEX
'''
print('\n CONVERSION OF COMPLEX TO ANOTHER TYPES')
c = 3+4j
print('\n complex value = ',c)
print(type(c))

#complex to int,float

print('\n cannot convert to other types')
print(int(c)) # not possible.. complex can be converted into intger or float
print(float(c))

#complex to bool

print('\n COMPLEX TO BOOL')
a = 3+4j
print('\n',a)
print(bool(a))
a = 0+0j
print('\n',a)
print(bool(a))
a = 0+4j
print('\n',a)
print(bool(a))
'''
# 2 - String

name1 = "noufal"
name2 = 'fajar'

name3 = '''vishnu'''
'''
print(name1)
print(type(name1))
print(name2)
print(type(name2))
print(name3)
print(type(name3))
c = "hkjh","uhhi"
print(c)
print(type(c))
c = "hkjh""uhhi"
print(c)
'''
# str to int and float
'''
print('string can be converted into int or float if only it is number')
a = '10'
print('\n',type(a))
b = int(a)
print(b)
print(type(b)) 
print(float(a))
'''

# string to bool
'''
print('\n STRING TO BOOL')
a = 'gsdgf'
b = ''
print(a)
print(bool(a))
print(b)
print(bool(b))
print('\n empty string gives False else True')
'''


# 3 - Boolean
'''
print('\nBOOLEAN')
a = True
print('\n',a)
print(type(a))

b = False
print('\n',b)
print(type(b))
'''

#bool to str
'''
print('\nBOOL TO STRING')
a = True
print('\n',a)
print(type(a))

b = str(a)
print(b)
print(type(b))
'''
#bool to int
'''
print('\n BOOL TO INTEGER')
a = True
print('\n',a)
print(int(a))
b = False
print('\n',b)
print(int(b))
'''
#bool to float
'''
print('\n BOOL TO FLOAT')
a = True
print('\n',a)
print(float(a))
b = False
print('\n',b)
print(float(b))
'''

#bool to complex
'''
print('\n BOOL TO COMPLEX')
a = True
print('\n',a)
print(complex(a))
a = False
print('\n',a)
print(complex(a))
'''
#bool to bin
'''
print('\n BOOL TO BIN')
a = True
print('\n',a)
print(bin(a))
a = False
print('\n',a)
print(bin(a))
'''
#bool to oct
'''
print('\n BOOL TO OCT')
a = True
print('\n',a)
print(oct(a))
a = False
print('\n',a)
print(oct(a))
'''
#bool to hex
'''
print('\n BOOL TO HEX')
a = True
print('\n',a)
print(hex(a))
a = False
print('\n',a)
print(hex(a))
'''






