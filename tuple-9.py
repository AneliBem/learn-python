data = (5, 7, 5, 5.45, [True, 6])

# data[1] = 45.5 error

print(data)
print(data[0:3])
print(data[:-1])
print(data.count(5))

info = 4, 5, 'some'
print(info)

some = 4,
print(some)

print("\n\n")

for el in data:
    print(el, end=" ")

print("\n\n")

title = [5, 7, 8,[6, 79, True]]
title1 = tuple(title)
print(title1)
