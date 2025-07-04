#sets
'''
my_set = {1, 2, 3, 4, 5}

print(my_set) 

my_set.add(6)
print(my_set)  

my_set.remove(3)
print(my_set)

'''
#Union of two sets
set1 = {1, 2, 3}
set2 = {3, 5, 6}

union_set = set1.union(set2)
print(union_set)

#Intersection of two sets
inner_set = set1.intersection(set2)
print(inner_set)

#Difference of two sets
diff_set = set1.difference(set2)
print(diff_set)

#Sets a usueful when you want to store unique items