from matplotlib.axes import Axes
import matplotlib.pyplot as plt
from kd_tree import KDTree, Node

from point import Point
from region import Region

maxInfinity = 1e10
minInfinity = -1e10


def plotKDTree(ax: Axes, tree: KDTree, points: list[Point]):
    maxPoint: Point = (minInfinity, minInfinity)
    minPoint: Point = (maxInfinity, maxInfinity)
    for point in points:
        maxPoint = (max(maxPoint[0], point[0]), max(maxPoint[1], point[1]))
        minPoint = (min(minPoint[0], point[0]), min(minPoint[1], point[1]))

    maxPoint = (maxPoint[0] + 2, maxPoint[1] + 2)
    minPoint = (minPoint[0] - 2, minPoint[1] - 2)

    ax.set_xlim((minPoint[0], maxPoint[0]))
    ax.set_ylim((minPoint[1], maxPoint[1]))
    __plotKDtreeHelper(tree, ax, tree.root, None, 0, (minPoint, maxPoint))
    ax.set_aspect("equal", "box")


def __plotKDtreeHelper(
    tree: KDTree, ax: Axes, node: Node, parent: Node, depth: int, boundaries: Region
):
    if not node:
        return

    if tree.k != 2:
        raise Exception("Only 2d trees can be plotted")

    ax.scatter(node.point[0], node.point[1], color="b")
    ax.annotate(f"{node.point}\nd[{depth}]", (node.point[0], node.point[1]))

    dimesion = depth % tree.k

    x, y = node.point
    minPoint, maxPoint = boundaries

    if not parent:
        if dimesion == 0:
            ax.axvline(x)
        else:
            ax.axhline(y)
    else:
        if dimesion == 0:
            if y >= parent.point[1]:
                ax.plot([x, x], [parent.point[1], maxPoint[1]], color="black")
            else:
                ax.plot([x, x], [parent.point[1], minPoint[1]], color="black")
        else:
            if x >= parent.point[0]:
                ax.plot([parent.point[0], maxPoint[0]], [y, y], color="black")
            else:
                ax.plot([parent.point[0], minPoint[0]], [y, y], color="black")

    __plotKDtreeHelper(
        tree,
        ax,
        node.left,
        node,
        depth + 1,
        [
            boundaries[0],
            [
                x if dimesion == 0 else boundaries[1][0],
                y if dimesion == 1 else boundaries[1][1],
            ],
        ],
    )
    __plotKDtreeHelper(
        tree,
        ax,
        node.right,
        node,
        depth + 1,
        [
            [
                x if dimesion == 0 else boundaries[0][0],
                y if dimesion == 1 else boundaries[0][1],
            ],
            boundaries[1],
        ],
    )


def plotRegionResult(ax: Axes, queryRegion: Region, regionResult: list[Point]):
    pointMin, pointMax = queryRegion
    ax.plot([pointMin[0], pointMin[0]], [pointMin[1], pointMax[1]], color="red")
    ax.plot([pointMax[0], pointMax[0]], [pointMin[1], pointMax[1]], color="red")
    ax.plot([pointMin[0], pointMax[0]], [pointMin[1], pointMin[1]], color="red")
    ax.plot([pointMin[0], pointMax[0]], [pointMax[1], pointMax[1]], color="red")

    for point in regionResult:
        ax.scatter(*point, color="red")
