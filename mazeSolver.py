from collections import heapq


def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    return path[::-1]


def get_connected_passages(start, m, n, matrix_scheme):
    x, y = start
    result = []

    if y - 1 >= 0 and not matrix_scheme[y-1][x].bottom_wall:
        result.append((x, y-1))

    if y + 1 < n and not matrix_scheme[y][x].bottom_wall:
        result.append((x, y+1))

    if x - 1 >= 0 and not matrix_scheme[y][x-1].right_wall:
        result.append((x-1, y))

    if x + 1 < m and not matrix_scheme[y][x].right_wall:
        result.append((x+1, y))

    return result


def cost(current, neighbour):
    return 1


def heuristic(start, exit):
    return abs(start[0] - exit[0]) + abs(start[1] - exit[1])


def A_star(start, exit, heuristic, matrix_scheme, m, n):
    pq = []
    heapq.heappush(pq, (0, start))

    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, exit)}
    closed_set = set()

    while pq:
        _, current = heapq.heappop(pq)

        if current in closed_set:
            continue
        closed_set.add(current)

        if current == exit:
            return reconstruct_path(came_from, current)

        for neighbor in get_connected_passages(current, m, n, matrix_scheme):
            if neighbor in closed_set:
                continue

            tentative_g = g_score[current] + cost(current, neighbor)

            if tentative_g < g_score.get(neighbor, float('inf')):
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score[neighbor] = tentative_g + heuristic(neighbor, exit)
                heapq.heappush(pq, (f_score[neighbor], neighbor))

    return None