'''
Determination of power received by a space satellite antenna

Created by @AdrianSzklarski, 11.2023
'''

import math


class Antena:

    def __init__(self, Pt, tetaT, fu, R, Dt, alfa3, tetar, c):
        self.Pt = Pt
        self.tetaT = tetaT
        self.fu = fu
        self.R = R
        self.Dt = Dt
        self.alfa3 = alfa3
        self.tetar = tetar
        self.c = c

    def calculation(self):
        self.GT = round(10 * math.log10((self.tetaT * math.pow((math.pi * self.Dt * self.fu * 1e9 / self.c), 2))), 2)
        self.GR = round(10 * math.log10(self.tetar * math.pow((math.pi * 70 / self.alfa3), 2)), 2)
        self.LFS = round(10 * math.log10(math.pow((4 * math.pi * self.R * 1e6 * self.fu * 1e9 / self.c), 2)), 2)
        self.Pr_dBW = self.Pt + self.GT + self.GR - self.LFS
        return self.GT, self.GR, self.LFS, self.Pr_dBW

    def __str__(self):
        return f'{self.GT}, {self.GR}, {self.LFS}, {self.Pr_dBW}'


if __name__ == '__main__':
    # input data
    Pt = 20
    tetaT = 0.6
    fu = 14
    R = 40
    Dt = 4
    alfa3 = 2
    tetar = 0.55
    c = 3e8

    # --- run program ---
    hear = Antena(Pt, tetaT, fu, R, Dt, alfa3, tetar, c)
    print('GT:', hear.calculation()[0], 'dBi')
    print('GR:', hear.calculation()[1], 'dBi')
    print('LFS:', hear.calculation()[2], 'dBi')
    print('Power received by the antenna: ', hear.calculation()[3], 'dBW')
