import sys
# Idea, writeup:
# Recursive combinatorics? (Show equivalence, recurrence relations?)
# Start with implementation of n choose 2, then generalize
# Title, "Recursive Combinatorics I", then "II", etc

# Nb. should be able to generate larger by combining n2, n3, etc 
# (That is, each just generates pairs of a given size and then all
# are combined. So that can be parameterized..
# TODO: Recursive convolution?
# Generate combinations of n=2
def n2(l):
    if len(l) == 2:
        return [ tuple(l) ]

    item = l[0]
    remainder = l[1:]

    pairs = [ (item,i) for i in remainder ]

    return [ *pairs, *n2(remainder) ]

# Given n2, what next?
# 1. Write func to generate convolutions (tuples)
# 2. Implement hamming dist func on tuples
# 3. Build graph (hashtable w/ neighbors incl. distance as pair)
#   nb. every node is considered a neighbor; order st it minimizes total
# TODO: Draw complete graph of convolutions?

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

# Finally, using the graph over convolutions, compute the distance of all edges.
# This will be a simple hashtable.
# Keep track of visited nodes; keep selecting the minimum until no nodes can be visited.
# That should provide an order of listing convolutions that minimizes the hamming distances.

if __name__ == '__main__':
    conv3 = convolutions(3, 10)
    # Next, compute the distances between them
    dist = dict()
    edges = n2(conv3)
    edge_graph = graph(edges)

    for edge in edges:
        start, end = edge
        dist[edge] = conv_dist(start, end)

    start_edge = min(dist, key=lambda key: dist[key])
    print(start_edge)
    visited = set([start_edge[0]])

    # TODO: How large is the edge graph? (wrt convolutions)
    # TODO: Is this provably the best? 
    # TODO: Counting convolutions (parameterized by k, sum)
    # Should it be minimizes total distance or average distance?
    # Again, review graph approach

    #path = [start_edge[0]]
    while True:
        next_edge = [ n for n in edge_graph[start_edge] if n[1] not in visited ]
        if next_edge == []:
            break

        next_edge = min(next_edge, key=lambda key: dist[key])
        print(next_edge, conv_dist(*next_edge))
        #path.append(next_edge)
        visited.add(next_edge[1])
        start_edge = next_edge

    #print(path)
    # TODO: Generate strings as example
