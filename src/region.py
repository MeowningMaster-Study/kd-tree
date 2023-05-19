from point import Point

Region = tuple[Point, Point]


def hasOverlap(region1: Region, region2: Region) -> bool:
    # Extract the boundaries of each region
    (minX1, minY1), (maxX1, maxY1) = region1
    (minX2, minY2), (maxX2, maxY2) = region2

    # Check for overlap by comparing the boundaries
    if maxX1 < minX2 or maxX2 < minX1 or maxY1 < minY2 or maxY2 < minY1:
        return False
    else:
        return True


def isPointInside(point: Point, region: Region) -> bool:
    x, y = point
    # Extract the boundaries of the region
    (minX, minY), (maxX, maxY) = region

    # Check if the point is inside the region
    if minX <= x <= maxX and minY <= y <= maxY:
        return True
    else:
        return False
