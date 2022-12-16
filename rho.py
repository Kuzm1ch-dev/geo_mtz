import numpy as np
import math


class rho:
    def __init__(self, file_path):
        self.file = open(file_path, 'r')

        self.mas_n = list(map(int, self.file.readline().strip().split()))
        self.h_z = list(map(int, self.file.readline().strip().split()))
        self.h_y = list(map(int, self.file.readline().strip().split()))
        self.rho = np.empty((len(self.h_y), len(self.h_z)), dtype=float)

        for i in range(len(self.h_z)):
            self.rho[i] = list(map(int, self.file.readline().strip().split()))  # h_z layers down counter

        self.file.close()

        self.list_x, self.list_y = [], []

        for i in range(len(self.h_y)):
            self.list_x.append(np.sum(self.h_y[:i])/1000)

        for i in range(len(self.h_z)):
            self.list_y.append(np.sum(self.h_z[:i])/1000)

        self.position_y = np.arange(len(self.list_x))
        self.position_z = np.arange(len(self.list_y))

        self.n = self.mas_n[0]  # Count of layers, that a going down in table
        self.m = 5  # count of periods
        self.t1 = 0.01  # first period
        self.q = 2  # period change coefficient

        self.row_solutions = []
        self.phi_solutions = []

        for i in range(self.mas_n[1]):
            temp = self.mtz_first([j[i] for j in self.rho], self.h_z)
            self.row_solutions.append(temp[0])
            self.phi_solutions.append(temp[1])

    def mtz_first(self, p, h) -> list:
        p, h = np.array(p), np.array(h)
        t = np.array([self.q ** i * self.t1 for i in range(self.m)])
        w = 2 * np.pi / t
        u = 4 * np.pi * 10 ** (-7)

        r = np.empty(self.m, dtype=complex)
        for i, e in enumerate(w):
            rc = 1
            for j in reversed(range(self.n - 1)):
                k = np.sqrt((-1 * complex("0+1j") * e * u) / p[j])
                a = np.sqrt(p[j] / p[j + 1])
                b = np.exp(-2 * k * h[j]) * (rc - a) / (rc + a)
                rc = (1 + b) / (1 - b)
            r[i] = rc

        rc = np.abs(r) ** 2 * p[0]
        phi_t = np.angle(r) - np.pi / 4
        phi = list(map(math.degrees, (np.angle(r) - np.pi / 4)))
        return [rc, phi]


if __name__ == "__main__":
    ShowData("test_data/x.txt")
