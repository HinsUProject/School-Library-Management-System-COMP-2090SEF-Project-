import tkinter as tk
from tkinter import messagebox, scrolledtext

class Graph:
    def __init__(self):
        self.adj_list={}
    def add_node(self,node):
        if node not in self.adj_list: #to avoid overwriting last record
            self.adj_list[node]=[]
    def add_edge(self, node1, node2):
        self.add_node(node1)
        self.add_node(node2)
        if node2 not in self.adj_list[node1]:
            self.adj_list[node1].append(node2)
        if node1 not in self.adj_list[node2]:
            self.adj_list[node2].append(node1)
    def get_related(self,node):
        return self.adj_list.get(node,[])
    def get_records(self):
        output = ''
        for node, related in self.adj_list.items():
            output = output + f"{node} -> {str(related)}\n"
        return output
    ##building drawing graph and get graph info
    ##========================================================##
    ##DFS algorithm
    def dfs(self,start_node):
        stack=[start_node]
        searched=set()
        while stack:
            now=stack.pop()
            if now not in searched:
                searched.add(now)  ## set searched
                for related in self.get_related(now):
                    if related not in searched:
                        stack.append(related)
                        #if related add in list
        return searched
#UI building
class LibraryUI:
    def __init__(self, root):
        self.libraryGraph = Graph()
        self.root = root
        self.root.title("School Library Management System (Borrowing record)")
        self.root.geometry("500x550")
        # Create a text area to handle user input
        tk.Label(root, text= "Student name:").pack(pady = 5)
        self.inputStu = tk.Entry(root, width=40)
        self.inputStu.pack()
        tk.Label(root, text = "Book name:").pack(pady = 5)
        self.inputBook = tk.Entry(root, width=40)
        self.inputBook.pack()
            #setting up the buttons that call a function when they are clicked  
        button = tk.Frame(root)
        button.pack(pady=15)                              
        tk.Button(button, text="Add Record", command=self.add_record).grid(row =0 , column = 0, padx=5)
        tk.Button(button, text="Search Connection (DFS)", command=self.run_dfs).grid(row = 0, column = 1, padx = 5)
        tk.Button(button, text="Show All Records", command=self.display_records).grid(row = 0, column = 2, padx = 5)
        #Create an area for displaying output
        tk.Label(root, text="System Log / Results:").pack()
        self.display = scrolledtext.ScrolledText(root, width=60, height=30)
        self.display.pack(pady=5)
        
    def add_record(self):
        student = self.inputStu.get().strip()
        book = self.inputBook.get().strip()
        if student and book: #call add_edge() when both student name and book name are field
            self.libraryGraph.add_edge(student, book)
            self.display.insert(tk.END, f"{student} borrowed '{book}'\n")
            self.inputStu.delete(0, tk.END)
            self.inputBook.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter both student name and book name.")

    def run_dfs(self): #call dfs()
        studentNode = self.inputStu.get().strip()
        if not studentNode:
            messagebox.showwarning("Input Error", "Please enter a student name to start DFS.")
            return
        
        if studentNode in self.libraryGraph.adj_list:
            result = self.libraryGraph.dfs(studentNode)
            self.display.insert(tk.END, "\n DFS Results:\n")
            for i in result:
                self.display.insert(tk.END, f"{i}\n")
            self.display.insert(tk.END, "==================================\n")
        else:
            self.display.insert(tk.END, "\nno records found.\n")

    def display_records(self):#call get_record() to print the graph of all existing records.
        self.display.delete(1.0, tk.END)
        records = self.libraryGraph.get_records()
        self.display.insert(tk.END, "---Graph of current records---\n")
        if records:
            self.display.insert(tk.END, f"{records}")
        else:
            self.display.insert(tk.END, "No records found")

if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryUI(root)
    root.mainloop()
