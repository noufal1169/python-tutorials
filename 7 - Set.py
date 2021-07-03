
#                                        ---
#                                        SET
#                                        ---

#  sets are unordered collection of elements enclosed within a curly  bracket and separated by commas.
#  sets are randomly ordered.
#  set does not stroes duplicate values.
#  the elements contained in a set must be immutabel type.
#  sets cannot be indexed and sliced



# 1 - Create Set

'''
a = {}
print(a)
print(type(a)) # this is not an empty set

a = set()
print(a)
print(type(a))   # this is an empty set

b = {10,'Python',30,True,40}
print(b)

b = {10,('Python',30),True,40}
print(b)

b = {10,['Python',30],True,40}
print(b)
'''

# set cannot store mutable data types
# set is mutable


#print(dir(set))

# Set Methods


# 2 - add
'''
a = {1,10,19,23}
print(a)
a.add(50)
print(a)
print(a.add(14)) #none
print(a)

a.add(23,24)
print(a)     # only one argument is added
'''

# 3 - update
'''
a = {1,10,19,23}
print(a)
a.update({50,100}) # updating set with another set
print(a)

b = [200,300] # we can use string,tuple,and list also
a.update(b)
print(a)
'''

# 4 - SUPER SET AND SUB SET

#if every element in a set_a  is present in set_b, then a is sub set of b and b is the super set
'''
a = {1,10,19,23}
b = {1,23}

print(b.issubset(a))
print(a.issuperset(b))
'''


# 5 - Union & Intersection function
'''
a = {10,34,12,90}
b = {12,13,40}

print(a)
print(b)

print(a.union(b))

print(a.intersection(b))
'''

# 6 - Set Difference
'''
a = {10,34,12,90}
b = {12,13,40}

print(a-b)
print(b-a)

print(a.difference(b))
print(b.difference(a))
'''

# 7 - Symmetric Difference

#removes the common elements and gives the rest
'''
a = {10,34,12,90}
b = {12,13,40}

print(a.symmetric_difference(b))
'''

# 8 - Intersection Update
'''
a = {10,34,12,90}
b = {12,13,40}

print(a)
print(a.intersection(b))
print(a)
print(a.intersection_update(b)) #none bcz this is not a new variable,its only modifing a
a.intersection_update(b)
print(a)
'''

# 9 - Difference Update
'''
a = {10,34,12,90}
b = {12,13,40}

a.difference_update(b)
print(a)
'''

# 10 - Symmetric Difference Update
'''
a = {10,34,12,90}
b = {12,13,40}

a.symmetric_difference_update(b)
print(a)
'''

# 11 - Clear
'''
a = {10,30,1,2,3}
a.clear()
print(a)
'''

# 12 - Copy
'''
a = {10,30,1,2,3}
b = a
print(id(a),id(b))
print(a,b)

a = {10,30,1,2,3}
b = a.copy()
print(id(a),id(b))
print(a,b)
'''


# 13 - Remove (remove one item)
'''
a = {10,30,1,2,3}
a.remove(10)
print(a)

a.remove(30,1)
print(a)  # error if more than one argument is given

a = {10,30,1,2,3}
a.remove(40)
print(a)  # error if the element given is not present
'''

# 14 - Discard  (remove one element without error)
'''
a = {10,30,1,2,3}
a.discard(10)
print(a)

a = {10,30,1,2,3}
a.discard(40)
print(a)  # no error if the element given is not present, the entire set is given instead

a.discard(30,1)
print(a)  # error if more than one argument is given
'''

# 15 - Pop (removes and return a random element)

'''
a = {10,30,1,2,3}
a.pop()
print(a)

a = {10,30,1,2,3}
print(a.pop())
print(a)

a = {10,30,1,2,3}
a.pop(1)              # no parameter is taken in pop of set
print(a)
'''

# 16 - Isdisjoint (true is no common elements)
'''
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

print(x.isdisjoint(y))


x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "mac"}

print(x.isdisjoint(y))

x = set ()
y = set ()

print(x)
print(y)

print(x.isdisjoint(y))
'''

# 17- Frozenset (make a mutable set into an immutable set)
'''
a = {10,20,45,'python'}

print(a)

b = frozenset(a)

print(b)
'''















