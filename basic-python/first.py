
# Lists
first_list = ["Maish", "Sahil"]
# print(first_list)

num_list = [1, 2, 3, 4, 5]
# for i in num_list:
#     print(i)
s_list = [x**2 for x in num_list]
# print(s_list)

second_list = [1, 2, 3, 4, 5]
second_list.append(2)
second_list.pop(0)
second_list.insert(0,1)
print(second_list)


#Dictionaries

first_dict = {'a': "Manish", 'b': "Sahil", 'c': "Rahul"}

# key and value
for key, value in first_dict.items():
    print(key, value)



# for printing both key and value at once
# for key, value in first_dict.items():
#     print(key, value)

# individual method

print(first_dict
      .keys())  # this will print all the keys in the dictionary
# i want to print one key at a time 
print(first_dict['a'])

print(first_dict
      .values())  # this will print all the values in the dictionary

print(first_dict
      .items())  # this will print all the items in the dictionary

# for getting specific values
# print(first_dict['a'])
# print(first_dict['b'])
# print(first_dict.get('a'))  # same as above, this will also print the value of 'a'

# ok, now printing the values of the dictionary without for loop
print(first_dict['a'], first_dict['b'], first_dict['c'])



for i in range(3):
    # i want i value to be in a b c in increamenting order
    print(f"{i} : {first_dict.get(chr(97+i))}") # this will print the key and value of the dictionary

# for printing abc in series order
for i in range(3):
    print(chr(97+i)) 
 
# set
set = {1, 2, 3, 4, 5}
print(set)
union_set = set.union({6, 7})
print(union_set)


# Tuples
tuple = (1, 2, 3)
print(tuple)
# make some hard tuples
t = (1, 2, 3, 4, 5)
print(t)
print(t[0])
print(t[1])
print(t[2])
print(t[3])
print(t[4])
print(t[0:3])


# Basic Algorithms
# linear search
def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i]==x:
            return i
    return -1

arr = [1, 2, 3, 4, 5]
print(linear_search(arr, 8)   ) 


