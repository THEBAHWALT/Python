# 用{}來建立
empty_dict = {}
print(empty_dict)
bierce = {
    "day": "A period of twenty-four hours, mostly misspent",
    "positive": "Mistaken at the top of one's voice",
    "misfortune": "The kind of fortune that never misses",
}
print(bierce)

# 用dict()來建立
acme_customer = {'first': 'Wile', 'middle': 'E', 'last': 'Coyote'}
print(acme_customer)
acme_customer = dict(first='Wile', middle='E', last='Coyote')
print(acme_customer)

# 用dict()來轉換
lol = [['a', 'b'], ['c', 'd'], ['e', 'f']] 
print(dict(lol)) 
lot = [('a', 'b'), ('c', 'd'), ('e', 'f')] 
print(dict(lot))
tol = (['a', 'b'], ['c', 'd'], ['e', 'f'])
print(dict(tol))

# 用[鍵]來加入或改變一個項目
pythons = {
    'Chapman': 'Graham',
    'Cleese': 'John',
    'Idle': 'Eric',
    'Jones': 'Terry',
    'Palin': 'Michael',
}
print(pythons)
pythons['Gilliam'] = 'Gerry'
print(pythons)
pythons['Gilliam'] = 'Terry'
print(pythons)
some_pythons = {
    'Graham': 'Chapman',
    'John': 'Cleese',
    'Eric': 'Idle',
    'Terry': 'Gilliam',
    'Michael': 'Palin',
    'Terry': 'Jones',
}
print(some_pythons)
print(some_pythons['John'])
print('Groucho' in some_pythons)
print(some_pythons.get('John'))
print(some_pythons.get('Groucho', 'Not a Python'))
print(some_pythons.get('Groucho'))

# 用keys()來取得所有的鍵
signals = {'green': 'go', 'yellow': 'go faster', 'red': 'smile for the camera'}
print(signals.keys())
print(list(signals.keys()))

# 用values()來取得所有的值
print(list(signals.values()))

# 用items()來取得所有的鍵/值
print(list(signals.items()))

# 用{**a, **b}來結合字典
first = {'a':'agony', 'b':'bliss'}
second = {'b':'bagels', 'c':'candy'}
print({**first, **second})
thied = {'d':'donuts'}
print({**first, **second, **thied})

# update()來結合字典
pythons = {
    'Chapman': 'Graham',
    'Cleese': 'John',
    'Gilliam': 'Terry',
    'Idle': 'Eric',
    'Jones': 'Terry',
    'Palin': 'Michael',
}
print(pythons)
others = {'Marx': 'Groucho', 'Howard': 'Moe'}
pythons.update(others)
print(pythons)
first = {'a':1, 'b':2}
second = {'b':'platypus'}
first.update(second)
print(first)

# 用del和鍵來刪除項目
del pythons['Marx']
print(pythons)
del pythons['Howard']
print(pythons)

# 用pop()和鍵取得項目並刪除他
print(len(pythons))
print(pythons.pop('Palin'))
print(len(pythons))
print(pythons.pop('First', 'Hugo'))
print(len(pythons))

# clear()來刪除所有的項目
pythons.clear()
print(len(pythons))

# 用in來檢查鍵是否存在
pythons = {'Chapman': 'Graham', 'Cleese': 'John', 'Jones': 'Terry', 'Palin': 'Michael'}
print('Chapman' in pythons)
print('Palin' in pythons)

# 用=來賦值
signals = {'green': 'go', 'yellow': 'go faster', 'red': 'smile for the camera'}
save_signals = signals
signals['blue'] = 'confuse everyone'
print(save_signals)
print(signals)

# 用copy()來複製
signals = {'green': 'go', 'yellow': 'go faster', 'red': 'smile for the camera'}
original_signals = signals.copy()
signals['blue'] = 'confuse everyone'
print(original_signals)
print(signals)

# 用deepcopy()來複製
signals = {'green': 'go', 'yellow': 'go faster', 'red': ['stop', 'smile']}
signals_copy = signals.copy()
print(signals)
print(signals_copy)
signals['red'][1] = 'sweat'
print(signals)
print(signals_copy)
import copy
signals = {'green': 'go', 'yellow': 'go faster', 'red': ['stop', 'smile']}
print(signals)
signals_copy = copy.deepcopy(signals)
print(signals)
print(signals_copy)
signals['red'][1] = 'sweat'
print(signals)
print(signals_copy)

# 比較dict
a = {1:1, 2:2, 3:3}
b = {3:3, 1:1, 2:2}
print(a == b)

a = {1:[1,2], 2:[1,2], 3:[1,2]}
b = {3:[1,1], 1:[1,2], 2:[1,2]}
print(a == b)

# 用for與in來迭代
accusation = {'room': 'ballroom', 'weapon': 'lead pipe', 'person': 'Col. Mustard'}
for card in accusation:
    print(card)
for value in accusation.values():
    print(value)
for item in accusation.items():
    print(item)
for card, contents in accusation.items():
    print('Card', card, 'has the contents', contents)

# dict生成式
# {key_expression: value_expression for expression in iterable}
word = 'letters'
letter_counts = {letter: word.count(letter) for letter in word}
print(letter_counts)
word = 'letters'
letter_counts = {letter: word.count(letter) for letter in set(word)}
print(letter_counts)
# {key_expression: value_expression for expression in iterable if condition}
vowels = 'aeiou'
word = 'onomatopoeia'
vowels_counts = {letter: word.count(letter) for letter in set(word) if letter in vowels}
print(vowels_counts)

# 用set()來建立
empty_set = set()
even_numbers = {0, 2, 4, 6, 8}
odd_numbers = {1, 3, 5, 7, 9}

