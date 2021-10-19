import json
import networkx as nx
import matplotlib.pyplot as plt
import pylab

import numpy as np

def build():
    with open("graph.json", "r") as f:
        g = json.load(f)

    source = g["source"]
    target = g["target"]
    relation = g["relation"]

    """
    perm = np.random.permutation(500)

    _source = []
    _target = []
    _relation = []

    for idx in perm:

        _source.append( source[idx] )
        _target.append( target[idx] )
        _relation.append( relation[idx] )

    source = _source
    target = _target
    relation = _relation
    """

    G = nx.DiGraph()
    G.add_edges_from( zip(source, target) )

    return G, (source, target, relation)