immutable_var = 1, 3, 5, "A", "B", "C", True
print(immutable_var)
immutable_var = ([1, 3, 5,], "A", "B", "C", True)
print(immutable_var)
immutable_var[0][2]=358
print(immutable_var)
mutable_list = [11,22,33,"икс","игрек","зед", False]
print(mutable_list)
mutable_list [3] = "зеро"
print(mutable_list)
mutable_list [6] = "999"
print(mutable_list)
mutable_list = [11,22,33,"икс","игрек","зед", False] + [9,8,7,6,5]
print(mutable_list)
mutable_list = [11,22,33,"икс","игрек","зед", False] + [9,8,7,6,5] * 2
print(mutable_list)