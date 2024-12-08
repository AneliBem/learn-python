def test_func(word):
    print(word, end='')
    print('!')


test_func('hello') # вивід функції (значення)
word = 'none'
test_func(word)
test_func('Hi')

print("\n\n")

def summa(a, b):
    res = a + b
    print(res)


summa(5, 6)
summa(3.6, 7.4)
summa("hi", " world")

print("\n\n")

def summa(a, b):
    res = a + b
    print(res)
    return res


res1 = summa(5, 6)
res2 = summa(3.6, 7.4)
res3 = summa("hi", " world")
print(res1)


print("\n\n")

# скорочення циклів за допомогою функцій
def minimal(l):
    min_num = l[0]
    for i in l:
        if i < min_num:
            min_num = i

    return min_num

nums1 = [5, 6, 1, -4, 0, 7]
res1 = minimal(nums1)

# nums1 = [5, 6, 1, -4, 0, 7]
# min1 = nums1[0]
# for i in nums1:
#     if i < min1:
#         min1 = i
#
# print(min1)

nums2 = [5, -6, 1, 4, 0, 7]
res2 = minimal(nums2)

# nums2 = [5, -6, 1, 4, 0, 7]
# min2 = nums2[0]
# for i in nums2:
#     if i < min2:
#         min2 = i
#
# print(min2)

if res1 < res2:
    print(res1)
else:
    print(res2)

print("\n\n")

# lambda
func = lambda x, y: x * y
print(func(5, 7))