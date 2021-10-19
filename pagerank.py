from built_graph import build
import networkx as nx
import matplotlib.pyplot as plt
import pylab

G, (source, target, relation) = build()

ppr1 = nx.pagerank(G)
tuples = sorted([(key, val) for key, val in ppr1.items()], key=lambda x: -x[1])

tuples = tuples[:400]

sel_names = [x[0] for x in tuples]

_source, _target, _relation = [], [], []
for s, t, r in zip(source, target, relation):
    if s in sel_names and t in sel_names:
        _source.append(s)
        _target.append(t)
        _relation.append(r)

print(len(_source))


G = nx.DiGraph()
rel = list(zip(_source, _target))
G.add_edges_from( rel )

node_list = list(G)
node_sizes = [ ppr1[x] * 500000 for x in node_list ]
pos = nx.kamada_kawai_layout(G)
plt.figure(num=None, figsize=(100, 100), dpi=80)
plt.axis('off')
fig = plt.figure(1)
nx.draw_networkx_nodes(G, pos, node_size=node_sizes)
nx.draw_networkx_edges(G, pos, edge_color=(0.9,0.9,0.9))
nx.draw_networkx_labels(G, pos, font_size=8)

plt.savefig("graph.pdf", bbox_inches="tight")
pylab.close()
del fig