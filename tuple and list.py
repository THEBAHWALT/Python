# tuple

# , ()
empty_tuple = ()
print(empty_tuple)
one_marx = "Groucho",
print(one_marx)
one_marx = ('Groucho')
print(one_marx)
print(type(one_marx))
marx_tuple = 'Groucho', 'Chico', 'Harpo'
print(marx_tuple)
print(type(marx_tuple))
marx_tuple = ('Groucho', 'Chico', 'Harpo')
print(marx_tuple)
print(type(marx_tuple))
one_marx = 'Groucho',
print(type(one_marx))
print(type('Groucho',))
print(type(('Groucho',)))
password = 'swordfish'
icecream = 'tuttifrutti'
password, icecream = icecream, password
print(password, icecream)

# tuple()
marx_tuple = ['Groucho', 'Chico', 'Harpo']
print(tuple(marx_tuple))
marx_tuple = ('Groucho',)+('Chico', 'Harpo')
print(marx_tuple)

# tuple comparing
a = (7, 2)
b = (7, 2, 9)
print(a == b)
print(a <= b)
print(a >= b)

# tuple - for and in
words = ("fresh", "out", "of", "ideas")
for word in words:
    print(word)

# tuple - changing
t1 = ('Fee', 'Fie', 'Foe')
t2 = ('Flop',)
print(t1 + t2)

t1 = ('Fee', 'Fie', 'Foe')
t2 = ('Flop',)
t1 += t2
print(t1)
t1 = ('Fee', 'Fie', 'Foe')
t2 = ('Flop',)
print(id(t1))
t1 += t2
print(id(t1))  

# list 
empty_list = []
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
big_birds = ['emu', 'ostrich', 'cassowary']
first_names = ['Graham', 'John', 'Terry', 'Terry', 'Michael']
leap_years = [2000, 2004, 2008]
randomness = ['Punxsutawney',{"groundhog":"Phil"}, "Feb. 2"]
print(randomness)

# list()
another_empty_list = list()
print(another_empty_list)
print(list('cat'))
a_tuple = ('ready', 'fire', 'aim')
print(list(a_tuple))

# split()
talk_like_a_pirate_day = "9/19/2019"
print(talk_like_a_pirate_day.split('/'))
splitme = 'a/b//c/d///e'
print(splitme.split('/'))
print(splitme.split('//'))

# offset
marxes = ['Groucho', 'Chico', 'Harpo']
print(marxes[0])
print(marxes[1])
print(marxes[2])
print(marxes[-1])
print(marxes[-2])
print(marxes[-3])

# slice
marxes = ['Groucho', 'Chico', 'Harpo']
print(marxes[0:2])
print(marxes[::2])
print(marxes[::-2])
print(marxes[::-1])
marxes = ['Groucho', 'Chico', 'Harpo']
marxes.reverse()
print(marxes)
marxes = ['Groucho', 'Chico', 'Harpo']
print(marxes[4:])
print(marxes[-6:])
print(marxes[-6:-2])

# append()
marxes = ['Groucho', 'Chico', 'Harpo']
marxes.append('Zeppo')
print(marxes)

# insert() and offset
marxes = ['Groucho', 'Chico', 'Harpo']
marxes.insert(2, 'Gummo')
print(marxes)
marxes.insert(10, 'Zeppo')
print(marxes)

# *
print(["blah"]*3)

# extend() and +
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
others = ['Gummo', 'Karl']
marxes.extend(others)
print(marxes)

# + and +=
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
others = ['Gummo', 'Karl']
marxes += others
print(marxes)
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
others = ['Gummo', 'Karl']
marxes.append(others)
print(marxes)

# 使用offset更改一個項目
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
marxes[2] = 'Wanda'
print(marxes)

# 使用Slice更改項目
numbers = [1, 2, 3, 4, 5]
numbers[1:3] = [8, 9]
print(numbers)
numbers[1:3] = [7, 8, 9]
print(numbers)
numbers[1:3] = []
print(numbers)
numbers = [1, 2, 3, 4, 5]
numbers[1:3] = [98, 99, 100]
print(numbers)
numbers[1:3] = 'wat?'
print(numbers)

# del and offset刪除項目
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
print(marxes[-1])
del marxes[-1]
print(marxes)
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
del marxes[1]
print(marxes)

# remove() and value刪除項目
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
marxes.remove('Chico')
print(marxes)

# pop() and offset刪除項目
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
print(marxes.pop())
print(marxes)
print(marxes.pop(1))
print(marxes)

# clear
work_quotes = ["Working hard?", "Hardly working!"]
print(work_quotes)
work_quotes.clear()
print(work_quotes)

# index() and value
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
print(marxes.index('Chico'))

# in 檢查項目是否存在
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
print('Groucho' in marxes)
print('Bob' in marxes)
words = ['a', 'deer', 'a' 'female', 'deer']
print('deer' in words)

# count() and value
marxes = ['Groucho', 'Chico', 'Harpo']
print(marxes.count('Harpo'))
snl_skit = ['cheeseburger', 'cheeseburger', 'cheeseburger']
print(snl_skit.count('cheeseburger'))

# join() list to string
marxes = ['Groucho', 'Chico', 'Harpo']
print(', '.join(marxes))
friends = ['Harry', 'Hermione', 'Ron']
separator = ' * '
joined = separator.join(friends)
print(joined)
separated = joined.split(separator)
print(separated)
print(separated == friends)

