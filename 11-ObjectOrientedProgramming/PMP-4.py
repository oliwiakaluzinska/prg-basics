class Ebook:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        self.page_number = 1
        self.is_open = False
    
    def open(self):
        self.is_open = True

    def close(self):
        self.is_open = False

    def book_status(self):
        if self.is_open:
            print('Book is open')
            print(f'Title: {self.title}\nAuthor: {self.author}\nNumber of pages: {self.pages}\nCurrent page number: {self.page_number}')
        else:
            print('Book is closed')

    def change(self):
        if self.is_open and self.page_number < self.pages:
          self.page_number += 1
        else:
            print('The book is closed, not possible')

def main():
    ebook = Ebook('Lalka','Bolesław Prus', 300)
    ebook.open()
    ebook.book_status()
    ebook.change()
    ebook.change()
    ebook.change()
    ebook.change()
    ebook.book_status()
    ebook.close()
    ebook.book_status()
    ebook.change()
main()
    