# 用set()來轉換
print(set('letters'))
print(set(['Dasher', 'Dancer', 'Prancer', 'Mason-Dixon']))
print(set(('Ummagumma', 'Echoes', 'Atom Heart Mother')))
print(set({'apple': 'red', 'orange': 'orange', 'cherry': 'red'}))

# 用len()來取得長度
reindeer = set(['Dasher', 'Dancer', 'Prancer', 'Mason-Dixon'])
print(len(reindeer))

# 用add()來加入一個項目
s = set((1,2,3))
print(s)
s.add(4)
print(s)

# 用remove()來刪除項目
s = set((1,2,3))
s.remove(3)
print(s)

# 用for in來迭代
furniture = set(('sofa', 'ottoman', 'table'))
for piece in furniture:
    print(piece)

# 用in來檢查是否存在
drinks = {
    'martini': {'vodka', 'vermouth'},
    'black russian': {'vodka', 'kahlua'},
    'white russian': {'cream', 'kahlua', 'vodka'},
    'manhattan': {'rye', 'vermouth', 'bitters'},
    'screwdriver': {'orange juice', 'vodka'},
}
for name, contents in drinks.items():
    if 'vodka' in contents:
        print(name)
for name, contents in drinks.items():
    if 'vodka' in contents and not ('vermouth' in contents or 'cream' in contents):
        print(name)

# 組合與運算子
for name, contents in drinks.items():
    if contents & {'vermouth', 'orange juice'}:
        print(name)

for name, contents in drinks.items():
    if 'vodka' in contents and not contents & {'vermouth', 'cream'}:
        print(name)
bruss = drinks['black russian']
wruss = drinks['white russian']
print(bruss & wruss)
a = {1, 2}
b = {2, 3}
print(a & b)
print(a.intersection(b))
print(a | b)
print(a.union(b))
print(bruss | wruss)
print(a - b)
print(a.difference(b))
print(bruss - wruss)
print(wruss - bruss)
print(a ^ b)
print(a.symmetric_difference(b))
print(bruss ^ wruss)
print(a <= b)
print(a.issubset(b))
print(bruss <= wruss)
print(a <= a)
print(a.issubset(a))
print(a < b)
print(a < a)
print(a >= b)
print(a.issuperset(b))
print(wruss >= bruss)
print(a >= a)
print(a.issuperset(a))
print(a > b)
print(wruss > bruss)
print(a > a)

# 集合生成式
# { expression for expression in iterable }
# { expression for expression in iterable if condition }
a_set = {number for number in range(1, 6) if number % 3 == 1}
print(f'a_set = {a_set}')

# 用frozenset()建立不可變集合
print(frozenset([3, 2, 1]))
print(frozenset(set([3, 2, 1])))
print(frozenset({3, 2, 1}))
print(frozenset((2, 3, 1)))

fs = frozenset([3, 2, 1])
print(f'fs = {fs}')
# fs.add(4) print(f'fs = {fs}') # AttributeError: 'frozenset' object has no attribute 'add'

# 截至目前為止的資料結構
marx_list = ['Groucho', 'Chico', 'Harpo']
marx_tuple = 'Groucho', 'Chico', 'Harpo'
marx_dict = {'Groucho': 'banjo', 'Chico': 'piano', 'Harpo': 'harp'}
marx_set = {'Groucho', 'Chico', 'Harpo'}
print(f'marx_list[2] = {marx_list[2]}')
print(f'marx_tuple[2] = {marx_tuple[2]}')
print(f'marx_dict["Harpo"] = {marx_dict["Harpo"]}')
print('Harpo' in marx_set)
print('Harpo' in marx_dict)
print('Harpo' in marx_tuple)
print('Harpo' in marx_list)

# 製造更大型的資料結構
marxes = ['Groucho', 'Chico', 'Harpo']
pythons = ['Chapman', 'Cleese', 'Gilliam', 'Jones', 'Palin']
stooges = ['Moe', 'Curly', 'Larry']
tuple_of_lists = marxes, pythons, stooges
print(tuple_of_lists)
list_of_lists = [marxes, pythons, stooges]
print(list_of_lists)
dict_of_lists = {'Marxes': marxes, 'Pythons': pythons, 'Stooges': stooges}
print(dict_of_lists)
houses = {
    (44.79, -93.14, 285): 'My House',
    (38.89, -77.03, 13): 'The White House',
}
print(houses)

# 8.1
e2f = {'dog':'chien', 'cat':'chat', 'walrus':'morse'}
print(e2f)

# 8.2
print(e2f['walrus'])

# 8.3
f2e = {}
for english, french in e2f.items():
    f2e[french] = english
print(f2e)

# 8.4
print(f2e['chien'])

# 8.5
print(set(e2f.keys()))

# 8.6
life = {
    'animals': {
        'cats': [
            'Henri', 'Grumpy', 'Lucy'
        ],
        'octopi': {},
        'emus': {},
    },
    'plants': {},
    'other': {},
}

# 8.7
print(life.keys())

# 8.8
print(life['animals'].keys())

# 8.9
print(life['animals']['cats'])

# 8.10
squares = {number: number * number for number in range(10)}
print(squares)

# 8.11
odd = {number for number in range(10) if number % 2 == 1}
print(odd)

# 8.12
for thing in ('Got %s' % number for number in range(10)):
    print(thing)

# 8.13
keys = ('optimist', 'pessimist', 'troll')
values = ('The glass is half full', 'The glass is half empty', 'How did you get a glass?')
print(dict(zip(keys, values)))

# 8.14
titles = ['Creature of Habit', 'Crewel Fate']
plots = ['A nun turns into a monster', 'A haunted yarn shop']
print(dict(zip(titles, plots)))