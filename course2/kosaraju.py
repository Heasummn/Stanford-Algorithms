from collections import deque, Counter
import sys

def load_graph(f):
    graph = {}
    rev_graph = {}
    for line in f:
        (head, tail) = (int(x) for x in line.split())
        if head in graph:
            graph[head].append(tail)
        else:
            graph[head] = [tail]
        if tail in rev_graph:
            rev_graph[tail].append(head)
        else:
            rev_graph[tail] = [head]

    return graph, rev_graph

def kosaruja(graph, rev_graph):
    order = dfs_order(rev_graph)
    explored = set()
    s = None

    # silly edge case because some of the test cases skip numbers but expect those to count as an SCC. Easier solution is leader = [0] * len(order)
    leader = list(range(max(*graph.keys(), *rev_graph.keys())))

    for node in order:
        if node not in explored:
            s = node
            explored.add(node)
            stack = deque()
            stack.append(node)
            while len(stack) > 0:
                v = stack.pop()
                leader[v - 1] = s
                if v not in graph:
                    leader[v - 1] = v
                    continue
                for edge in graph[v]:
                    if edge not in explored:
                        explored.add(edge)
                        stack.append(edge)
    scc = Counter(leader)
    ret = list(map(lambda x: x[1], scc.most_common(5)))
    return ret + [0] * (5 - len(ret))


def dfs_order(rev_graph):
    finishing = []
    explored = set()
    for node in rev_graph:
        if node not in explored:
            explored.add(node)

            ## actual DFS
            stack = deque()
            stack.append(node)
            while len(stack) > 0:
                v = stack.pop()
                if v in rev_graph:
                    for edge in rev_graph[v]:
                        if edge not in explored:
                            explored.add(edge)
                            stack.append(edge)
                finishing.append(v)
    return finishing

def alg(file):
    with open(file) as f:
        graph, rev_graph = load_graph(f)
        scc = kosaruja(graph, rev_graph)
        return ",".join(map(str, scc))