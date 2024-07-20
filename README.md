# EduGraph: An Intelligent Course Prerequisite Analyzer
In this project, I developed a Python-based tool that helps students plan their course schedules by analyzing prerequisites, detecting cycles, and providing an optimal order of courses using graph theory algorithms and visualizations.

1. User Input for Prerequisites:
   - Prompted the user to input the number of course prerequisites.
   - Collected prerequisite pairs (course and its prerequisite) from the user as input.

2. Create Course Graph:
   - Initialized a directed graph using defaultdict to store courses and their prerequisites.
   - Ensured that both course and prerequisite are strings.
   - I populated the graph by adding each prerequisite as a key and appending the corresponding course to its list of neighbors.

3. Cycle Detection in the Graph:
   - Implemented the Depth-First Search (DFS) algorithm to check for cycles in the graph.
   - Used a stack to track the current path and a set to track visited nodes.
   - If a node was revisited in the current path,a cycle was detected.

4. Topological Sorting:
   - If no cycle was detected, I performed topological sorting to determine the order in which courses should be taken.
   - Used DFS to traverse the graph and appended nodes to a stack in post-order.
   - I reversed the stack to get the topological order of the courses.

5. Graph Visualization:
    - Used the NetworkX library to create a directed graph from the course-prerequisite relationships.
    - Computed positions of nodes in the graph using the spring layout algorithm.
    - Finally, visualized the graph using Matplotlib, displaying nodes, edges, and labels.

And then as a result and output, we get the topological order of courses.
