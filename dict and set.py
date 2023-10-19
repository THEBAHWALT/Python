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