import random
import re

file_name = input("Enter the name of your file: ")
directory = r'C:\Users\Malavika U\PycharmProjects\Final_code\\'
num_hospitals = 0
hospital_list = []
word_list = []
f = open("PartCD_Output.txt", "w")
f.write("Starting point\tDistance")

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
    with open(directory + 'PartCD_Input.txt', 'w') as fout:
        fout.writelines(data[2:])
    f = open(directory + 'PartCD_Input.txt', 'r')  # opening the file
    first_line = f.readline()  # read first line to move file pointer
    total_num_node_edges = re.findall(r'\d+', first_line)
    global total_num_nodes
    total_num_nodes = int(total_num_node_edges[0])

    print("Hospitals: ")
    print(hospital_list)
    with open(directory + 'PartCD_Input.txt', 'w') as fout:
        fout.writelines(data[4:])
    f = open(directory + 'PartCD_Input.txt', 'r')  # opening the file
    first_line = f.readline()  # read first line to move file pointer

    graph = {new_list: [] for new_list in range(total_num_nodes)}
    for line in f:
        word_list = line.split()
        a = int(word_list[0])
        b = int(word_list[1])
        graph[a].append(b)
        graph[b].append(a)
    return graph


def BFS_knearest(graph, start, k):
    needed = isHospital.copy()
    explored = []
    count = 0
    f.write("\n" + str(start) + "\t\t\t\t")
    # Queue for traversing the
    # graph in the BFS
    queue = [[start]]

    # If the desired node is
    # reached
    if needed[start]:
        needed[start] = 0
        count += 1
        if count == k:
            return
        f.write("0, ")

    # Loop to traverse the graph
    # with the help samplof the queue
    while queue:
        path = queue.pop(0)
        node = path[-1]

        # Codition to check if the
        # current node is not visited
        if node not in explored:
            neighbours = graph[node]

            # Loop to iterate over the
            # neighbours of the node
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)

                # Condition to check if the
                # neighbour node is the goal
                if needed[neighbour]:
                    count += 1
                    needed[neighbour] = 0
                    f.write(str(len(new_path) - 1) + ", ")
                    if count == k:
                        return
            explored.append(node)

            # Condition when the nodes
    # are not connected
    f.write("-, ")
    return


graph = build_graph()
global isHospital
isHospital = [0] * total_num_nodes
for m in hospital_list:
    isHospital[int(m)] = 1
print(graph)    
k = int(input("Enter the no. of nearest hospitals to find: "))
for z in range(total_num_nodes):
    BFS_knearest(graph, z, k)