class Book:
    def __init__(self, title, author, page_count):
        self.title = title
        self.author = author
        self.page_count = page_count

    def __str__(self):
        return f"'{self.title}' by {self.author}, {self.page_count} pages"

    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}', page_count={self.page_count})"

    def is_long(self):
        return self.page_count > 300
