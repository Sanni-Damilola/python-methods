# 1: Append()
people = ["Carl Johnson", "Sweet", "Sweet", "Big Smoke", "bola", "anu"]
people.append("Sanni")
# print(people)

# 2: Clear()
# people.clear()
# print(people)

# 3: copy()
copy_people: list[str] = people.copy()
print(copy_people)
copy_people.remove("Sweet")
print(copy_people)

# 4: count()
print(people.count("Sweet"))

# 5: extend()
extend_list : list[str] = ["A", "B", "C"]
extend_list1: list[int] = [1, 2, 3, 4,]
extend_list.extend(extend_list1)
print(extend_list)

# 6: index()
print(people.index("Sweet"))

# 7: insert()
extend_list1.insert(0,"0")
print(extend_list1)

# 8: pop()
extend_list1.pop(0)
print(extend_list1)

# 9: remove()
extend_list1.remove(1)
print(extend_list1)

# 10: reverse()
extend_list1.reverse()
print(extend_list1)

# 11 sort()
people.sort()
print(people)
people.sort(key=lambda name: len(name))
print(people)