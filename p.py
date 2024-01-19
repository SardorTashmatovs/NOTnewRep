class Book:
    def __init__(self, title, creator, year):
        self.title = title
        self.creator = creator
        self.year = year

    def info(self):
        print(f"{self.title}")
        print(f"{self.creator}")
        print(f"{self.year}")

book1 = Book("a", "b", 1999)

book1.info()
