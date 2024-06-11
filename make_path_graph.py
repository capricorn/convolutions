from jinja2 import Template

import conv

if __name__ == '__main__':
    k = 2
    n = 10
    all_convs = conv.convolutions(k,n)
    edges = conv.n2(all_convs)

    # WIP: Reference this instead; the short_path_edges should also be in the same form
    edges_set = [ frozenset(e) for e in edges ]

    path = conv.shortest_path(n,k)
    shortest_path_edges = set(map(lambda t: frozenset(t), zip(path, path[1:])))

    '''
    print(len(all_convs))
    #print(len(shortest_path_edges))
    print(edges[0])
    print(shortest_path_edges)
    '''

    # What the problem is:
    # TODO: Fix; convert edges to frozen sets; can then hash against them
    # n2 returns tuples but really should return sets; otherwise, (v1,v2) may exist but not (v2,v1).
    results = []
    # TODO: Just set shortest path edges to this for now? And implement correctly later (new edition of n2)
    # TODO: Separate n2 implementation instead?
    for e in edges_set:
        # Hack to get combinations of edges
        #if e in shortest_path_edges or tuple(reversed(e)) in shortest_path_edges:
        if e in shortest_path_edges:
            results.append(e)
    
    #print(len(results))

    with open('path_graph.jinja2', 'r') as f:
        print(Template(f.read()).render(
            edges=enumerate(edges_set), 
            shortest_path=shortest_path_edges, 
            n=n, 
            k=k,
            start_node=path[0],
            end_node=path[-1],
            make_edge=lambda e: tuple(e)))