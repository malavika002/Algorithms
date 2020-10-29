import random
import re

file_name = input("Enter the name of your file: ")
directory = r'C:\Users\Malavika U\PycharmProjects\Final_code\\'
edges = []
fromTo = []
num_hospitals = 0
hospital_list = []
word_list = []
f_out = open("PartB_Output.txt", "w")
f_out.write("Starting point\tDistance\tPath\n")

# Function to build the graph
def build_graph():
    f_hospitals = open(directory + 'Hospitals.txt', 'r')  # opening the file
    first_line = f_hospitals.readline()  # read first line to move file pointer
    num_hospitals = re.findall(r'\d+', first_line)
    num_hospitals = int(num_hospitals[0])
    for line in f_hospitals:
        hospital_list.append(int(line))
    f_hospitals.close()

    with open(directory + file_name + '.txt', 'r') as fin:
        data = fin.read().splitlines(True)
    with open(directory + 'PartB_Input.txt', 'w') as fout:
        fout.writelines(data[2:])
    f = open(directory + 'PartB_Input.txt', 'r')  # opening the file
    first_line = f.readline()  # read first line to move file pointer
    total_num_node_edges = re.findall(r'\d+', first_line)
    global total_num_nodes
    total_num_nodes = int(total_num_node_edges[0])

    with open(directory + 'PartB_Input.txt', 'w') as fout:
        fout.writelines(data[4:])
    f = open(directory + 'PartB_Input.txt', 'r')  # opening the file
    first_line = f.readline()  # read first line to move file pointer

    graph = {new_list: [] for new_list in range(total_num_nodes)}
    for line in f:
        word_list = line.split()
        a = int(word_list[0])
        b = int(word_list[1])
        for k in range(0, num_hospitals):
            if a == hospital_list[k]:
                word_list[0] = 'H'
            if b == hospital_list[k]:
                word_list[1] = 'H'
        graph[a].append(word_list[1])
        graph[b].append(word_list[0])
    return graph


def BFS_SP(graph, start, goal):
    explored = []
    # Queue for traversing the graph in the BFS
    queue = [[start]]

    # If the desired node is reached
    if isHospital[start]:
        f_out.write(str(start) + "\t\t\t\t0\t\t\tH\n")
        return

    # Loop to traverse the graph with the help of the queue
    while queue:
        path = queue.pop(0)
        node = int(path[-1])

        # Condition to check if the current node is not visited
        if node not in explored:
            neighbours = graph[node]

            # Loop to iterate over the neighbours of the node
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)

                # Condition to check if the neighbour node is the goal
                if neighbour == goal:
                    f_out.write(str(start) + "\t\t\t\t" + str(len(new_path)) + "\t\t\t" + str(new_path) + "\n")
                    return
            explored.append(node)

            # Condition when the nodes are not connected
    print("Path doesn't exist.")
    return


graph = build_graph()
global isHospital
isHospital = [0] * total_num_nodes
for m in hospital_list:
    isHospital[int(m)] = 1
for z in range(total_num_nodes):
    BFS_SP(graph, z, 'H')
