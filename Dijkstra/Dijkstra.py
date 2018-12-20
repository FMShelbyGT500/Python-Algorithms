from pprint import pprint
import numpy as np
from collections import OrderedDict, deque


class Dijkstra:
    def __init__(self, matrix, start, end):
        self.matrix = matrix
        self.distances = self.direct_pass(start, end, self.matrix)
        self.path = self.reverse_pass(start, end, self.matrix, self.distances)

    @staticmethod
    def direct_pass(start, end, matrix):
        N = len(matrix)
        unhandled = {i: None for i in range(N)}
        unhandled.pop(end)
        handled = []

        distances = {i: float("inf") for i in range(N)}
        distances[start] = 0
        transitional = OrderedDict()

        current = start

        while unhandled:
            unhandled.pop(current)
            handled.append(current)

            node = matrix[current]

            for i in range(N):
                if node[i]:
                    if i not in handled and i != end:
                        transitional[i] = None
                    new_d = distances[current] + node[i]
                    if new_d < distances[i]:
                        distances[i] = new_d

            try:
                # print(current)
                current = transitional.popitem(last=False)[0]
            except KeyError:
                pass

        return distances

    @staticmethod
    def reverse_pass(start, end, matrix, distances):
        N = len(matrix)
        path = deque()

        def rec(node, path):
            dist = distances[node]
            weights = matrix[node]
            path.appendleft(node)
            if node != start:
                for i in range(N):
                    if weights[i] and distances[i] == dist - weights[i]:
                        return rec(i, path)

            return path

        return rec(end, path)
