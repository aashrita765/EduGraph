from collections import defaultdict

def create_course_graph(prerequisites):
    graph = defaultdict(list)
    for course, prereq in prerequisites:
        if not isinstance(course, str) or not isinstance(prereq, str):
            raise ValueError("Both course and prerequisite must be strings.")
        if course not in graph:
            graph[course] = []
        if prereq not in graph:
            graph[prereq] = []
        graph[prereq].append(course)
    return graph


# prerequisites = [("CH102", "CH101"), ("CH103", "CH101"), ("CH103", "CH104"), ("CH104", "CH102"), ("CH105", "CH103"), ("CH105", "CH104")]
def get_user_input():
    n = int(input("Enter the number of prerequisites: "))
    prerequisites = []
    for _ in range(n):
        course, prereq = input("Enter course and prerequisite separated by space: ").split()
        prerequisites.append((course, prereq))
    return prerequisites

prerequisites = get_user_input()
graph = create_course_graph(prerequisites)

def has_cycle(graph):
    visited = set()
    stack = set()
    
    def dfs(node):
        if node in stack:
            return True
        if node in visited:
            return False
        visited.add(node)
        stack.add(node)
        for neighbor in graph[node]:
            if dfs(neighbor):
                return True
        stack.remove(node)
        return False
    
    for node in graph:
        if node not in visited:
            if dfs(node):
                return True
            # print("cycle", stack, visited, node)
    return False

if has_cycle(graph):
    print("Graph has cycle:(")
else:
    print("No cycle")

def topological_sort(graph):
    visited = set()
    stack = []
    
    def dfs(node):
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                dfs(neighbor)
            stack.append(node)
    
    for node in graph:
        if node not in visited:
            dfs(node)
    
    return stack[::-1]

if not has_cycle(graph):
    course_order = topological_sort(graph)
    print("Course order:", course_order)
else:
    print("Cannot determine course order due to cycle.")

import networkx as nx
import matplotlib.pyplot as plt

def visualize_graph(graph):
    G = nx.DiGraph()
    for node in graph:
        for neighbor in graph[node]:
            G.add_edge(node, neighbor)
    pos = nx.spring_layout(G)   #computes the positions of nodes in a graph 
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_size=10, font_weight='bold')
    plt.show()

visualize_graph(graph)
