translations = {
   'computer': 'komputer',
   'mouse': 'myszka',
   'keyboard': 'klawiatura',
   'printer': 'drukarka'
}
english = input('Enter english word: ')
if english in translations:
    print(translations[english])
else:
    print('Word is not on the list')