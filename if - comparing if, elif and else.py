#P.55-P.57

disaster = True
if disaster:
    print("Woe!")
else:
    print("Whee!")

furry = False
large = True

if furry:
    if large:
        print("It's a yeti.")
    else:
        print("It's a cat!")
else:
    if large:
        print("It's a whale!")
    else:
        print("It's a human. Or a hairless cat.")


color = "red"
if color == "red":
    print("It's a tomato")
elif color == "green":
    print("It's a green pepper")
elif color == "bee purple":
    print("I don't know what it is, but only bees can see it")
else:
    print("I've never heard of the color", color)

x = 7
print(5 < x and x < 10)
print(x == 5)
print(5 < x or x < 10)
print(5<x and not x>10)

some_list = [x]
if some_list:
    print("There's something in here")
else:
    print("Hey, it's empty!")
