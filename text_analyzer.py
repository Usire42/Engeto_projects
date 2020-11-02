
'''
author =
'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]

SEPARATOR = '-' * 40
USERS = {'bob': '123', 'ann': 'pass123', 'mike': 'password123', 'liz': 'pass123'}


print(SEPARATOR)
print('Welcome to the app. Please log in: ')
username = input('USERNAME: ').lower()
passwors = input('PASSWORD: ')
print(SEPARATOR)
#verificvation of username and password
if (username in USERS) and (passwors == USERS[username]):
    pass
else:
    print('Username or password  are incorrect')
    quit()

#Creates list of words without ' , . ? !'
print('We have 3 texts to be analyzed.')
user_text = int(input('Enter a number btw. 1 and 3 to select: ')) -1
simple_word = TEXTS[user_text].split()
clear_text = []
clear_text = [word.strip(' , . ? ! ') for word in simple_word]

#Counts the occurrence of words
i = 0
numbers = 0
sum_ = 0
upper_words = 0
lower_words = 0
capitalize_words = 0
word_count = len(clear_text)
len_words = []

for i in range(len(clear_text)):
    if clear_text[i].isnumeric():
        numbers += 1
        number = float(clear_text[i])
        sum_ += number
    elif clear_text[i].isupper():
        upper_words += 1
    elif clear_text[i].islower():
        lower_words += 1
    elif clear_text[i][0].isupper():
        capitalize_words += 1
    len_words.append(len(clear_text[i]))
print(SEPARATOR)
print(f'There are {word_count} words in the selected text.')
print(f'There are {capitalize_words} titlecase words')
print(f'There are {upper_words} uppercase words')
print(f'There are {lower_words} lowercase words')
print(f'There are {numbers} numeric strings')
print(SEPARATOR)

#Count frequency of different word lengths in the text
diff_word_count = {}

for diff_word in len_words:
    diff_word_count[diff_word] = diff_word_count.get(diff_word, 0) + 1

word_count_list = list(diff_word_count.items())
word_count_list.sort(reverse=True)

while word_count_list:
    word_graph = word_count_list.pop()
    print(f'{word_graph[0]} {"*" * word_graph[1]} {word_graph[1]}')

print(SEPARATOR)

print(f'If we summed all the numbers in this text we would get: {sum_}')

print(SEPARATOR)


