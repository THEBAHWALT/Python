#P.65
poem = 'There was a young lady named Norway'
print(poem)
poem2 = """
    I do not like thee, Doctor Fell.
    The reason why, I cannot tell.
    But this I know, and know full well:
    I do not like thee, Doctor Fell.
    """
print(poem2)
print('Give',"us",'''some''',"""space""")

#P.66
print(str(98.6))
print(str(1.0e4))
print(str(True))
palindrome = 'A man, \nA plan, \nA canal:\nPanama.'
print(palindrome)

#P.67
print('\tabc')
print('a\tbc')
print('ab\tc')
print('abc\t')

testimony = "\"I did nothing!\" he said. \"Not that either! Or the other thing.\""
print(testimony)
speech = 'The backslash (\\) escapes.'
print(speech)
info = r'Type a \n to get a new line in a string'
print(info)
poem = r'''Boys and girls, come out to play.
\n The moon doth shine as bright as day.'''
print(poem)
vowels = ('a', 'e', 'i', 'o', 'u')
print(vowels[0]+vowels[1]+vowels[2]+vowels[3]+vowels[4])
a = 'Duck.'
b = a
c = 'Grey Duck!'
print(a + b + c)

start = 'Na' * 4 + '\n'
middle = 'Hey' * 3 + '\n'
end = 'Goodbye.'
print(start + start + middle + end)

letters = 'abcdefghijklmnopqrstuvwxyz'
print(letters[0])

name = 'Henny'
new_name = name.replace('H', 'P')
print(new_name)

print(letters[:])
print(letters[20:])
print(letters[10:]) 
print(letters[12:15])  
print(letters[-3:])
print(letters[18:-3])
print(letters[-6:-2])
print(letters[::7])
print(letters[4:20:3])
print(letters[19::4])
print(letters[:21:5])
print(letters[::-1])
print(letters[-50:])
print(letters[-51:-50])
print(letters[:70])
print(letters[70:71])
print(len(letters))
empty = ''
print(len(empty))   

#split()
tasks = 'get gloves,get mask,give cat vitamins,call ambulance'
print(tasks.split(','))
print(tasks.split())

#join()
crypto_list = ['Yeti', 'Bigfoot', 'Loch Ness Monster']
crypto_string = ', '.join(crypto_list)
print('Found and signing book deals:', crypto_string)   

#replace()
setup = "a duck goes into a bar..."
print(setup.replace('duck','marmoset'))
print(setup.replace('a ','a famous ',100))

#strip()
world = '  earth  '
world.strip()
print(world)
world = '  earth  '
world.strip(' ')
print(world)
world.lstrip()
print(world)   
blurt = "What the...!!?"
print(blurt.strip('.!?'))

#search
poem = """All that doth flow we cannot liquid name
Or else would fire and water be the same;
But that is liquid which is moist and wet
Fire that property can never get.
Then 'tis not cold that doth the fire put out
But 'tis the wet that makes it die, no doubt."""
print(poem[:13])
print(len(poem))
print(poem.startswith('All'))
print(poem.endswith('That\'s all, folks!'))
word = 'the'
print(poem.find(word))
print(poem.index(word))
print(poem.rfind(word))
print(poem.rindex(word))
print(poem.count(word))
print(poem.isalnum())

#大小寫
setup = 'a duck goes into a bar...'
print(setup.strip('.'))
print(setup.capitalize())
print(setup.title())
print(setup.upper())
print(setup.lower())
print(setup.swapcase())

#對齊方式
setup.center(30)
print(setup.center(30))
print(setup.ljust(30))
print(setup.rjust(30))

#新式f-strings
thing = 'wereduck'
place = 'werepond'
print(f'The {thing} is in the {place}.')
print(f'The {thing.capitalize()} is in the {place.rjust(20)}.')
print(f'The {thing:>20} is in the {place:.^20}.')
print(f'{thing = }, {place = }')
print(f'{thing[-4:] = }, {place.title() = }')
print(f'{thing = :>4.4}')

#excercise 5.1
song = """When an eel grabs your arm,
And it causes great harm,
That's - a moray!"""
print(song.replace(' m', ' M'))

#excercise 5.2
questions = [
    "We don't serve strings around here. Are you a string?",
    "What is said on Father's Day in the forest?",
    "What makes the sound 'Sis! Boom! Bah!'?"
    ]
answers = [
    "An exploding sheep.",
    "No, I'm a frayed knot.",
    "'Pop!' goes the weasel."
    ]
print('Q: ', questions[0])
print('A: ', answers[1])
print('Q: ', questions[1])
print('A: ', answers[2])
print('Q: ', questions[2])
print('A: ', answers[0])

#excercise 5.4 and 5.5
salutation = 'Mr.'
name = 'Cindy'
product = 'potato chips'
verbed = 'exploded'
room = 'bag'
animals = 'dogs'
amount = '$99,999'
percent = '99%'
spokesman = 'Mr. Walter'
job_title = 'Dogs'
print(f"""Dear {salutation} {name},
      
    Thank you for your letter. We are sorry that our {product} 
    {verbed} in your {room}. Please note that it should never 
    be used in a {room}, especially near any {animals}.
        
    Send us your receipt and {amount} for shipping and handling.
    We will send you another {product} that, in our tests,
    is {percent}% less likely to have {verbed}.
      
    thank you for your support.
    Sincerely,
    {spokesman}
    {job_title}""")

#exercise 5.6
boat_name = 'duck'
horse_name = 'gourd'
Train_name = 'spitz'
print(f"""根據調查，大家喜歡用這種格式來命名：英國潛水艇{boat_name}、澳洲賽馬{horse_name}、瑞典火車{Train_name}""")
