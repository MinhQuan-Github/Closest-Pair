import numpy as np
import matplotlib.pyplot as plt
import math

points = []
xcoords = []
ycoords = []


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class ClosestPair:
    @staticmethod
    def distance(p1, p2):
        return math.sqrt((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2)

    def bruteforce_closest_pair(self, p, n):
        index1, index2 = None, None
        d_min = float("inf")
        for i in range(0, n - 1):
            for j in range(i + 1, n):
                d = self.distance(p[i], p[j])
                if d < d_min:
                    d_min = d
                    index1 = i
                    index2 = j
        return index1, index2

    def closest_pair(self, points):
        px = sorted(points, key=lambda p1: p1.x)
        py = sorted(points, key=lambda p1: p1.y)
        return self.rcp(px, py)

    def rcp(self, px, py):
        if len(px) <= 3:
            p1, p2 = self.bruteforce_closest_pair(px, len(px))
            return px[p1], px[p2]
        else:
            num_points = len(px)
            left_size = math.ceil(num_points / 2)
            right_size = math.floor(num_points / 2)
            lx = px[:left_size]
            rx = px[right_size:]
            m = (max(point.x for point in lx) + min(point.x for point in rx)) / 2
            ly = sorted(lx, key=lambda p1: p1.y)
            ry = sorted(rx, key=lambda p1: p1.y)
            pl, ql = self.rcp(lx, ly)
            pr, qr = self.rcp(rx, ry)
            delta = min(self.distance(pl, ql), self.distance(pr, qr))
            left_rectangle = m - delta
            right_rectangle = m + delta
            b = []
            for i in py:
                if left_rectangle <= i.x <= right_rectangle:
                    b.append(i)
            if len(b) <= 1:
                if self.distance(pl, ql) <= self.distance(pr, qr):
                    return pl, ql
                else:
                    return pr, qr
            else:
                p1 = b[0]
                q1 = b[1]
                for i in range(0, len(b)):
                    for j in range(i + 1, len(b)):
                        if self.distance(b[i], b[j]) < self.distance(p1, q1):
                            p1, q1 = b[i], b[j]
                if self.distance(p1, q1) < delta:
                    return p1, q1
                elif self.distance(pl, ql) <= self.distance(pr, qr):
                    return pl, ql
                else:
                    return pr, qr

    def scatter(self, n):
        for i in range(0, n):
            Point.x = np.random.randint(1000)
            Point.y = np.random.randint(1000)
            xcoords.append(Point.x)
            ycoords.append(Point.y)
            points.append(Point(Point.x, Point.y))

    def run(self):
        n = int(input("Enter number of points: "))
        self.scatter(n)
        a, b = self.closest_pair(points)
        print("The closest pair of points is:", "(%d, %d) and (%d, %d)" % (a.x, a.y, b.x, b.y))
        print("Their distance is %f" % self.distance(a, b))
        plt.scatter(xcoords, ycoords, c='black')
        plt.scatter(a.x, a.y, c='red')
        plt.scatter(b.x, b.y, c='red')
        plt.plot([a.x, b.x], [a.y, b.y])
        path = 'Closest_Pair_Result.png'
        plt.savefig(path)
        plt.show()


if __name__ == '__main__':
    objc = ClosestPair()
    objc.run()
