# file = open("data/file.txt", "w+") # w = запис файлу, "+" = створити файл якщо його неіснує
data = input("Hobby: ")
file = open("data/file.txt", "a") # а = додавання інформації до файлу
file.write(data + "\n")
# file.write("!!!")

file.close()
