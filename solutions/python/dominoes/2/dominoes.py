"""Function to help build a chain of dominoes.
   defaultdict module is used to initialize dict keys with empty lists and zeros.
"""

from collections import defaultdict

def can_chain(dominoes):
    """Order a given set of domino stones so that they form a correct domino chain.
    
       In the chain, the dots on one half of a stone must match the dots on the neighboring 
       half of an adjacent stone. dditionally, the dots on the halves of the stones without 
       neighbors (the first and last stone) must match each other.

    :param dominoes: list[tuple] - dominoes set.
    :return: list[tuple] or None - chain of dominoes if it is possible. Otherwise, None.
    """
    if not dominoes:
        return []
    graph = defaultdict(list)
    counts = defaultdict(int)
    for l_num, r_num in dominoes:
        graph[l_num].append(r_num)
        graph[r_num].append(l_num)
        counts[l_num] += 1
        counts[r_num] += 1
    if any(count % 2 != 0 for count in counts.values()):
        return None
    start_node = dominoes[0][0]
    stack = [start_node]
    path = []
    while stack:
        node = stack[-1]
        if graph[node]:
            neighbor = graph[node].pop()
            graph[neighbor].remove(node)
            stack.append(neighbor)
        else:
            path.append(stack.pop())
    if len(path) - 1 != len(dominoes) or path[0] != path[-1]:
        return None
    return [(path[index], path[index+1]) for index in range(len(path) - 1)]