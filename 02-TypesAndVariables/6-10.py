movie = "The Lord of the Rings: The Return of the King"

# print number of characters
print('Number of characters: ', len(movie))

# print title in capital letters
big_title = movie.upper()
print(f'Title in capital letter: {big_title}')

# print title in small letters
small_title = movie.lower()
print(f'Small title: {small_title}')

# print how many times the vowel "e" appears in the title
litera = "e"
print(f'Litera e w tytule występuje {movie.count(litera)}')

# print where in the text is the word "Lord"
print(f'The word Lord exsists on {movie.find("Lord")} position')

# print where in the text is the word "dragon"
print(f'The word DRAGON is on {movie.find("dragon")} position')