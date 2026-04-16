import tkinter as tk
from tkinter import messagebox
from library_system import Library, Books

class bookListPanel(Library):
    def __init__(self, frame, lfile):
        self.frame = frame
        self.lfile = lfile
        self.count = 0
    def UIsettings(self):
        all_books = self.lfile.ReadBook()
        overall_status = Books.total_status(all_books)
        self.counter = tk.Label(self.frame, text = overall_status)
        self.counter.pack(pady=5)
        
        input_frame = tk.Frame(self.frame)
        input_frame.pack(fill="x", pady=10)
        tk.Label(input_frame, text="BID:").grid(row = 0, column= 0)
        self.addbid = tk.Entry(input_frame)
        self.addbid.grid(row = 0, column = 1, padx =5)
        tk.Label(input_frame, text="Title:").grid(row = 0, column = 2, padx = 5)
        self.addtitle = tk.Entry(input_frame)
        self.addtitle.grid(row = 0, column=3, padx=5)
        tk.Label(input_frame, text = "Author:").grid(row = 0, column = 4, padx = 5)
        self.addauthor = tk.Entry(input_frame)
        self.addauthor.grid(row = 0, column=5, padx=5)
        tk.Label(input_frame, text = "Genre:").grid(row = 0, column = 6, padx = 5)
        self.addgenre = tk.Entry(input_frame)
        self.addgenre.grid(row=0, column =7, padx = 5)
        tk.Button(input_frame, text = "Add book", command=self.booksUI).grid(row=2, column=4, pady=10)
        self.displayrecord = tk.Frame(self.frame)
        self.displayrecord.pack(fill="both", expand=True)
        self.showrecords()

    def showrecords(self):
        for i in self.displayrecord.winfo_children():
            i.destroy()
        category = ["BID", "Title", "Author", "Genre", "Status", "Delete"]
        for i, text in enumerate(category):
            tk.Label(self.displayrecord, text=text, width=15).grid(row=0, column=i)
        bookdata = self.lfile.ReadBook()            #grab data from the file
        overall_status = Books.total_status(bookdata)
        if self.counter: # keep datinng the count of books
            update_status = Books.total_status(bookdata)
            self.counter.config(text = update_status)
        for rowindex, line in enumerate(bookdata, start=1):
            details = line.split('|')
            BID = details[0]
            for columnindex, value in enumerate(details):
                tk.Label(self.displayrecord, text=value, width=15).grid(row=rowindex, column=columnindex)
                
            def deletebook(target = BID):
                self.lfile.DelBook(target)
                self.showrecords()
                messagebox.showinfo("Success", "The book has been removed")
            tk.Button(self.displayrecord, text="Delete" ,command = deletebook).grid(row=rowindex, column=5, padx=5)

    def booksUI(self):
        title = self.addtitle.get()
        author = self.addauthor.get()
        genre = self.addgenre.get()
        bid = self.addbid.get()
        if Books.check_bid(bid):
            if all([bid, title, author, genre]):
                if self.checkbook(bid) == False:
                    self.lfile.AddBook(bid, title, author, genre)
                    self.showrecords()
                    self.addtitle.delete(0, tk.END)
                    self.addauthor.delete(0, tk.END)
                    self.addgenre.delete(0, tk.END)
                    self.addbid.delete(0, tk.END)
                    messagebox.showinfo("Success", "Book added to list")
                else:
                    messagebox.showinfo("Failed", "This book id is occupied")
            else:
                messagebox.showwarning("Failed", "Please fill every data")
        else:
            messagebox.showwarning("Error", "BID must start with B and follows by number")
    def checkbook(self, bid):
        booklist = self.lfile.ReadBook()
        for i in booklist:
            details = i.split("|")
            details[0].strip()
            if details[0] == bid:
                return True
        return False

