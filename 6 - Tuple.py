
#                                        ------
#                                        TUPLES
#                                        ------


# tuples are ordered collection of elements enclosed within a round bracket and separeated by commas.
# Tuples are immutable data types that means we cannot add, update , and delete the elements of the tuples
# Tuples can be indexed and sliced in similar ways as strings and lists
# Tuples are also type of iterables in python
# Tuples can also store multiple type of data

# Create
'''
a = tuple() #creating empty tuple
print(a)
print(type(a))

a = ('Ram',23,True,44.5)
print(a)
print(type(a))

a = ('Ram')
print(type(a)) # this is not a tuple

a = ()
print(type(a)) # this is a tuple
'''
# To know what all methods can be used on tuple
'''
print(dir(tuple))
'''


# TUPLE

'''
a = (1,'Pythion','Data Analytics')
print(type(a))

a = ('dgs')
print(type(a))

a = ('dgs',)
print(type(a))

a = ((1,'Pythion'),'Data Analytics',True)
print(a)

a = (1,2,3,4,('python','java','c','c++'))
print(a[4][1])
print(a[4][True]) # true - 1, false - 0
print(a[4][False])


a = (1,2,3,4,['python','java','c','c++'])
print(a[-1][0])
a[-1][0] = 'Go'
print(a)   # list inside the tuple can be modified
'''

# LIST <=> TUPLE <=> STRING
'''
#tuple to list
a = (1,'Pythion','Data Analytics')
print(list(a))

#list to tuple
a = [1,'Pythion','Data Analytics']
print(tuple(a))

#string to tuple and list
c = 'python'
print(tuple(c))
print(list(c))
'''
# modifing tuple
'''
a = (1,2,3,4,5,[10,12,13])
a[-1] = tuple(a[-1])
print(a) # cannot assign item
'''
