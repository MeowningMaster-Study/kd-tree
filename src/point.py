Point = (int, int)


class Point:
    @staticmethod
    def isEqual(point_a, point_b):
        for i in range(len(point_a)):
            if point_a[i] != point_b[i]:
                return False
        return True
