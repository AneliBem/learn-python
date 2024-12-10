file = open("data/file.txt", "r") # r = читання файлу
# print(file.read(10)) # кількість символів які треба вивести
for line in file:
    print(line, end="")
file.close()