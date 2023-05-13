import matplotlib.pyplot as plt
from kd_tree import KDTree, Node
import copy

maxInfinity = 1e10
minInfinity = -1e10


def plotKDTree(tree: KDTree, points):
    maxPoint = [minInfinity, minInfinity]
    minPoint = [maxInfinity, maxInfinity]
    for point in points:
        maxPoint[0] = max(maxPoint[0], point[0])
        maxPoint[1] = max(maxPoint[1], point[1])
        minPoint[0] = min(minPoint[0], point[0])
        minPoint[1] = min(minPoint[1], point[1])

    maxPoint[0] += 2
    maxPoint[1] += 2
    minPoint[0] -= 2
    minPoint[1] -= 2

    fig, ax = plt.subplots()
    ax.set_xlim([minPoint[0], maxPoint[0]])
    ax.set_ylim([minPoint[1], maxPoint[1]])
    __plotKDtreeHelper(tree, ax, tree.root, None, 0, [minPoint, maxPoint])
    ax.set_aspect("equal", "box")
    plt.show()


def __plotKDtreeHelper(tree: KDTree, ax, node: Node, parent: Node, depth: int, bounds):
    if not node:
        return

    if tree.k != 2:
        raise Exception("Only 2d trees can be plotted")

    ax.scatter(node.point[0], node.point[1], color="b")
    ax.annotate(f"{node.point}\nd[{depth}]", (node.point[0], node.point[1]))

    dimesion = depth % tree.k

    x, y = node.point
    minPoint, maxPoint = bounds

    if not parent:
        if dimesion == 0:
            ax.axvline(x)
        else:
            ax.axhline(y)
    else:
        if dimesion == 0:
            if y >= parent.point[1]:
                ax.plot([x, x], [parent.point[1], maxPoint[1]])
            else:
                ax.plot([x, x], [parent.point[1], minPoint[1]])
        else:
            if x >= parent.point[0]:
                ax.plot([parent.point[0], maxPoint[0]], [y, y])
            else:
                ax.plot([parent.point[0], minPoint[0]], [y, y])

    __plotKDtreeHelper(
        tree,
        ax,
        node.left,
        node,
        depth + 1,
        [
            bounds[0],
            [
                x if dimesion == 0 else bounds[1][0],
                y if dimesion == 1 else bounds[1][1],
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
                x if dimesion == 0 else bounds[0][0],
                y if dimesion == 1 else bounds[0][1],
            ],
            bounds[1],
        ],
    )
