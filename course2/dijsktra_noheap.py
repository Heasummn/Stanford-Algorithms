def dijkstra(graph, weights, s):
    x = {s}
    length = {s: 0}
    while len(x) < len(graph):
        min_len = 1000000
        min_edge = None
        for node in x:
            for edge in graph[node]:
                if edge not in x:
                    #if edge == 133:
                        #print(node, length[node], weights[(node, edge)])
                    l_vw = length[node] + weights[(node, edge)]
                    if l_vw < min_len:
                        min_len = l_vw
                        min_edge = edge
        if min_edge is None: # disconnected graph
            break
        length[min_edge] = min_len
        x.add(min_edge)
    return length

def alg(file):
    graph = {}
    weights = {}
    with open(file) as f:
        for line in f:
            vals = line.split()
            node = int(vals[0])
            graph[node] = []
            for weight in vals[1:]:
                fst, snd = weight.split(",")
                fst = int(fst)
                graph[node].append(fst)
                # Simplify multiple edges to 1 node into just the smallest edge
                if (node, fst) in weights:
                    weights[(node, fst)] = min(int(snd), weights[(node, fst)])
                else:
                    weights[(node, fst)] = int(snd)
    results = dijkstra(graph, weights, 1)
    indices = [7,37,59,82,99,115,133,165,188,197]
    answer = map(str, map(results.__getitem__, indices))
    return(",".join(answer))