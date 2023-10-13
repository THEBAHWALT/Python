#P.59-P.61
letter = 'o'
if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
    print(letter, "is a vowel")
else:
    print(letter, "is not a vowel")

"""
vowels = 'aeiou'
letter = 'o'
if letter in vowels:
    print(letter, "is a vowel")
"""

vowels_set = {'a', 'e', 'i', 'o', 'u'}
if letter in vowels_set:
    print(letter, "is a under vowel_set") 
vowels_list = ['a', 'e', 'i', 'o', 'u']
if letter in vowels_list:
    print(letter, "is a under vowel_list")
vowels_tuple = ('a', 'e', 'i', 'o', 'u')
if letter in vowels_tuple:
    print(letter, "is a under vowel_tuple")
vowels_dict = {'a':1, 'e':2, 'i':3, 'o':4, 'u':5}
if letter in vowels_dict:
    print(letter, "is a under vowel_dict")
first_vowel_value = vowels_dict.get(letter[0])
if first_vowel_value:
    print("first_vowel_value is on the dict of the place ", first_vowel_value)

tweet_limit = 280
tweet_string = 'I got a huge python' * 50
diff = tweet_limit - len(tweet_string)
if diff >= 0:
    print("A fitting tweet")
    print(diff, "characters left")
else:
    print("Went over by ", abs(diff))

#excercise 4.1
secret = 7
guess = 7
if guess < secret:
    print("too low")
elif guess > secret:
    print("too high")
else:
    print("just right")

#excercise 4.2
small = True
green = False
if small:
    if green:
        print("pea")
    else:
        print("cherry")
else:
    if green:
        print("watermelon")
    else:
        print("pumpkin")

