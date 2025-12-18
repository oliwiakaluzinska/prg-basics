import csv

# 1️⃣ Funkcja wczytująca książki z CSV
def read_books(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return list(csv.DictReader(file))


# 2️⃣ Funkcja zapisująca książki danego gatunku do pliku
def save_books_by_genre(books, genre, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        for book in books:
            if book['Genre'] == genre:
                file.write(f"{book['Title']},{book['Author']},{book['Year']}\n")


# 3️⃣ Funkcja główna – rozdziela książki do plików
def split_books_by_genre(input_file):
    books = read_books(input_file)

    genre_files = {
        "Fantasy": "books_fantasy.txt",
        "Historical": "books_historical.txt",
        "Romance": "books_romance.txt",
        "Classic": "books_classic.txt"
    }

    for genre, filename in genre_files.items():
        save_books_by_genre(books, genre, filename)


# uruchomienie programu
split_books_by_genre("books.csv")