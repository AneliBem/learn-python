for i in range(1, 11):

    if i % 2 == 0:
        continue

    if i == 7:
        break

    print("Element:", i)

print("\n\n2 task")

for i in range(1, 25, 3):
    print("Element:", i)

print("\n\n3 task")

word = "Some text"
for i in word:
    print(i)

print("\n\n4 task")

for i in word:
    if i == "m":
        print("Літера m є")


print("\n\n5 task (while)")

i = 0
while i <= 10:
    print(i)
    i += 1

print("\n\n6 task (while)")

work = True
while work:
    user_input = input("Enter word STOP: ")
    if user_input == "STOP":
        work = False

print("while is done")

print("\n\n7 task")

word = "Some text"
for i in word:
    if i == "c":
        print("Done")
        break
else:
    print("Not found")
