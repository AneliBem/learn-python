import time # connect modules time
import datetime as data # тег для звернення до модуля
import sys
import os
import platform
from math import ceil, sqrt as s # імпорт деяких функцій з модуля
import mymodulesixteen

import Django # підключення сторонього модуля

print(ceil(s(25)))

print(sys.path) # шлях до проекта
print(os.name) # ім'я ОС
print(platform.system()) # ОС

time.sleep(2) # зупинка програми на вказаний час
print("Hello")
print(data.datetime.now().time()) # вивід часу

mymodulesixteen.hi()
print(mymodulesixteen.name)
res = mymodulesixteen.add_3_number(3, 8, 5)
print(res)