#Lists: ordered, mutable, allows duplicate elements

mylist = ["banana", "cherry", "apple"]
print(mylist)

mylist2 = [5, 4, 3, 2, 1, 0]
print(mylist2)

print(mylist[2])
print(mylist[-1])

# Iterate through list
for i in mylist:
     print(i)

if 'orange' in mylist:
     print("yes")
else:
     print('no')

# Add to end of list
mylist.append("lemon")
print(mylist)
print(len(mylist))

# Add to a specific location in list
mylist.insert(0, "orange")
print(mylist)

# Remove last item
item = mylist.pop()
print(item)
# Remove specific item from list
mylist.remove("cherry")
print(mylist)

# Reverse list
mylist.reverse()
print(mylist)

# Remove all items
mylist.clear()
print(mylist)

# Sorting lists
sorted_list = sorted(mylist2)
print(sorted_list)
print(mylist2)
mylist2.sort()
print(mylist2)

# List with same item multiple times
mylist = [0] * 5
print(mylist)

# Concatination
new_list = mylist + mylist2
print(new_list)

# Splicing
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a = mylist[1:5]
b = mylist[:5]
c = mylist[4:]
d = mylist[1::2]
rev = mylist[::-1]
print(a)
print(b)
print(c)
print(d)
print(rev)

# Copy list
list_org = ["banana", "cherry", "apple"]

# This method refers to the original place in memory so any changes made to the copy will be applied to the original
#list_cpy = list_org
list_cpy = list(list_org)
list_cpy2 = list_org[:]
print(list_cpy)
list_cpy.append("Lemon")
print(list_org)
print(list_cpy)
print(list_cpy2)

# Create new list with functoin applied to each item
a = [1, 2, 3, 4, 5, 6]
b = [i*i for i in a]
print(a)
print(b)