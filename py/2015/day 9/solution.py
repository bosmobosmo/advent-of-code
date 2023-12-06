
from itertools import permutations

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

f=open("input.txt")
lines=f.readlines()
f.close()

vertices = []
vertices_no = 0
graph = []    
distances = []
for i in lines:
    word = i.split()
    add_vertex(word[0])
    add_vertex(word[2])
    add_edge(word[0], word[2], int(word[4]))
    add_edge(word[2], word[0], int(word[4]))

for i in vertices:
    print(i)

routes = list(permutations(vertices, 8))
# for i in graph:
#     for j in i:
#         print(j)
for i in routes:
    temp = 0
    for j in range(len(i) - 1):
        i1 = vertices.index(i[j])
        i2 = vertices.index(i[j+1])
        temp = temp + graph[i1][i2]
    distances.append(temp)

print(len(distances))

distances = set(distances)
print(min(distances))
print(max(distances))