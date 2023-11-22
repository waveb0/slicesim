class BaseStation:
    def __init__(self, pk, coverage, capacity_bandwidth, slices=None):
        self.pk = pk
        self.coverage = coverage #基站覆盖范围
        self.capacity_bandwidth = capacity_bandwidth #基站带宽
        self.slices = slices #基站部署切片
        print(self)

    def __str__(self):
        return f'BS_{self.pk:<2}\t cov:{self.coverage}\t with cap {self.capacity_bandwidth:<5}'

