"""
# while
count = 1
while count <= 5:
    print(count)
    count += 1

while True:
    stuff = input("String to capitalize [type q to quit]: ")
    if stuff == "q":
        break
    print(stuff.capitalize())
    
# continue
while True:
    value = input("Integer, please [q to quit]: ")
    if value == "q":
        break
    number = int(value)
    if number % 2 == 0:
        continue
    print(number, "squared is ", number * number)

# else to break
numbers = [2, 3, 5]
position = 0
while position < len(numbers):
    number = numbers[position]
    if number % 2 == 0:
        print("Found even number", number)
        break
    position += 1
else:
    print("No even number found")
"""
# for and in
word = "thud"
offset = 0
while offset < len(word):
    print(word[offset])
    offset += 1

for letter in word:
    print(letter)

# for and in - break
word = "thud"
for letter in word:
    if letter == "u":
        break
    print(letter)

# for and in - else to break
word = "thudx"
for letter in word:
    if letter =='x':
        print("Eek! An 'x'!")
        break
    print(letter)
else:
    print("No 'x' in there.")

# range()
for x in range(0, 3):
    print(x)
print(list(range(0, 3)))

for x in range(2, -1, -1):
    print(x)
print(list(range(2, -1, -1)))
print(list(range(0, 11, 2)))

# excercise 6-1
for x in range(3, -1, -1):
    print(x)
print(list(range(3, -1, -1)))

# excercise 6-2
guess_me = 7
number = 1
while True:
    if number < guess_me:
        print("too low")
    elif number == guess_me:
        print("found it!")
        break
    else:
        print("oops")
        break
    number += 1

# excercise 6-3
guess_me = 5
number = 0
for number in range(10):
    number += 1
    if number < guess_me:
        print("too low")
    elif number == guess_me:
        print("found it!")
        break
    else:
        print("oops")
        break
