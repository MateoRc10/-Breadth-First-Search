from collections import deque

def solve_maze(maze):
    # Encontrar posición inicial (S) y final (E)
    start = None
    end = None
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 'S':
                start = (i, j)
            elif maze[i][j] == 'E':
                end = (i, j)
    if not start or not end:
        return None

    # Direcciones posibles: arriba, abajo, izquierda, derecha
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([start])
    visited = {start: None}

    while queue:
        current = queue.popleft()
        if current == end:
            break  # Camino encontrado

        for dx, dy in directions:
            x, y = current[0] + dx, current[1] + dy
            # Verificar límites y si la celda es transitable (no es una pared)
            if 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] != '#' and (x, y) not in visited:
                queue.append((x, y))
                visited[(x, y)] = current

    # Reconstruir el camino
    path = []
    if end in visited:
        current = end
        while current:
            path.append(current)
            current = visited[current]
        path.reverse()
    return path

# Laberinto de ejemplo (S: inicio, E: fin, #: pared)
maze = [
    ['#', 'S', '#', '#', '#', '#', '#', '#', '#'],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
    [' ', '#', '#', '#', '#', ' ', '#', ' ', '#'],
    [' ', ' ', ' ', ' ', '#', ' ', '#', ' ', '#'],
    ['#', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#'],
    ['#', ' ', '#', '#', '#', '#', '#', ' ', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', '#', 'E', '#'],
    ['#', '#', '#', '#', '#', '#', '#', '#', '#'],
]

# Resolver e imprimir el camino
path = solve_maze(maze)
if path:
    print("Camino encontrado:")
    for step in path:
        print(f"→ ({step[0]}, {step[1]})")
else:
    print("¡No hay camino válido!")