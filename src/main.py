from kd_tree import KDTree
from plot import plotKDTree

points = [[3, 6], [17, 15], [13, 15], [0, 0], [6, 12], [9, 1], [2, 7], [10, 19]]

tree = KDTree(2, points)


def testSearch(point):
    if tree.search(point):
        print("Found")
    else:
        print("Not Found")


testSearch([10, 19])
testSearch([12, 19])

plotKDTree(tree, points)
