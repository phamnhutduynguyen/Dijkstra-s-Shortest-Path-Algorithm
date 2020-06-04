nodes = ('X','A1','A2','A3','A4','A5','B1','B2','B3','B4','B5','B6','C1','C2','C3','C4','C5','C6')
distances = {
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

for start in nodes:
    current = start
    currentDistance = 0
    unvisited = {node: None for node in nodes} 
    visited = {}
    unvisited[current] = currentDistance
    path={}
    while True:
        for neighbour, distance in distances[current].items():
            if neighbour not in unvisited: continue
            newDistance = currentDistance + distance
            if unvisited[neighbour] is None or unvisited[neighbour] > newDistance:
                unvisited[neighbour] = newDistance
        visited[current] = currentDistance
        del unvisited[current]
        if not unvisited: break
        candidates = [node for node in unvisited.items() if node[1]]
        current, currentDistance = sorted(candidates, key = lambda x: x[1])[0]

    print('-- Shortest distances from %s --' % start)
    print(visited)