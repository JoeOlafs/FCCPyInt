# Dictionary: Key-Value pairs, Unordered, Mutable
my_dict = {"name": "Max", "age": 28, "city": "New York"}
my_dict2 = dict(name="Joe", age=27, city="Kamloops")
print(my_dict)
print(my_dict2)

# Print specific values
print(my_dict["age"])

# Add to dictionary
my_dict["Email"] = "max@xyz.com"
print(my_dict)

# Override value
my_dict["Email"] = "coolmax@xyz.com"
print(my_dict)

# Remove items
del my_dict["name"]
print(my_dict)
my_dict.pop("age")
print(my_dict)
my_dict.popitem()
print(my_dict)

# Search in dictionary
my_dict = {"name": "Max", "age": 28, "city": "New York"}
if "name" in my_dict:
     print(my_dict["name"])
else:
     print("Name is not in dictionary")

# Loop through dictionary
for key in my_dict:
     print(key)

for key, value in my_dict.items():
     print(key,value)

# Copy dictionary
my_dict_cpy = my_dict.copy()

my_dict_cpy["email"] = "max@xyz.com"
print(my_dict)
print(my_dict_cpy)

# Merging dictionaries
my_dict = {"name": "Max", "age": 28, "email": "max@xyz.com"}
my_dict2 = {"name": "Mary", "age": 27, "city": "Boston"}

my_dict.update(my_dict2)
print(my_dict) # Values get updated if keys are in both dictionaries, otherwise they stay the same

# Using Tuples as keys
mytuple = (8, 7)
my_dict = {mytuple: 15}
print(my_dict) # Lists do not work because they are mutable