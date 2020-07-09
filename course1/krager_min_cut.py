import random
import math
import copy

def krager_min_cut(graph):
    while len(graph) > 2:
        node1 = random.choice(tuple(graph.keys()))
        node2 = random.choice(graph[node1])
        for node in graph[node2]:
            if node != node1:
                graph[node1].append(node)
            graph[node].remove(node2)
            if node != node1:
                graph[node].append(node1)
        del graph[node2]

    min_cut = len(graph[list(graph)[0]])
    return min_cut


def alg(file):
    graph = {}
    with open(file) as f:
        for line in f:
            split = [int(x) for x in line.split()]
            graph[split[0]] = split[1:]
    n = len(graph)
    N = int(n ** 2 * math.log2(n))

    min_cut = n
    for i in range(N):
        new_cut = krager_min_cut(copy.deepcopy(graph))
        if new_cut < min_cut:
            min_cut = new_cut
    return min_cut