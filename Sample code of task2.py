import networkx as nx 
class LibraryGraph:
    def init(self):
        self.graph = nx.DiGraph() ##create a graph
    def reader(self, reader_name):
        self.graph.add_node(reader_name,type='reader', reader_name=reader_name) ##create a node "reader" and set the type to 'reader' add attribute to seperate reader and book
    def book(self, book_name):
        self.graph.add_node(book_name,type='book',book_name=book_name) ##same as reader one but become book
    def borrow(self, reader_name, book_name, end_day):
        self.graph.add_edge(reader_name, book_name, end_day=end_day, returnday=None,##return day not yet firmed
                            status='borrowed') ##set book borrowed by reader and set the due day
    def bookreturn(self, reader_name, book_name, return_day):##reader returning book
        self.graph[reader_name][book_name]['return_day']='returned'##make the book returned and set the return day
    def borrowing(self, reader_name):
        borrow = [] ##ccreate a borrowed list
        for book in self.graph.successors(reader_name):
            edge_data=self.graph[reader_name][book] ##to get all borrowed book from the reader
            if edge_data.get('status')=='borrowed':
                borrow.append((book,edge_data['end_day'])) ## if book borrowed add in the list
        return borrow
lib = LibraryGraph()
lib.reader('Leon')
lib.book('awa')

lib.borrow('Leon','awa','20266-02-31')
print("borrowed: ",lib.borrowing)