from point import Point


class Node:
    def __init__(self, point):
        self.point = point
        self.left = None
        self.right = None


class KDTree:
    def __init__(self, k: int = 2, points=None):
        self.k = k
        self.root = None

        if points:
            for point in points:
                self.insert(point)

    # insert

    def insert(self, point):
        self.root = self.__insertHelper(self.root, point, 0)

    def __insertHelper(self, node, point, depth):
        if not node:
            return Node(point)

        dimesion = depth % self.k

        if point[dimesion] < node.point[dimesion]:
            node.left = self.__insertHelper(node.left, point, depth + 1)
        else:
            node.right = self.__insertHelper(node.right, point, depth + 1)

        return node

    # search

    def search(self, point):
        return self.__searchHelper(self.root, point, 0)

    def __searchHelper(self, node: Node, point, depth: int):
        if not node:
            return False
        if Point.isEqual(node.point, point):
            return True

        dimesion = depth % self.k

        if point[dimesion] < node.point[dimesion]:
            return self.__searchHelper(node.left, point, depth + 1)

        return self.__searchHelper(node.right, point, depth + 1)
