# try:
#     file = open("text.txt", "r") # а = додавання інформації до файлу
#     print(file.read())
# except FileNotFoundError:
#     print("File not found")
# finally:
#     file.close()


# With...as
try:
    with open("text.txt", "r", encoding="utf-8") as file: # utf-8 = файл може бути з кирилецею
        print(file.read())
except FileNotFoundError:
    print("File not found")