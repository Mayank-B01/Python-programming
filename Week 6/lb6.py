set1 = {"apple", "banana", "orange", "strawberry"}
set2 = {"orange", "peach", "watermelon", "strawberry"}
uni = set1.union(set2)
inter = set1.intersection(set2)
diff = set1.difference(set2)
diff2 = set2.difference(set1)
print(uni)
print(inter)
print(diff)
print(diff2)
tuple1 = (1, 2, 3, 4, 5)
reverse_tuple1 = tuple(reversed(tuple1))
print(reverse_tuple1)
index_no = tuple1.index(3)
print(index_no)