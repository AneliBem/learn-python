word = list("python")
word[0] = "P"
word.append("?")
result = "".join(word) # об'єднання в строку
print(word)
print(len(word)) # довжина рядка
print(word.count("o"))
print(result)
print(result.upper()) # Верх регістер
print(result.lower()) # Нижній регістер
print(result.capitalize()) # перша буква в верх регістрі
print(result.isupper()) # перевірка чи всі символи в верх регістрі
print(result.islower()) # перевірка чи всі символи в низ регістрі

print("\n\n")

text = "football,basketball,skate"
hobbies = text.split(",") # розділення списку по розділювачу

for i in range(0, len(hobbies)):
    hobbies[i] = hobbies[i].capitalize()

resultat = ", ".join(hobbies)
print(resultat)

print("\n\n")
nums = [5, 7, 5, 5.45, True, 6]
print(nums[0:3])
print(nums[:-1])
print(nums[2:])
print(nums[0::2])