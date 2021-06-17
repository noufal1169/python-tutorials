
#                                   ------
#                                   STRING
#                                   ------


# 1 - STRING OPERATIONS
print('\n')
print('STRING'.center(50))
# 1.1 - String indexing
'''
print('\n 1.1 STRING INDEXING \n')
name = "Codegnan"
print('1',name)
print('2',name[0])
print('3',name[-1])
print('4',len(name)) #length of the string
print('5',name[10]) #error gives when out of range
'''

# 1.2 - String Slicing
'''
print('\n 1.2 STRING SLICING \n')
name = "Noufal is a data analyst"
print('1',name[0:5])
print('2',name[0:6]) #name[start : end+1]
print('3',len(name[0:6]))
print('4',name[6:]) # leaving blank means to the extent
print('5',name[-1:-7]) #python only reads from left to right
print('6',name[-7: ])
print('7',name[ : 6]) 
print('8',name[7:-7]) # we can use negative and positive indexes
print('9',name[ : ]) # it gives the entire string
print('10',name[0:6] + " " + name[12: ]) # concatination of sliced string
print('11',name[7:500]) # range is not a problem in slicing
'''

# 1.3 - String Striding
'''
print('\n 1.3 STRING STRIDING \n')
a = "Manvendra is a data analyst"
print('1',a[0:9])
print('2',a[0:9:2]) #str[start : end+1 : step]
print('3',a[-12 : :3])

# python ---->nohtyp
b = "python"
print('4',b)
print('5',b[ : : 2])
print('6',b[ : : -1])

a = "Manvendra is a data analyst"
print('7',a)
print('8',a[0 : 8 : -1])
print('9',a[8 :  : -1]) # when reversing end first and start second, cause it reads from right to left

print('10',a[15:19])
print('11',a[18:14:-1])
print('12',a[18:14:-2])
print('13',a[18:14:-7])

print('14',a[20: ])
print('15',a[ 26 : 19 : -1])
'''

# 1.4 - Old Style String Formatting
'''
print('\n 1.4 OLD STYLE STRING FORMATTING \n')
lang = "python"
print("1 we are learning %s"%lang) # %s is a place holder

lang = 10.12
print("2 we are learning %.10f"%lang) #%.nf for number of decimanls needed,"n" is the number of decimals

fname = "john"
lname = "smith"
print('3',fname,lname)
print('4',fname+lname)
print('5',fname+" "+lname)

a = 10
b = 20
c  = a + b
print("6 The addition of %s and %s is %s" %(a,b,c)
'''

# 1.5 - New Style String Formatting
'''
print('\n 1.5 NEW STYLE STRING FORMATTING \n')
fname = "john"
lname = "smith"
print("1 {} {}".format(fname,lname))

a = 10
b = 20
c  = a + b
print("2 The addition of ", a, "and",b,"is",c)
print("3 The addition of {} and {} is {}".format(a,b,c))
print("4 The addition of {1} and {2} is {0}".format(c,a,b))
print(f"5 the addition of {a} and {b} is {a+b}")

print('6',"python" * 3)
'''


# 2 - String Functions

# 2.1 - concatination
'''
print('\n 2.1 CONCATINATION \n')
a = "hello"
b = "world"
print('1',a + b)
print('2',a +" "+b)
print('3',a*3)
'''
# 2.2 - ASCII TABLE
'''
print('\n 2.2 ASCII TABLE \n')
print('1',ord("a")) #numeric equivalent can be found only for one character
print('2',chr(97))  #charater equivalent (case sensitive)
'''
# 3 - String Methods
'''
help(str) 
print(dir(str))
'''
# 3.1 - to change the string int upper case
'''
print('\n 3.1 UPPER CASE \n')
a = "Python"
print('1',a.upper())
help(str.upper)
'''
# 3.2 - to change string into lower case
'''
print('\n 3.2 LOWER CASE \n')
str1 = "DATA ANALYTICS"
print(str1.lower())
'''
# 3.3 - to check the count of specific part in the string
string1 = "twinkle little twinkle star"

'''
print('\n 3.3 COUNT \n')
print('1',string1)
print('2',string1.count("twinkle"))
print('3',string1.count("t"))
print('4',string1.count("t",3)) #start index for counting section
print('5',string1.count("t",8,16))  # start and end index for counting section
'''
# 3.4 - to replace  specific part in the string
'''
print('\n 3.4 REPLACE \n')
print('1',string1)
print('2',string1.replace("star","moon"))
'''
# 3.5 - to find the start index of the specific part
'''
print('\n 3.5 FIND AND INDEX \n')
print('1',string1)
print('2',string1.find("twinkle"))
print('3',string1.find("twinkle",8,50))
print('4',string1.find("bond")) # -1 means the part doesn't present
print('5',string1.rfind("twinkle")) #rfind gives first occurance from the right side
print('6',string1.index("twinkle")) #index can be used for find, but it gives error incase the substring is not present
'''
# 3.6 - capitalize the first letter of the string
'''
print('\n 3.6 CAPITALIZE  \n')
str1 = "data analytics"
print('1',str1)
print('2',str1.capitalize())
'''
# 3.7 - make the string as title (all first letter of the words will be capitalized)
'''
print('\n 3.7 TITLE \n')
str1 = "the data analytics"
print(str1)
print(str1.title())
'''
# 3.8 - casefold (generally change the string into lower case and helps in logically comparing the strings)
'''
print('\n 3.8 CASEFOLD \n')
str1 = "DATA"
print(str1)
print(str1.casefold)
str2 = "data"
print(str1.casefold() == str2.casefold())
'''
# 3.9 - checking the string
'''
print('\n 3.9 VARIOUS IS CHECKING \n')
str1 = "Hello11"
print('1',str1)
print('2',str1.islower()) #if it is in lower case
print('3',str1.isupper()) #if it is in upper case
print('4',str1.istitle()) #if it is a title
print('5',str1.isascii()) #if is has ascii value
print('6',str1.isspace()) #if only white space
print('7',str1.isdigit()) #if it has only number
print('8',str1.isalpha()) #if only has alphabets, even white space is rejected
print('9',str1.isalnum()) #if it has alphabets and number, white space is rejected
'''

