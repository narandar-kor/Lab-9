class Book():
    def __init__(self,title,author):
        self.title = title
        self.author = author
    def display_info(self):
        print(f"""The title of this book is -> {self.title}
And the author of this book is -> {self.author} \n""")


book1 = Book("Rich Dad poor Dad","Robert kiyosaki")
book2 = Book("Atomic Habits","james Clear")
book3 = Book("A brief History of Time","Stephen Hawking")

book1.display_info()
book2.display_info()
book3.display_info()