# sort() and sorted()
marxes = ['Groucho', 'Chico', 'Harpo']
sorted_marxes = sorted(marxes) 
print(sorted_marxes)
marxes.sort()
print(marxes)
numbers = [2, 1, 4.0, 3]
numbers.sort()
print(numbers)
numbers = [2, 1, 4.0, 3]
numbers.sort(reverse=True)
print(numbers)
a = [1, 2, 3]
b = a 
a[0] = 'surprise'
print(a)
print(b)
b[0] = 'I hate surprises'
print(a)
print(b)

# 用copy(), list()或slice來複製
a = [1, 2, 3]
b = a.copy()
c = list(a)
d = a[:]
print(f'a is {a},\n b is {b},\n c is {c},\n d is {d}')
a[0] = 'integer lists are boring'
print(f'a is {a},\n b is {b},\n c is {c},\n d is {d}')

# deepcopy()
a = [1, 2, [8, 9]]
b = a.copy()
c = list(a)
d = a[:]
print(f'a is {a},\n b is {b},\n c is {c},\n d is {d}')
a[2][1] = 10
print(f'a is {a},\n b is {b},\n c is {c},\n d is {d}')

import copy
a = [1, 2, [8, 9]]
b = copy.deepcopy(a)
print(f'a is {a},\n b is {b}')
a[2][1] = 10
print(f'a is {a},\n b is {b}')

# 比較list
a = [7, 2]
b = [7, 2, 9]
print(a == b)
print(a <= b)
print(a >= b)

# list - for and in
cheeses = ['brie', 'gjetost', 'havarti']
for cheese in cheeses:
    print(cheese)  
for cheese in cheeses:
    if cheese.startswith('g'):
        print("I won't eat anything that starts with 'g'")
        break
    else:
        print(cheese)
for cheese in cheeses:
    if cheese.startswith('x'):
        print("I won't eat anything that starts with 'g'")
        break
    else:
        print(cheese)
else:
    print('Didn\'t find anything that started with "x"')
cheeses = []
for cheese in cheeses:
    print('This shop has some lovely', cheese)
    break
else:
    print('This is not much of a cheese shop, is it?')

# zip()
days = ['Monday', 'Tuesday', 'Wednesday']
fruits = ['banana', 'orange', 'peach']
drinks = ['coffee', 'tea', 'beer']
desserts = ['tiramisu', 'ice cream', 'pie', 'pudding']
for day, fruit, drink, dessert in zip(days, fruits, drinks, desserts):
    print(f'{day}: drink {drink} - eat {fruit} - enjoy {dessert}')
english = 'Monday', 'Tuesday', 'Wednesday'
french = 'Lundi', 'Mardi', 'Mercredi'
print(list(zip(english, french)))
print(dict(zip(english, french)))

# 用生成式來建立串列
number_list = []
for i in range(5):
    number_list.append(i+1)
print(number_list)
number_list = [number for number in range(1,6)]
print(number_list)
number_list = [number-1 for number in range(1,6)]
print(number_list)
a_list = [number for number in range(1,6) if number % 2 == 1]
print(a_list)
a_list = []
for number in range(1, 6):
    if number % 2 == 1:
        a_list.append(number)
print(a_list)
rows = range(1, 4)
cols = range(1, 3)
for row in rows:
    for col in cols:
        print(row, col)
cells = [(row, col) for row in rows for col in cols]
for cell in cells:
    print(cell)
for row, col in cells:
    print(row, col)

# 串列的串列
small_birds = ['hummingbird', 'finch']
extinct_birds = ['dodo', 'passenger pigeon', 'Norwegian Blue']
carol_birds = [3, 'French hens', 2, 'turtledoves']
all_birds = [small_birds, extinct_birds, 'macaw', carol_birds]
print(all_birds)
print(all_birds[0])
print(all_birds[1])
print(all_birds[1][0])

# 7.1
years_list = []
n = 1996
while True:
    years_list.append(n)
    n += 1
    if n == 2001:
        print(years_list)
        print(f'The fifth birthday is {years_list[4]}')
        break

# 7.2
years_list.clear()
n = 1996
while True:
    years_list.append(n)
    n += 1
    if n == 2001:
        print(years_list)
        print(f'The third birthday is {years_list[2]}')
        break

# 7.3
max_year = 0
for year in years_list:
    if year > max_year:
        max_year = year
print(f'The oldest is {max_year}')

# 7.4
thins = ['mozzarella', 'cinderella', 'salmonella']
print(thins)

# 7.5
thins[1] = thins[1].capitalize()
print(thins)

# 7.6
thins[0] = thins[0].upper()
print(thins)

# 7.7
del thins[2]
print(thins)

# 7.8
surprise = ['Groucho', 'Chico', 'Harpo']
print(surprise)

# 7.9
surprise[-1] = surprise[-1].lower()
print(surprise)
for word in range(len(surprise[-1][::-1])):
    new_word = surprise[-1][::-1]
    print(new_word)
surprise[-1] = new_word.capitalize()
print(surprise)

#7.10
even = [number for number in range(10)]
print(even)

#7.11
start1 = ["fee", "fie", "foe"]
rhymes = [
    ("flop", "get a mop"),
    ("fope", "turn the rope"),
    ("fa", "get your ma"),
    ("fudge", "call the judge"),
    ("fat", "pet the cat"),
    ("fog", "walk the dog"),
    ("fun", "say we're done"),
]
start2 = "Someone better"
for i in range(len(start1)):
    print(f'{start1[i].capitalize()}! {rhymes[i][0].capitalize()}!')
    print(f'{start2} {rhymes[i][1]}.')

