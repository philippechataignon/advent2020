#!/usr/bin/env python3
import re
import networkx as nx

# plaid green bags contain 3 dark red bags, 1 wavy crimson bag, 4 light coral bags, 4 striped indigo bags.
motif4 = re.compile(r'^(.*) bags contain (\d+) (.*) bags?, (\d+) (.*) bags?, (\d+) (.*) bags?, (\d+) (.*) bags?\.$')
motif3 = re.compile(r'^(.*) bags contain (\d+) (.*) bags?, (\d+) (.*) bags?, (\d+) (.*) bags?\.$')
motif2 = re.compile(r'^(.*) bags contain (\d+) (.*) bags?, (\d+) (.*) bags?\.$')
motif1 = re.compile(r'^(.*) bags contain (\d+) (.*) bags?\.$')

G = nx.DiGraph()

def value(node):
    return 1 + sum([w * value(n2) for _, n2, w in G.edges(node, data="weight")])

if __name__ == "__main__":
    with open("input.txt") as f:
        for l in f:
            l = l.rstrip()
            m4 = motif4.findall(l)
            m3 = motif3.findall(l)
            m2 = motif2.findall(l)
            m1 = motif1.findall(l)
            m = m4[0] if m4 else m3[0] if m3 else m2[0] if m2 else m1[0] if m1 else []

            for i in range(2, len(m), 2):
                G.add_edge(m[0], m[i], weight=int(m[i-1]))

    print(value("shiny gold") - 1)
