import numpy as np
import random
import re

file_name = input("Enter the name of your file: ")
directory = r'C:\Users\Malavika U\PycharmProjects\Final_code\\'
num_hospitals = 0
hospital_list = []
word_list = []
traversalPath = []
calc = 1
search = 0


def build_graph():
    with open(directory + file_name + '.txt', 'r') as fin:
        data = fin.read().splitlines(True)
    with open(directory + 'PartA_Input.txt', 'w') as fout:
        fout.writelines(data[2:])
    f = open(directory + 'PartA_Input.txt', 'r')  # opening the file
    first_line = f.readline()  # read first line to move file pointer
    total_num_node_edges = re.findall(r'\d+', first_line)
    global total_num_nodes
    total_num_nodes = int(total_num_node_edges[0])
    global nodes
    nodes = total_num_nodes
    global adj_mat
    adj_mat = [[0] * nodes] * nodes  # initialising empty adj matrix
    global matrix
    global tree
    global distance
    matrix = np.array(adj_mat)
    tree = np.array(adj_mat)

    f_hospitals = open(directory + 'Hospitals.txt', 'r')  # opening the file
    first_line = f_hospitals.readline()  # read first line to move file pointer
    num_hospitals = re.findall(r'\d+', first_line)
    num_hospitals = int(num_hospitals[0])
    for line in f_hospitals:
        hospital_list.append(int(line))
    f_hospitals.close()

    print(hospital_list)
    distance = np.array([[0] * num_hospitals] * nodes)
    with open(directory + 'PartA_Input.txt', 'w') as fout:
        fout.writelines(data[4:])
    f = open(directory + 'PartA_Input.txt', 'r')  # opening the file
    first_line = f.readline()  # read first line to move file pointer
    for line in f:
        word_list = line.split()
        fromnode = int(word_list[0])
        tonode = int(word_list[1])
        matrix[fromnode][tonode] = 1
        matrix[tonode][fromnode] = 1  # since an edge exists between fromnode and tonode, assign 1 to this element


def minAndHospital(a):
    # print(a)
    minVal = a[0]
    pos = 0
    for i in range(len(a)):
        if a[i] < minVal:
            minVal = a[i]
            pos = i
    return [minVal, hospital_list[pos]]


def BFS(v, start):

    visited = [False] * v
    q = [start]

    # Set source as visited 
    visited[start] = True

    while q:
        vis = q[0]
        # Print current node 
        # print(vis, end=' ')
        q.pop(0)

        # For every adjacent vertex to  
        # the current vertex 
        for i in range(v):
            if matrix[vis][i] == 1 and not visited[i]:
                # Push the adjacent node  
                # in the queue
                tree[vis][i] = 1
                q.append(i)

                # set 
                visited[i] = True
    # print()


def treeTraverse(v, start, h, location):
    # Visited vector to so that a
    # vertex is not visited more than
    # once Initializing the vector to
    # false as no vertex is visited at
    # the beginning
    visited = [False] * v
    q = [start]
    distance[start][h] = 0

    # Set source as visited
    visited[start] = True

    while q:
        vis = q[0]
        traversalPath.append(vis)
        if vis == location and search:
            return
        q.pop(0)

        # For every adjacent vertex to
        # the current vertex
        for i in range(v):
            if tree[vis][i] == 1 and not visited[i]:
                if search:
                    if i == location:
                        # print(i)
                        traversalPath.append(i)
                        return
                # Push the adjacent node
                # in the queue
                # print(distance)
                if calc:
                    distance[i][h] += 1 + distance[vis][h]
                # print(distance)
                q.append(i)

                # set
                visited[i] = True


build_graph()

count = 0
for i in hospital_list:
    BFS(nodes, i)
    treeTraverse(nodes, i, count, i)
    count = count + 1
    tree = np.array(adj_mat)
    traversalPath = []
# print(distance)

f = open("PartA_Output.txt", "w")
f.write("Starting point\tDistance\tPath\n")
calc = 0
search = 1
for i in range(nodes):
    answer = minAndHospital(distance[i])
    # print(answer)
    dist = answer[0]
    hospital = answer[1]
    BFS(nodes, i)
    # print(tree)
    treeTraverse(nodes, i, 0, hospital)
    f.write(str(i) + "\t\t\t\t" + str(dist) + "\t\t\t" + str(traversalPath) + "\n")
    tree = np.array(adj_mat)
    traversalPath = []
