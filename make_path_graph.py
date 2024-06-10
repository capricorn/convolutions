from jinja2 import Template

import conv

if __name__ == '__main__':
    k = 2
    n = 10
    all_convs = conv.convolutions(k,n)
    edges = conv.n2(all_convs)

    path = conv.shortest_path(n,k)
    shortest_path_edges = set(zip(path, path[1:]))

    with open('path_graph.jinja2', 'r') as f:
        print(Template(f.read()).render(
            edges=enumerate(edges), 
            shortest_path=shortest_path_edges, 
            n=n, 
            k=k,
            start_node=path[0],
            end_node=path[-1]))