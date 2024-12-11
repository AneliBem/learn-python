# num = None
#
# while num is None:
#     try:
#         num = int(input("Enter num: "))
#         num += 5
#         print(num)
#     except ValueError:
#         print("Некоректне значення")

try:
    a = 10
    b = int(input("Enter num: "))
    print(a / b)
except ValueError:
    print("Некоректне значення")
except ZeroDivisionError:
    print("На нуль ділити не можна")
# except Exception # реагує на всі помилки
#     print("Некоректне значення")
else:
    print("Erroe None")
finally: # спрацьовує хавжди в кінці
    print("The end")