import math


class Coverage: #覆盖范围
    def __init__(self, center, radius):
        self.center = center #基站中心（位置x，y）
        self.radius = radius #半径

    def _get_gaussian_distance(self, p):
        return math.sqrt(sum((i-j)**2 for i,j in zip(p, self.center)))

    def is_in_coverage(self, x, y): #判断是否在基站的覆盖范围内
        return self._get_gaussian_distance((x,y)) <= self.radius

    def __str__(self):
        x, y = self.center
        return f'[c=({x:<4}, {y:>4}), r={self.radius:>4}]'
