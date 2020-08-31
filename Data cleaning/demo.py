# we can make set from a list
# Output: {1, 2, 3}
my_set = set([1, 2, 3, 2 ,2,"haha"])

my_set.add(10)
my_set.add(10)
print(my_set)

dic = {}
# set cannot have mutable items
# here [3, 4] is a mutable list
# this will cause an error.

dic["a"] = set([type(1.1), type([]), type(None)])

print(dic["a"])