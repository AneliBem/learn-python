data = {"abc", "Bob", 7, True, True, True, 24.5, 24.5} # множина виводмить елементи з одним значенням лише раз
# data[0] = "Bob" # error

# print(data[0]) # error
data.pop() # видалення останнього знач. коли виводиться
# data.clear()
data.add(5) # додавання елементу
data.update(["4", 6, 24.5]) # додається тільки перший елемент, інші присутні
data.remove(6) # видалення елемент. за значенням
print(data)

nums = [5, 6, 2, 7, 6, 2, 5]
res = set(nums)
print(res)
Text = "Hello"
print(set(Text))

#frozenset
data2 = frozenset(["abc", "Bob", 7, True, True, True, 24.5, 24.5]) # заморожена множина
# data2.pop() # error
# data.clear() # error
# data2.add(5) # error
# data2.update(["4", 6, 24.5]) # error
# data2.remove(6) # error
print(data2)