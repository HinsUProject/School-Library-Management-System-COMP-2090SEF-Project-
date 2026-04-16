import tkinter as tk

class Library:
    total = 0  #class attribute, track the number of books in the library
    def __init__(self, BID, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre
        self.BID = BID 
    def UIsettings(self):       #abstraction
        pass
        
class Books(Library):
    def __init__(self,fname):
        self.fname = fname
        
    @staticmethod
    def check_bid(bid):          #check is the BID a valid id or not
        if bid[0] == 'B' and bid[1:].isdigit():        #BID must be in "BXXX" format, where X is number.
            return True
        else:
            return False
        return True
    @classmethod
    def total_status(cls,booklist):     #use classmethod to show total status of books
        available = 0
        borrowed = 0
        for i in booklist:
            detail = i.split('|')      
            status = detail[4].strip()
            if status == "Available":     #count the number of borrowed and available books
                available = available +1
            elif status == "Borrowed":
                borrowed = borrowed + 1
        return f"Total: {cls.total} Available: {available} Borrowed: {borrowed}"
    def ReadBook(self):         #show all books and the info
        fread = open(self.fname, 'r')
        booklist = fread.readlines()
        booklist = [book.strip() for book in booklist]
        Library.total = len(booklist)
        fread.close()
        return booklist
    
    def AddBook(self, BID, title, author, genre): 
        newbook = BID + '|' + title + '|' + author + '|' + genre + '|' + 'Available' + '\n'
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

    def UpdateStatus(self, BID, status):
        lines = self.ReadBook()
        updatedList = []
        for i in lines:
            details = i.split('|')
            if details[0] == BID:
                # Keep everything but change the 4th index (Status)
                details[4] = status
                updatedList.append("|".join(details) + "\n")
            else:
                updatedList.append(i + "\n")
        fin = open(self.fname, 'w')
        fin.writelines(updatedList)
        fin.close()
    
class BorrowBook(Library):    
    def __init__(self, fname):
        self.fname = fname
    
    def Borrow(self, action, BID, SID):
        newBorrow = BID+"|"+SID
        fin = open(self.fname, 'a')
        fin.write(action+": "+newBorrow+"\n")
        fin.close()

    def Readlog(self):
        fin = open(self.fname, 'r')
        borrowList = fin.readlines()
        fin.close()
        return borrowList