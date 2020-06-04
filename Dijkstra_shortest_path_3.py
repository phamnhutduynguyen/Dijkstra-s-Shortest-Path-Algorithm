def initial_graph() :
    
    return {
    'X': {'B1': 5, 'B3': 6},
    'A1': {'A2': 4, 'A3': 8, 'A5': 5, 'B2': 5},
    'A2': {'A1': 4, 'A3': 4, 'A5': 3, 'A4': 3, 'B2': 6, 'C2': 8},
    'A3': {'A1': 8, 'A2': 4, 'A4': 6, 'C2': 7},
    'A4': {'A2': 3, 'A3': 6, 'A5': 3, 'B6': 7, 'C1': 9, 'C2': 8, 'C3': 9},
    'A5': {'A1': 5, 'A2': 3, 'A4': 3, 'B2': 6, 'B3': 8, 'B4': 6, 'B6': 6},
    'B1': {'X': 5, 'B2': 8, 'B3': 5},
    'B2': {'B1': 8, 'B3': 6, 'A5': 6, 'A2': 6, 'A1': 5},
    'B3': {'X': 6, 'B2': 6, 'B1': 5, 'B4': 5, 'A5': 8},
    'B4': {'B3': 5, 'A5': 6, 'B6': 5},
    'B5': {'B6': 5, 'C1': 5},
    'B6': {'B4': 5, 'B5': 5, 'A4': 7, 'A5': 6, 'C1': 6},
    'C1': {'B5': 5, 'B6': 6, 'A4': 9, 'C3': 8, 'C4': 7, 'C5': 7, 'C6': 9},
    'C2': {'A2': 8, 'A3': 7, 'A4': 8, 'C3': 4},
    'C3': {'C2': 4, 'A4': 9, 'C1': 8, 'C4': 4},
    'C4': {'C1': 7, 'C3': 4, 'C5': 3},
    'C5': {'C4': 3, 'C6': 3, 'C1': 7},
    'C6': {'C5': 3, 'C1': 9}}

print(initial_graph())
    
initial = 'X'
path = {}
adj_node = {}
queue = []
graph = initial_graph()
for node in graph:
    path[node] = float("inf")
    adj_node[node] = None
    queue.append(node)
    
path[initial] = 0
while queue:
    # find min distance which wasn't marked as current
    key_min = queue[0]
    min_val = path[key_min]
    for n in range(1, len(queue)):
        if path[queue[n]] < min_val:
            key_min = queue[n]  
            min_val = path[key_min]
    cur = key_min
    queue.remove(cur)
    print(cur)
    
    for i in graph[cur]:
        alternate = graph[cur][i] + path[cur]
        if path[i] > alternate:
            path[i] = alternate
            adj_node[i] = cur
            
            
x = 'B6'
print('The path between X to C6')
print(x, end = '<-')
while True:
    x = adj_node[x]
    if x is None:
        print("")
        break
    print(x, end='<-')