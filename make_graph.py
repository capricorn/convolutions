from jinja2 import Template

import conv

k = 2
n = 10
all_convs = conv.convolutions(k,n)
edges = conv.n2(all_convs)

with open('graph.jinja2', 'r') as f:
    t = Template(f.read())

print(t.render(edges=edges,k=k,n=n))