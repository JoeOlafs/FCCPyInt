# Tuple: ordered, immutable, allows duplicate elements
mytuple = ("Max", 28, "Boston")

# Iterate through tuple
for i in mytuple:
     print(i)

# Check if item in Tuple
if "Max" in mytuple:
     print("yes")
else:
     print("no")

my_tuple = ('a', 'p', 'p', 'l', 'e')

# Check Length
print(len(my_tuple))

# Check count of item
print(my_tuple.count('p'))

# Check location of item
print(my_tuple.index('p'))

# Convert to list
my_list = list(my_tuple)
print(type(my_list))
my_tuple2 = tuple(my_list)
print(type(my_tuple2))

# Slicing, works the same as lists
a = (1, 2, 3, 4, 5, 6, 7, 8, 9)

b = a[1:6]
print(b)

# Unpacking
name, age, city = mytuple
print(name, age, city)

i1, *i2, i3 = a
print(i1, i2, i3)

# Comparing List to Tuple
import sys
import timeit
my_list = [0, 1, 2, "Hello", True]
my_tuple = (0, 1, 2, "Hello", True)
print(sys.getsizeof(my_list, bytes))
print(sys.getsizeof(my_tuple, bytes))
print(timeit.timeit(stmt="[0, 1, 2, 3, 4, 5]", number=1000000))
print(timeit.timeit(stmt="(0, 1, 2, 3, 4, 5)", number=1000000))