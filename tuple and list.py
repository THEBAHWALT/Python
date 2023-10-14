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


