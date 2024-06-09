from jinja2 import Template

import conv

all_convs = conv.convolutions(2,10)
edges = conv.n2(all_convs)

with open('graph.jinja2', 'r') as f:
    t = Template(f.read())

print(t.render(edges=edges))