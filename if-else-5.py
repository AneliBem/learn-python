num = float(input("Enter num: "))

isHasCar = True

if num >= 55 and isHasCar:
    print("Yes num is 55+")
    if num != 56 or isHasCar:
        print("Num no is 56")
        if num == 100:
            print("Num is 100")
elif num == 40:
    print("Num is 40")
else:
    print("Else")


isHappy = False
if not isHappy:
    print("Yes he is no happy")



data = "Info"
# if data == "Info":
#     correct = True
# else:
#     correct = False

correct = True if data == "Info" else False

print(correct)