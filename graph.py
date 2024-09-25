# class Graph:
#
#     def __init__(self):
#         self.list = {} # Adjacency lists
#
#     def add_vertex(self,vertex):
#         if vertex not in self.list:
#              self.list[vertex]=[]
#
#     def add_edge(self,first,second):
#         if first not in self.list:
#             self.list[first]=[]
#         if second not in self.list:
#             self.list[second]=[]
#         self.list[first].append(second)
#         self.list[second].append(first)
#
#     def remove_vertex(self,vertex):
#         if vertex in self.list:
#             for adj in self.list[vertex]:
#                 self.list[adj].remove(vertex)
#         del self.list[vertex]
#
#     def get_vertices(self):
#         return list(self.list.keys())
#
#     def get_edges(self):
#
#         edges=[]
#         for vertex,neighbors in self.list.items():
#             for neighbor in neighbors:
#                 if (neighbor,vertex) not in edges:
#                     edges.append((vertex,neighbor))
#
#         return edges
#
#     def __str__(self):
#         result = []
#         for vertex, neighbors in self.list.items():
#             result.append(f"{vertex}: {', '.join(map(str, neighbors))}")
#         return "\n".join(result)

class Graph:

    def __init__(self,v):
        self.v=v
        self.mat=[[0] * v for _ in range(v)]


    def add_edge(self,first,second):
            if first<self.v and second<self.v:
                self.mat[first][second]=1
                self.mat[second][first]=1


    def remove_edge(self,first,second):
        if first <self.v and second<self.v:
            self.mat[first][second]=0
            self.mat[second][first]=0



    def get_vertices(self):
        return self.v

    def get_edges(self):
        edges=[]
        for i in range(self.v):
            for j in range(self.v):
                if self.mat[i][j]==1:
                    edges.append([i,j])

        return edges

    def display(self):
        # Print the adjacency matrix
        for row in self.mat:
            print(" ".join(map(str, row)))

if __name__=='__main__':

    gp=Graph(10)

    gp.add_edge(2,5)
    gp.add_edge(0,1)
    gp.add_edge(6,5)
    gp.add_edge(1,9)

    gp.display()




