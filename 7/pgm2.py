#!/usr/bin/env python3
import re
import networkx as nx
import uuid

# plaid green bags contain 3 dark red bags, 1 wavy crimson bag, 4 light coral bags, 4 striped indigo bags.
motif4 = re.compile(r'^(.*) bags contain (\d+) (.*) bags?, (\d+) (.*) bags?, (\d+) (.*) bags?, (\d+) (.*) bags?\.$')
motif3 = re.compile(r'^(.*) bags contain (\d+) (.*) bags?, (\d+) (.*) bags?, (\d+) (.*) bags?\.$')
motif2 = re.compile(r'^(.*) bags contain (\d+) (.*) bags?, (\d+) (.*) bags?\.$')
motif1 = re.compile(r'^(.*) bags contain (\d+) (.*) bags?\.$')
motif0 = re.compile(r'^(.*) bags contain no other bags\.$')

G = nx.DiGraph()

def value(node):
    adj = G.edges(node, data="weight")
    if adj:
        sum = 1
        for n1, n2, w in adj:
            sum += w * value(n2)
        return sum
    else:
        return 1

if __name__ == "__main__":
    with open("input.txt") as f:
        for l in f:
            l = l.rstrip()
            m4 = motif4.findall(l)
            m3 = motif3.findall(l)
            m2 = motif2.findall(l)
            m1 = motif1.findall(l)
            m0 = motif0.findall(l)
            if m4:
                m = m4[0]
                for i in range(2, len(m), 2):
                    G.add_edge(m[0], m[i], weight=int(m[i-1]))
            elif m3:
                m = m3[0]
                for i in range(2, len(m), 2):
                    G.add_edge(m[0], m[i], weight=int(m[i-1]))
            elif m2:
                m = m2[0]
                for i in range(2, len(m), 2):
                    G.add_edge(m[0], m[i], weight=int(m[i-1]))
            elif m1:
                m = m1[0]
                G.add_edge(m[0], m[2], weight=int(m[1]))
            elif m0:
                G.add_node(m0[0])

    print(value("shiny gold") - 1)
