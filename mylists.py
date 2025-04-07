# 1.Create 
my_list = []

# 2.Append 
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# 3.Insert 
my_list.insert(1, 15)

# 4.Extend
my_list.extend([50, 60, 70])

# 5.Remove
my_list.pop()

# 6.Sort
my_list.sort()

# 7.Find and print 
index_of_30 = my_list.index(30)
print(f"The index of 30 in my_list is: {index_of_30}")

print(f"The final my_list is: {my_list}")
