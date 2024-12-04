nums = [5, 7, 5, 5.45, True, 6]
nums[1] = 45.5
print(nums)
print(nums[3])

nums2 = [5, 7, 8,[6, 79, True]]
print(nums2[-1][0])

nums.append(45) # додавання ел. в кінець списку
nums.insert(1, False) # зміна ел. за індексом
nums2.extend(nums) # в список додати список
nums.sort() # сортування
nums.reverse() # перевертає список
nums.pop() # видаляє останній елемент
nums.remove(5.45) # видаляє ел. за значенням
# nums.clear() # очищення списку
print(nums.count(5)) # кількість елементів з таким значенням
print(len(nums)) #довжина списку

print(nums)
print(nums2)

print("\n\n2")

for i in nums:
    el = i * 2
    print(el)

print("\n\n3")

user_hobby = int(input("Enter hobby number: "))

i = 0
hobby = []
while i < user_hobby:
    text = "Enter hobby " + str(i + 1) + ": "
    hobby.append(input(text))

    i += 1

print(hobby)