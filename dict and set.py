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
