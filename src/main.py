from kd_tree import KDTree
from plot import plotKDTree, plotRegionResult
from point import Point
import matplotlib.pyplot as plt

from region import Region

points: list[Point] = [
    (3, 6),
    (17, 15),
    (13, 15),
    (0, 0),
    (6, 12),
    (9, 1),
    (2, 7),
    (10, 19),
]

tree = KDTree(points)


def testSearch(point):
    if tree.search(point):
        print("Found")
    else:
        print("Not Found")


testSearch((10, 19))
testSearch((12, 19))

queryRegion: Region = ((2, 5), (14, 16))
regionResult = tree.regionQuery(queryRegion)

fig, ax = plt.subplots()
plotKDTree(ax, tree, points)
plotRegionResult(ax, queryRegion, regionResult)
plt.show()
