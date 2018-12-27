# similar to dictionary
# hashed and immutable
# used less often
# good for cleaning up data

farm_animals = {"sheep", "cow", "hen"}
print(farm_animals)

for animal in farm_animals:
  print(animal)

print("=" * 40)

wild_animals = set(["lion", "tiger", "panther", "elephant", "hare"])
print(wild_animals)

for animal in wild_animals:
  print(animal)

farm_animals.add("horse")
wild_animals.add("horse")

print(farm_animals)
print(wild_animals)

# no inherint ordering
# user set() to create an empty set

empty_set = set()
# empty_set_2 = {} // doesn't create empty set
empty_set.add("a")
# empty_set_2.add("a") // cannot add

even = set(range(0, 42, 2))
print(even)
squares_tuple = (4, 6, 9, 16, 25)
squares = set(squares_tuple)
print(squares)

print(len(even))

print(len(squares))

print(even.union(squares))
print(len(even.union(squares)))

print(squares.union(even))

print("-" * 40)

print(even.intersection(squares))
print(even & squares)
print(squares.intersection(even))
print(squares & even)

print("-" * 40)

print(sorted(even))
print(sorted(squares))

print("even minus squares")
print(sorted(even.difference(squares)))
print(sorted(even - squares))

print("squares minus even")
print(squares.difference(even))
print(sorted(squares - even))

print("=" * 40)

print(sorted(even))
print(squares)
# even.difference_update(squares) // commented bc of symmertric_diff
print(sorted(even))

print("-" * 40)

print("symmetric even minus squares")
print(sorted(even.symmetric_difference(squares)))

print("symmetric squares minus even")
print(squares.symmetric_difference(even))
print(squares ^ even) # shorthand

# don't rely on python to sort

print("-" * 40)

# discard vs remove, remove raises error if no object

squares.discard(4)
squares.remove(16)
squares.discard(8) # no error, does nothing
# squares.remove(8) # error

print(squares)

try:
  squares.remove(8)
except KeyError:
  print("The item 8 is not a member of the set")

print("=-" * 20)

even = set(range(0, 40, 2))
squares_tuple = (4, 6, 16)
squares = set(squares_tuple)

if squares.issubset(even):
  print("squares is a subset of even")

if even.issuperset(squares):
  print("even is a superset of squares")

print("*" * 40)

even = frozenset(range(0, 100, 2))

print(even)
even.add(3) # error frozen set


