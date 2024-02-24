# sets are started with curly brackets like {..}

seta = {"a","b","c","a","c"}
print(seta)

# add element in set
seta.add("d")
seta.add("e")
print(seta)

# remove element
seta.remove("a")
print(seta)

# convert list to set
list_test = ["pop", "rock", "soul", "hard rock", "rock", "R&B", "rock", "disco"]
setb = set(list_test)
print(setb)

# find the intersection
album_set1 = set(['AC/DC', "Thriller", 'Back in Black'])
album_set2 = set(["Back in Black", "AC/DC", "The Dark Moon"])
print(album_set1 & album_set2)

# Intersection with method
print(album_set1.intersection(album_set2))

# Find the difference in set1 but not set2
print(album_set1.difference(album_set2))
print(album_set2.difference(album_set1))

# union of two sets
print(album_set1.union(album_set2))

# Check the superset in b/w
print(set(album_set1).issuperset(album_set2))
print(album_set1.issuperset({"Back in Black", "AC/DC"}))

# Check if subset
print(set(album_set2).issubset(album_set1))
print(set({"Back in Black", "AC/DC"}).issubset(album_set1))

# check sum of A = sum of B
A = [1, 1, 2, 2]
B = set([1, 2, 2, 1])
print("the sum of A is:", sum(A))
print("the sum of B is:", sum(B))