import time
from binary_search_tree import BSTNode

start_time = time.time()

f = open('names/names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names/names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# less than a second with python lists

# for name_1 in names_1:
#     if name_1 in names_2:
#         duplicates.append(name_1)

# still about less than a second with a bst search

# grab the first value of the first list to create
# the bst
bst = BSTNode(names_1[0])
# create lambda function that appends any dupes
# it finds in the bst
func = lambda x: duplicates.append(x)
# for loop that inserts all the values of the
# first list into the bst

# time complexity of the construction of a binary search tree
# would be O(nlogn)
for name_1 in names_1[1:]: #O(n)
    bst.insert(name_1) #O(logn)
# O(n) * O(logn) = O(nlogn)
# contain_in_list checks all the nodes
# values and see if that value
# is in the passed in list and if it is,
# append that value into the dupes list

# since this has to check all the nodes in the bst to
# find dupes, the time complexity would be O(n)
bst.contain_in_list(names_2, func)

# final time complexity would be O(nlogn)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
