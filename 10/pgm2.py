#!/usr/bin/env python3
import networkx as nx

G = nx.DiGraph()

with open("input.txt") as f:
    for l in f:
        G.add_node(int(l.strip()))

G.add_node(0)
end = max(G) + 3
G.add_node(end)
print(G.nodes)

for n in G.nodes:
    for i in range(1, 4):
        if n + i in G.nodes:
            G.add_edge(n, n + i)
print(G.edges)

d = {}
for node in sorted(G.nodes):
    n = 0
    for p in G.predecessors(node):
        # si déjà calculé, on récupère
        if p in d:
            n += d[p]
        # sinon on ajoute 1
        else:
            n += 1
        # et on stocke
        d[node] = n

# trajets possibles final
print(d[end])
