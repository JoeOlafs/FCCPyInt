# Sets: unordered, mutable, no duplicates
my_set = {1, 2, 3, 1, 2}
print(my_set)
my_set = set([1,2,3]) # works with lists
print(my_set)
my_set = set("hello") # works with strings
print(my_set)

# Create empty set
my_set_wrong = {}
my_set = set()
print(type(my_set_wrong))
print(type(my_set))

# Add/remove items to set
my_set.add(1)
my_set.add(2)
my_set.add(3)
print(my_set)
my_set.remove(3)
my_set.discard(3) # Does not throw an error if element is not in set
print(my_set)

# Iterate through set
for i in my_set:
     print(i)

# Check for elements
if 1 in my_set:
     print("yes")

# Union & intersections
odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

u = odds.union(evens)
print(u)

i = odds.intersection(primes)
print(i)

# Difference between sets
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}

print(setA.difference(setB))
print(setB.difference(setA))
print(setA.symmetric_difference(setB))

# Update sets
setA.update(setB)
print(setA)

setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}
setA.intersection_update(setB)
print(setA)

setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}
setA.difference_update(setB)
print(setA)

setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}
setA.symmetric_difference_update(setB)
print(setA)

# Subsets, Supersets & disjoined
setA = {1, 2, 3, 4, 5, 6}
setB = {1, 2, 3}
setC = {7, 8, 9}
print(setA.issubset(setB))
print(setB.issubset(setA))
print(setA.issuperset(setB))
print(setB.issuperset(setA))
print(setA.isdisjoint(setB))
print(setA.isdisjoint(setC))

# Frozenset - immutable version
a = frozenset([1, 2, 3, 4])
# a.add(2) does not work
print(a)