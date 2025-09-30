class Book:
    book_lan = "English"
    count = 0
    def __init__(self,bid,bname,price,author):
        Book.count +=1
        self.id = bid
        self.name = bname
        self.price = price
        self.author = author

    def showBook(self):
        print("BOOK ID : ",self.id)
        print("NAME: ",self.name)
        print("PRICE: ",self.price)
        print("AUTHOR: ",self.author)
        print("BOOK LANGUAGE: ",Book.book_lan)
    
    def total_Book():
        print("Total_book : ",Book.count)

b1 = Book(101,"Atomic Habits ",150,"James Clear")
b1.showBook()

Book.total_Book()

        