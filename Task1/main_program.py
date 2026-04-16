import tkinter as tk
from library_system import Books, BorrowBook
from interface import bookListPanel, BorrowPanel

class LibraryUI:    
    def __init__(self, root):
        self.root = root
        self.root.title("Library management system")
        self.root.geometry("1280x720")
        
        self.lfile = Books('booklist.txt')     #initializing these classes to show the data in the files
        self.Bfile = BorrowBook("Borrowlog.txt")

        
        self.booklist = tk.LabelFrame(self.root, text="Book Records", padx=10, pady=10)
        self.booklist.pack(side=tk.LEFT, fill="both", expand=True, padx=10, pady=10)
        
        self.borrowrecord = tk.LabelFrame(self.root, text="Borrow Records", padx=10, pady=10)
        self.borrowrecord.pack(side=tk.RIGHT, fill="both", expand=True, padx=10, pady=10)
        
        self.leftpanel = bookListPanel(self.booklist, self.lfile)
        self.leftpanel.UIsettings()
        self.rightpanel = BorrowPanel(self.borrowrecord, self.lfile, self.Bfile, self.leftpanel)
        self.rightpanel.UIsettings()            



if __name__ == "__main__":
    UI = tk.Tk()
    window = LibraryUI(UI)
    UI.mainloop()