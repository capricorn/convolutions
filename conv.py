import sys
from typing import List, Tuple

import colorful as cf
def trad_conv3_ex(l):
    results = []
    for i in range(0,l+1):
        for j in range(0,l-i+1):
            results.append((i,j,l-i-j))

    return results

def convolutions2(l):
    results = []
    for i in range(0,l+1):
        results.append((i,l-i))
    return results

# Generate combinations of n=2
def n2(l):
    if len(l) == 2:
        return [ tuple(l) ]

    item = l[0]
    remainder = l[1:]

    pairs = [ (item,i) for i in remainder ]

    return [ *pairs, *n2(remainder) ]

# Fully complete graph
def graph(l):
    g = dict()

    for key in l:
        g[key] = []
        for val in l:
            if val == key:
                continue
            g[key].append(val)

    return g

def conv_dist(a, b):
    ''' Compute hamming dist betw. two convolutions '''
    return sum(map(abs, map(lambda t: t[0]-t[1], zip(a,b))))

# TODO: Recursive implementation?
def convolutions(k, k_sum):
    ''' Generate the set of convolutions of length k equaling k_sum '''

    if k == 1:
        return [[k_sum]]

    results = []
    for i in range(0,k_sum+1):
        subcon = convolutions(k-1, k_sum-i)
        subcon = [ tuple([i, *c]) for c in subcon ]
        results.extend(subcon)

    return results

def shortest_path(n,k) -> List[Tuple[int]]:
    # TODO: Rename
    conv3 = convolutions(k,n)
    # Next, compute the distances between them
    dist = dict()
    edges = n2(conv3)
    #edge_graph = graph(edges)
    edge_graph = graph(conv3)

    # bidirectional so may need permutations instead
    for edge in edges:
        start, end = edge
        dist[edge] = conv_dist(start, end)
        dist[(end,start)] = conv_dist(end,start)

    start_edge = min(dist, key=lambda key: dist[key])
    #print(start_edge)
    visited = set([start_edge[0]])

    path = [start_edge[0]]
    start_node = start_edge[0]
    while True:
        # TODO: Edge graph should just be reachable vertices, not edges themselves
        # All reachable nodes not yet visited
        next_edge = [ n for n in edge_graph[start_node] if n not in visited ]
        if next_edge == []:
            break

        possible_edges = [ (start_node, n) for n in next_edge ]
        next_edge = min(possible_edges, key=lambda key: dist[key])
        #print(f'{next_edge[0]}->{next_edge[1]} ({conv_dist(*next_edge)})')
        #print(f'{start_edge[0]}->{next_edge[1]}')
        #print(next_edge, conv_dist(*next_edge))
        path.append(next_edge[1])
        visited.add(next_edge[1])
        #start_edge = next_edge
        start_node = next_edge[1]
    
    # TODO: Return path
    return path

def minimum_conv2_path(n) -> List[Tuple[int]]:
    conv = convolutions2(n)
    curr_node = (0,n)
    visited = set([curr_node])
    path = [curr_node]

    while True:
        neighbor_nodes = [ n for n in conv if n not in visited ]
        if neighbor_nodes == []:
            break

        curr_node = min(neighbor_nodes, key=lambda n: conv_dist(curr_node,n))
        path.append(curr_node)
        visited.add(curr_node)
    
    return path

if __name__ == '__main__':
    convs = convolutions(3,5)
    path = shortest_path(5, 3)

    for min_conv, trad_conv in zip(path, convs):
        mi, mj, mk = min_conv
        ti, tj, tk = trad_conv

        min_conv_str = f'{cf.red("a"*mi)}' + f'{cf.green("b"*mj)}' + f'{cf.blue("c"*mk)}'
        trad_conv_str = f'{cf.red("a"*ti)}' + f'{cf.green("b"*tj)}' + f'{cf.blue("c"*tk)}'

        print(min_conv_str + '\t' + trad_conv_str)