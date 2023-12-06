f=open("input.txt")
dat=f.read()
f.close()

def add_vertex(v):
    global graph
    global vertices_no
    global vertices
    if (v not in vertices):
        vertices.append(v)
        vertices_no = vertices_no + 1
        for vertex in graph:
            vertex.append(0)
        temp = []
        for i in range(vertices_no):
            temp.append(0)
        graph.append(temp)

def add_edge(v1,v2,e):
    global graph
    global vertices_no
    global vertices
    if (v1 in vertices and v2 in vertices):
        index1 = vertices.index(v1)
        index2 = vertices.index(v2)
        graph[index1][index2] = e

def print_graph():
    global graph
    global vertices_no
    for i in range(vertices_no):
        for j in range(vertices_no):
            if graph[i][j] != 0:
                print(vertices[i], " -> ", vertices[j], " edge weight: ", graph[i][j])

f=open("input.txt")
lines=f.readlines()
f.close()

vertices = []
vertices_no = 0
graph = []    
for i in lines:
    word = i.split()
    add_vertex(word[0])
    add_vertex(word[2])
    add_edge(word[0], word[2], word[4])

print_graph()