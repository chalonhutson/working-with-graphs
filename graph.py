import abc

import numpy as np


class Graph(abc.ABC):
    
    def __init__(self, numbVertices, directed=False):
        self.numVertices = numVertices
        self.directed = directed