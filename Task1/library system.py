class Library:
    def __init__(self, BID, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre
        self.BID = BID
class Books(Library):
    def __init__(self,fname):
        self.fname = fname
        
    def ReadBook(self):
        fread = open(self.fname, 'r')
        booklist = fread.readlines()
        booklist = [book.strip() for book in booklist]
        fread.close()
        print(booklist)
        return booklist
    
    def AddBook(self, BID, title, author, genre):
        newbook = BID + '|' + title + '|' + author + '|' + genre + '\n'
        fadd = open(self.fname,'a')
        fadd.write(newbook)
        fadd.close()
    
    def DelBook(self, BID):
        fread = open(self.fname, 'r')
        temp_booklist = fread.readlines()
        temp_booklist = [book.strip() for book in temp_booklist]
        fread.close()
        new_booklist = []
        for book in temp_booklist:
            if BID in book:
                continue
            new_booklist.append(book+'\n')
        fdel = open(self.fname, 'w')
        fdel.writelines(new_booklist)
        fdel.close()
        
class BorrowBook(Library):
    def __init__(self, fname):
        self.fname = fname
    
    def Borrow(self, BID, SID):
        newBorrow = BID+"|"+SID
        fin = open(self.fname, 'a')
        fin.write("Borrow|"+newBorrow+"\n")
        fin.close()

class ReturnBook(Library):
    def __init__(self, fname):
        self.fname = fname

    def Return(self, BID, SID):
        newReturn = BID+"|"+SID
        fin = open(self.fname, 'a')
        fin.write("Return|"+newReturn+"\n")
        fin.close()
        
if __name__ == "__main__":
    lfile = Books('booklist.txt')
    lfile.ReadBook()
    lfile.AddBook('B004', 'Book4', 'author4', 'genre4')
    lfile.ReadBook()
    lfile.DelBook('B001')
    lfile.ReadBook()
    Bfile = BorrowBook("Borrowlog.txt")
    Bfile.Borrow("B123", "S456")
    Rfile = ReturnBook("Borrowlog.txt")
    Rfile.Return("R123","S456")
