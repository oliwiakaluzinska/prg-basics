def number_of_files(text):
    with open(text, 'r', encoding="utf-8") as file:
        lines = file.readlines()
    
    sum = 0 
    for i in range(len(lines)):
        sum += 1
    return sum

print(number_of_files('healthy_lifestyle.txt'))

def number_of_characters(text):
    with open(text, 'r', encoding="utf-8") as file:
        characters = file.read()
    return len(characters)

print(number_of_characters('healthy_lifestyle.txt'))

import re
def number_of_words(text):
    with open(text, 'r', encoding='utf-8') as file:
        words = file.read()

    clean_text = re.sub(r'[^\w\s]', '', words)
    words = clean_text.split()
    return len(words)

print(number_of_words('healthy_lifestyle.txt'))
