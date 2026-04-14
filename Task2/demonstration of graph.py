class Graph:
    def __init__(self):
        self.adj_list={}
    def add_node(self,node):
        self.adj_list[node]=[]
    def add_edge(self, node1, node2):
        self.add_node(node1)
        self.add_node(node2)
        self.adj_list[node1].append(node2)
        self.adj_list[node2].append(node1)
    def get_related(self,node):
        return self.adj_list.get(node,[])
    def print_graph(self):
        for node, related in self.adj_list.items():
            print(node+"->"+str(related))
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
                        ##if related add in list
        return searched

g = Graph()
g.add_edge("amy", "alice wonderland")
g.add_edge("jimmy", "dictionary")
g.add_edge("mimi", "harry potter")
g.add_edge("mami", "peppa pig")

g.print_graph()
result = g.dfs("amy")
print(result)
