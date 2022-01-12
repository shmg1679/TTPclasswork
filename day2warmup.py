import math
import sys

# using slice syntax
word = "hello world"
# 1
print(word[2:6])
# 2
print(word[::-1])

# using input()
# 3
userInt = input("enter something: ")
print(userInt[::-1])
# 4
print("your word is ", userInt)

# using type()
# 5
a = 10022
b = "wuuuut"
c = True
print(type(a))
print(type(b))
print(type(c))

# algebra operation
# 6
d = 2333
print(a+d)
# 7
print(math.sqrt(49))
print(math.sqrt(43))
print(math.sqrt(69))
print(math.sqrt(36))
print(math.sqrt(4))
# 8
print(a//d)
print(155//33)
print(44//3)
print(220//23)


# list/arrays
# 9
mylist = [1, 2, "ddsds", 4]
mylist2 = [5, 6, "e2rr", 8]
mylist3 = mylist+mylist2
print(mylist3)
print(mylist+mylist2)

# 10
arr1 = (1, 2, 3, 4, 5, 6)
arr2 = (4, 5, 6, 6, 7)
arr3 = arr1+arr2
print(arr3)

# converting objects
# 11
int1 = 25
change = 25*1.0
print(change)
print(type(change))
print(int1)
print(float(int1))
print("change this into string "+str(change))
i = True
int(i)
print(type(i))

# 12
string1 = "this is a string"
string2 = string1.upper()
print(string2)
print(string1.upper())

# challenge section
# 13
stringg = list("python")
for i in range(len(stringg)):
    print(stringg[i])

for letter in stringg:
    print(letter)

# 14
print(stringg[2])

# 15
print(sys.version)
print(sys.version_info)
