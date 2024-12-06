person = {'name': 'Anatolii', 'age': 20, 5: 12, True: 'False', (3, 5): 45 }
print(person)
print(person['age'])
print(person[5])
print(person[(3, 5)])
person[5] = 'Five'
print(person[5])

print('\n\n')

person1 = dict(name = 'Alex', age = 15)
print(person1['age'])

print('\n\n')

for key in person:
    print(key)

print('\n\n')

for key, values in person.items():
    print(key, values, sep=" - ")

print('\n\n')

for el in  person.values():
    print(el)

print(person.get('name')) # вивід значення за ключем

person.popitem() # видалення останього елемента
person.pop(5) # видалення за ключем
person['bio'] = 'Text' # додавання елемента в словник

print(person)

print('\n\n')

people = {
    'user1':{
        'name': 'John',
        'age': 27,
        'adress': ('Seattle', 'Some street', 6635),
        'grades': {'math': 5, 'physics': 2}
    },
    'user2':{
        'surname': 'Doe',
        'name': 'Alex',
    }

}
print(people['user1']['adress'][1])

