import matplotlib.pyplot as plt
from networkx import nx
import random

n = 10  # 10 nodes
m = 30  # 20 edges

G = nx.gnm_random_graph(n, m)

# print the adjacency list
f = open("sample.txt", "w")
f.write("Road Map Sample\nGenerated using NetworkX\nTotal Nodes: " + str(n) + " Total Edges: " + str(m) + "\n")
f.write("The edges are as follows:\n")
count = 0
for line in nx.generate_adjlist(G):
    for i in line:
        if i.isdigit():
            f.write(str(count) + " " + str(i) + "\n")
    count += 1

num_hospitals = random.randint(0, n-1)
hospital_list = []
f.close()
f = open("Hospitals.txt", "w")
f.write("#" + str(num_hospitals) + "\n")
j = 0
while j < num_hospitals:
    flag = 1
    temp = random.randint(1, n)
    for m in hospital_list:
        if temp == m:
            flag = 0
            break
    if flag:
        hospital_list.append(temp)
        f.write(str(temp) + "\n")
        j += 1

nx.draw(G)
plt.show()
