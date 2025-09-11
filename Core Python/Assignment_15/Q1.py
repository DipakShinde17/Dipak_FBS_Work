#1. Create a class Book with members as bid,bname,price and author.Add following methods:
# a. Constructor (Support both parameterized and parameterless)
# b. Destructor
# c. ShowBook

class book():
    def __init__(self,bid,bname,price,author):
        self.id = bid
        self.name = bname
        self.price = price
        self.author = author

    def showbook(self):
        print("--------book details-----------")
        print("bid:",self.id)
        print("bname:",self.name)
        print("price:",self.price)
        print("author:",self.author)
        print("----------------------")

    def __del__(self):
        print("distructor")

b1 = book(101,"shamchi aai",140,"sane guruji")
b1.showbook()

    