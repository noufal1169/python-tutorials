
#                                        -----
#                                        LISTS
#                                        -----


#list are ordered collection of elements enclosed within a bracket and seperated by comas
#list are mutable data types
#lists can be indexed and sliced
#lists are also a type of iterables in python
#we can store multiple kind of data types in lists

# 1 - create a list
'''
list = ['john',23,True,87.3]
print(list)
print(type(list))

lst = [] # empty list
print(lst)
lst = list()
print(lst)

a = 'python'
print(list(a))
'''
# 2 - list of list
'''
std_details = [['ram',90],['sam',89],['john',56],'abc public school']
print(std_details)
'''
# 3 - mutability
'''
a = ['john',23,True,87.3,'java']
print(a)
print(a[0])
a[0] = 'ram'
print(a)
'''
# 4 - indexing and slicing and straiding
'''
a = ['python','java','c','html','c++']
print(a[0])
print(a[-1]) #indexing

print(a[0:-2]) #slicing

print(a[0:4:2]) #straiding

print(type(a[0:4:2]))
print(type((a[0])))

print(a[ : : -1]) #reverse the list
'''
#activity
'''
a = ['python','java','c','html','c++']
print(a[2: :-1])
'''

# 5 - Slicing list inside the list
'''
lst1 = ['Python','Java','ML','IoT','Data Science']
print(lst1)
print(len(lst1))
lst1 = ['Python',['Java','ML'],'IoT','Data Science']
print(len(lst1))

print(lst1[0])
print(lst1[1])
print(lst1[1][0])
print(lst1[0],lst1[1][0])

lst1 = ['Python',['Java',['ML','C++'],'C'],'IoT','Data Science']
print(lst1[1][1][0])
'''

# LIST METHODS

#print(dir(list))

# 6 - Append (adds one argument at the end of the list)
'''
lst1 = ['Arun','Swati','Ram','John']
print(lst1)
lst1.append('Joe')
print(lst1)
lst1.append(['Joe','John']) #list is considered as one argument
'''

# 7 - Extend (extend the list with another list as arguments individualy)
'''
lst1 = ['Arun','Swati','Ram','John']
lst1.extend(['Joe','John'])
print(lst1)
lst1.extend('Joe','John') # takes only one argument
print(lst1)
'''

# 8 - Insert (insert a argument before the given index)
'''
lst1 = ['Arun','Swati','Ram','John']
lst1.insert(1,'Joe')
print(lst1)

lst1.insert(1,['Joe','Jose'])
print(lst1)

lst1.insert(1,'Joe','Jose') #only one element is inserted
print(lst1)
'''

# 9 - Clear (clears the entire list)
'''            
lst1 = ['Arun','Swati','Ram','John']
lst1.clear()
print(lst1)
'''

# 10 - Remove (removes one argument from the list )
'''
lst1 = ['Arun','Swati','Ram','John','Swati']
lst1.remove('Swati')
print(lst1) #remove the first occurance
help(list.remove)
'''

# 11 - Count (count a specific argument of the list)
'''
help(list.count)
lst1 = ['Arun','Swati','Ram','John','Swati']
print(lst1.count('Swati'))

'''

# 12 - Index (gives the index of the argument)
'''
help(list.index)
lst1 = ['Arun','Swati','Ram','John','Swati']
print(lst1.index('Swati'))
print(lst1.index('Swati',2))
print(lst1.index('Swati',2,4))
'''

# 13 - Pop (removes using index and also returns it)
'''
help(list.pop)
lst1 = ['Arun','Swati','Ram','John','Swati']
print(lst1.pop()) #if index is not given, it removes the last argument
print(lst1)
print(lst1.pop(0))
print(lst1)
'''


# 14 - Copy
'''
help(list.copy)
lst1 = ['Arun','Swati','Ram','John','Swati']
b = lst1
b.append('Joe')
print(lst1)
print(b)

lst1 = ['Arun','Swati','Ram','John','Swati']
b = lst1.copy() # makes a copy in new id without affecting the original
b.append('Joe')
print(lst1)
print(b)
'''

# 15 - Reverse (reverse the original list permenantly)
'''
lst1 = ['Arun','Swati','Ram','John','Swati']
print(lst1)
print(lst1[ : :-1])

lst1 = ['Arun','Swati','Ram','John','Swati']
print(lst1)
lst1.reverse()
print(lst1)
'''

# 16 - Sort
'''
a = [1,235,3,1,5,15,56,1]
a.sort()
print(a)
a.sort(reverse=True)
print(a)

a = ['s','g','h','ge']
a.sort()
print(a)

a = [1,235,3,1,5,15,56,1,True,False]
a.sort()
print(a) # True stands for 1 and False for 0

a = ['s','g','h','ge',True]
a.sort()
print(a) #boolean alpha cannot be sorted
'''

# 17 - case sensitive sort

'''
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)
'''

# 18 - case insensitive sorting
'''
help(list.sort)
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)
'''

# 19 - Del
'''
a = ['s','g','h','ge',True]

del a[0]
print(a)

del a
print(a) # error becz there is no more a 
'''

# 20 - Concatination
'''
a = ['a','b','c','d']
b = [1,2,3,4]
print(a+b)

lst1 = ["python"]
print(lst1*3)
'''

# change case of only first and last letters
'''
a = "pyThoN"
print(a[0].upper()+a[1:-1]+a[-1].lower())
print(f'{a[0].upper()}{a[1:-1]}{a[-1].lower()}')
'''

# 21 - print the   elements of the list
'''
a = [1, 2, 3, 4, 5]
print(a)
print(*a)
print(*a,sep= ",")
print(*a,sep= "\n")

print("-".join(str(a)))
'''

# 22 - Unpacking the list (same in tuple) (only keys in dict)(cant know which will assign)

'''
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
'''

##########
'''
lst1=['M','na','i','Ke']

lst2=['y','me','s','lly']

print(zip(lst1,lst2))
print(list(zip(lst1,lst2)))

a = list(zip(lst1,lst2))
for i,j in a:
    print(i+j,end=' ')
'''


















