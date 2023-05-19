from point import Point
from region import Region, hasOverlap, isPointInside

maxInfinity = 1e10
minInfinity = -1e10


class Node:
    def __init__(self, point):
        self.point = point
        self.left = None
        self.right = None


class KDTree:
    def __init__(self, points=None):
        self.k = 2  # dimensions
        self.root = None

        if points:
            for point in points:
                self.insert(point)

    # insert point

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

    # search point

    def search(self, point: Point):
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

    # query over region

    def regionQuery(self, searchRegion: Region) -> list[Point]:
        return self.__regionQueryHelper(
            self.root,
            searchRegion,
            0,
            ((minInfinity, minInfinity), (maxInfinity, maxInfinity)),
        )

    def __regionQueryHelper(
        self, node: Node, region: Region, depth: int, boundaries: Region
    ) -> list[Point]:
        result = []

        if not node or not hasOverlap(region, boundaries):
            return result

        point = node.point

        if isPointInside(point, region):
            result.append(point)

        dimesion = depth % self.k
        x, y = point

        leftResult = self.__regionQueryHelper(
            node.left,
            region,
            depth + 1,
            [
                boundaries[0],
                [
                    x if dimesion == 0 else boundaries[1][0],
                    y if dimesion == 1 else boundaries[1][1],
                ],
            ],
        )

        rigthResult = self.__regionQueryHelper(
            node.right,
            region,
            depth + 1,
            [
                [
                    x if dimesion == 0 else boundaries[0][0],
                    y if dimesion == 1 else boundaries[0][1],
                ],
                boundaries[1],
            ],
        )

        return result + leftResult + rigthResult
