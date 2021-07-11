
#                                 ----------
#                                 DICTIONARY
#                                 ----------


# Dictionaries are mutable unordered collections written with curly braces.
# Data is stored in key and value pair.
# The keys must be unique and should be hashable.
# We cannot do indexing and slicing in dictionary

# 1 - Create
'''
a = {}
print(a)            #empty dictionary
print(type(a))

a = dict()
print(a)            #empty dictionary
print(type(a))

dct1 = {'Name' : "Manvendra"}
print(dct1)


dct1 = {'Name' : ["Manvendra","Noufal","Gopika","Dilju"]} #values in list
print(dct1)

dct1 = {'Name' : ("Manvendra","Noufal","Gopika","Dilju")}  #values in tuple
print(dct1)

dct1 = {'Name' : {"Manvendra","Noufal","Gopika","Dilju"}} #values in set
print(dct1)
'''
# Key must be of immutable data type
'''
dct1 = {('Name',) : ["Manvendra","Noufal","Gopika","Dilju"],
        "Course" :"Data Analytics",
        1 : 35,
        "dct2" : {"T_Name" : "Ram","Age" : 34, "City" : "Bangalore"}}

print(dct1,"\n")

print(dct1[("Name",)],"\n")

print(dct1["Course"],"\n")

print(dct1["dct2"],"\n")

print(dct1["dct2"]["T_Name"],"\n")
'''

#       Methods

#print(dir(dict))

# Copy and Clear are same as other data types

# 2 - Length of the dictionary
''''
dct1 = {('Name',) : ["Manvendra","Noufal","Gopika","Dilju"],
        "Course" :"Data Analytics",
        1 : 35,
        "dct2" : {"T_Name" : "Ram",
                  "Age" : 34,
                  "City" : "Bangalore"}}

print(len(dct1))
'''

#help(dict.items)


# 3 - Items & Keys & Values
'''
dct1 = {('Name',) : ["Manvendra","Noufal","Gopika","Dilju"],
        "Course" :"Data Analytics",
        1 : 35,
        "dct2" : {"T_Name" : "Ram",
                  "Age" : 34,
                  "City" : "Bangalore"}}

print(dct1.items(),'\n')

print(dct1.keys(),'\n')

print(dct1.values())

print("\n")

for i,j in dct1.items() :
    print(i,j)

print("\n")
'''

#   4 -  Get    (to print the value of the key)
'''
dct1 = {'Name' : "John",
        "Course" :"Data Analytics",
        "Attendance" : 35}

print(dct1["Name"])
#print(dct1["Module"])     # error if key is not present

print(dct1.get('Name'))
print(dct1.get('Module'))   # no error if key is not present

print(dct1.get('Module',"There is no key")) # customize the output
print(dct1)
'''
#  5 -  Popitem  (removes and return the last item, return gives in tuple)

'''
dct1 = {'Name' : "John",
        "Course" :"Data Analytics",
        "Attendance" : 35}

print(dct1)
print(dct1.popitem())
print(dct1)

dct1 = {}

print(dct1)
print(dct1.popitem())
print(dct1)
'''


#  6 -     Pop   (removes any item)
'''
dct1 = {'Name' : "John",
        "Course" :"Data Analytics",
        "Attendance" : 35}
print(dct1)
'''

#print(dct1.pop())  # argument is needed
'''
print(dct1.pop('Course'))
print(dct1)
'''
# 7 - Dictionaty into list,tuple,set and string


# list, tuple and set gives only keys
'''
dct1 = {'Name' : "John",
        "Course" :"Data Analytics",
        "Attendance" : 35}

print(list(dct1))

print(tuple(dct1))

print(set(dct1))

print(str(dct1)) #gives all
'''

# 8 - List into dictionary (only if there is list in list)
'''
a = ["python",10,"data analytics",35]

#print(dict(a))


a = [["python",10],["data analytics",35]]

print(dict(a))

a = [["python",10,25],["data analytics",35]]

print(dict(a))      # only 2 elements are permitted
'''

# 9 - Tuple into dictionary
'''
a = ("python",10,"data analytics",35)

#print(dict(a))


a = (("python",10),["data analytics",35])
print(dict(a))

a = (["python",10,25],["data analytics",35])

#print(dict(a))      # only 2 elements are permitted
'''


# set into dictionary

# cannot process bcz set in not ordered
'''
a = {"python",10,"data analytics",35}

#print(dict(a))


a = {["python",10],["data analytics",35]}
#print(dict(a))

a = {["python",10,25],["data analytics",35]}
#print(dict(a))      # only 2 elements are permitted
'''

#   Fromkeys

#  10 - convert the elments of list,tuples,string into key of dictionary
'''
a = ['python','java','ml','iot']
print(dict.fromkeys(a))
print(dict.fromkeys(a,0)) #initialize with value


a = ('python','java','ml','iot')
print(dict.fromkeys(a))
print(dict.fromkeys(a,"z"))

a = "python"
print(dict.fromkeys(a))
print(dict.fromkeys(a,['z',1]))

a = {'python','java','ml','iot'}
print(dict.fromkeys(a))
print(dict.fromkeys(a,"z"))
'''

# 11 - Setdefault (update with a new key-value)
'''
x = {'name' :'john',
     'course' : 'data analytics',
     'test1' : 35}
     
x.setdefault('test2','still to take place')

print(x.setdefault('test2','still to take place'))

print(x['test2'])

print(x)
'''

# 12 - Update (can change and add new key-values)

'''
x = {'name' :'john',
     'course' : 'data analytics',
     'test1' : 35}
     
x.update({'test1':45,'test2':65})

print(x)
'''