class BorrowPanel(Library):
    def __init__(self, frame, booklisthandle, loghandle, leftpanel):
        self.frame = frame
        self.booklisthandle = booklisthandle
        self.loghandle = loghandle
        self.leftpanel = leftpanel
    def UIsettings(self):
        # Entry fields for Borrowing
        tk.Label(self.frame, text="Book ID (BID):").pack(pady=(10, 0))
        self.bidInputBox = tk.Entry(self.frame)
        self.bidInputBox.pack(pady=5)
        
        tk.Label(self.frame, text="Student ID (SID):").pack(pady=(10, 0))
        self.sidInputBox = tk.Entry(self.frame)
        self.sidInputBox.pack(pady=5)
        
        # Action Buttons
        btnFrame = tk.Frame(self.frame)
        btnFrame.pack(pady=20)
        
        tk.Button(btnFrame, text="Borrow Book", width=15, 
                  command=lambda: self.process("Borrow")).pack(side=tk.LEFT, padx=5)
        tk.Button(btnFrame, text="Return Book", width=15, 
                  command=lambda: self.process("Return")).pack(side=tk.LEFT, padx=5)

        tk.Label(self.frame, text="Transaction History:", font=('Arial', 9, 'bold')).pack(anchor='w')
        self.borrowLog = tk.Text(self.frame, height=12, state='disabled', font=('Consolas', 9))
        self.borrowLog.pack(fill="both", expand=True)
        self.update_log()

    def checkstatus(self, bid):
        fin = open("booklist.txt", "r")
        booklists = fin.readlines()
        for i in booklists:
            eachbook = i.split("|")
            if eachbook[0] == bid:
                eachbook[4] = eachbook[4].strip()
                if eachbook[4] == "Available":
                    return True
                else:
                    return False            
        fin.close()
        return "NotFound"
    
    def checkstd(self, bid, sid):
        fin = open("Borrowlog.txt","r")
        loglist = fin.readlines()
        isstudent = False
        for i in loglist:
            record = i.strip().split("|")
            if record[1] == sid.strip():
                if record[0] == ("Return: ")+bid:
                    isstudent = False
                elif record[0] == ("Borrow: ")+bid:
                    isstudent = True
        fin.close()
        return isstudent
    
    def process(self, action):
        bid = self.bidInputBox.get()   #book id inputted
        sid = self.sidInputBox.get()   #student id inputted
        bookstatus = self.checkstatus(bid)
        isstudent = self.checkstd(bid, sid)
        if bid and sid:
            if action == "Borrow":
                if bookstatus == False:
                    messagebox.showwarning(message="This book has been borrowed!")
                elif bookstatus == "NotFound":
                    messagebox.showwarning(message="This book does not exist!")
                else:
                    self.loghandle.Borrow(action, bid, sid)
                    self.booklisthandle.UpdateStatus(bid, "Borrowed")
                    self.refresh()
                    
            else:
                if bookstatus == True:
                    messagebox.showwarning(message="This book is not borrowed!")
                elif bookstatus == "NotFound":
                    messagebox.showwarning(message="This book does not exist!")
                else:
                    if isstudent == True:    
                        self.loghandle.Borrow(action, bid, sid)
                        self.booklisthandle.UpdateStatus(bid, "Available")
                        self.refresh()
                    
                    else:
                        messagebox.showwarning(message="This book is not borrowed by this student!")


        else:
            messagebox.showwarning(message="Please Enter both IDs!")

    def refresh(self):
        """Refreshes both UI panels and clears inputs"""
        self.update_log() # Refresh the borrow log
        self.leftpanel.showrecords() # Refresh the book list UI
        self.bidInputBox.delete(0, tk.END)
        self.sidInputBox.delete(0, tk.END)

    def update_log(self):
        self.borrowLog.config(state='normal')
        self.borrowLog.delete('1.0', tk.END)
        for i in self.loghandle.Readlog():
            self.borrowLog.insert(tk.END, i.replace("|","->"))
        self.borrowLog.config(state='disabled')
