this_tuple = (1, "Hello", 3, 6, 5, "World")
temp = list(this_tuple)
temp[3] = 300
this_tuple = tuple(temp)
print(this_tuple)