# 3.10 - rjust & ljust & center justified
'''
print('\n 3.10 RJUST LJUST CENTER \n')
a = "python"
print('1',a)
print('2',a.rjust(10))
print('3',a.ljust(10))
print('4',a.center(10))
print("\n")
print('5',a.rjust(10,"a"))
print('6',a.ljust(10,"-"))
print('7',a.center(10,"_"))
'''
# 3.11 - swapcase
'''.
print('\n 3.11 SWAPCASE \n')
a = "Python"
print(a)
print(a.swapcase())
'''
# 3.12 - split
'''
print('\n 3.12 SPLIT \n')
str1 = "python,c,c++,javascript,html,go,scala,java"
print('1',str1)
print('2',str1.split())
print('3',str1.split(','))

str1 = 'python-c-c++-react'
print('4',str1.split())
print('5',str1.split('-'))
print('6',str1.split('c'))

str1 = 'twinkle twinkle little star'
print('7',str1)
print('8',str1.split())
'''

# 3.13 - partition (split in three parts)
'''
print('\n 3.13 PARTITION \n')
str1 = 'twinkle twinkle little star'
print(str1)
print(str1.partition("twinkle"))
str1 = "python,c,c++,javascript,html,go,scala,java"
print(str1)
print(str1.partition("c++"))
'''
# 3.14 - splitlines

print('\n 3.14 SPLITLINES \n')
str1 = 'twinkle twinkle little star'
print('1',str1.splitlines())
s1 = '''fgxfdf
jtff
fgfy'''
print('2',s1.splitlines())

# 3.15 - join
'''
print('\n 3.15 JOIN \n')
a = ('python','c','c++','react')

print(a)
print(' '.join(a))
print('-'.join(a))
'''

# 3.16 - strip (remove the white space and charac from the left and right)
'''
print('\n 3.16 STRIP \n')
a = '   Pyt hon---   '
print('1',a)
print('2',a.strip())
print('3',a.lstrip())
print('4',a.rstrip())
a = '   Pyt hon---'
print('5',a)
print('6',a.strip('-'))
a = 'p ython'
print('7',a)
print('8',a.strip('p'))
a = 'python'
print('9',a)
print('10',a.strip('py'))
'''

# 3.17 - startswith and endswith
'''
print('\n 3.17 STARTSWITH AND ENDSWITH \n')
str1 = 'python is easy'
print('1',str1)
print('2',str1.startswith('java'))
print('3',str1.startswith('python'))
print('4',str1.endswith('easy'))
print('5',str1.endswith('easy',3,9)) # start and end index for checking
print('6',str1.endswith('hard'))
'''

# 3.18 - expand the tab size of the string
'''
print('\n 3.18 EXPAND TAB \n')
print('01\t012\t0123\t01234'.expandtabs()) # default is 8

print('01\t012\t0123\t01234'.expandtabs(4))

'''

# 3.19 - replace with count.
'''
print('\n 3.19 REPLACE WITH COUNT \n')
a = 'noufal fahar noufal raheem sulaiman'
print(a)
print(a.replace('noufal','noufi',1))
'''


# 3.20 - Isidentifier
'''
print('\n 3.20 ISIDENTIFIER \n')
a = 'noufal'
print(a)
print(a.isidentifier())

a = "print()"
print(a)
print(a.isidentifier())
'''

# 3.21 - Encode
'''
print('\n 3.21 ENCODE \n')
txt = "My name is Ståle"

x = txt.encode()            #If no encoding is specified, UTF-8 will be used.

print(x)


txt = "My name is Ståle"

print(txt.encode(encoding="ascii",errors="backslashreplace")) #uses a backslash instead of the character that could not be encoded
print(txt.encode(encoding="ascii",errors="ignore")) #ignores the characters that cannot be encoded
print(txt.encode(encoding="ascii",errors="namereplace"))    #replaces the character with a text explaining the character
print(txt.encode(encoding="ascii",errors="replace"))#replaces the character with a questionmark
print(txt.encode(encoding="ascii",errors="xmlcharrefreplace")) #replaces the character with an xml character
'''


# 3.22 - unpacking
'''
print('\n 3.22 UNPACKING \n')
x = "python"

a,*b = x
print(x)
print(a)
print(b)
'''











