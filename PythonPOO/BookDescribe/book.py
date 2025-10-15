class Book:
    def __init__(self, title: str, author: str, page_number: int) -> None:
        self.title = title.capitalize()
        self.author = author.capitalize()
        self.page_number = page_number
    
    def show_book_describe(self):
        return f' The book {self.title} have the author {self.author} and have {self.page_number} pages.'
