'''
To determine the diameter of a lead sphere, it was weighed on a balance,
obtaining the result 5.2 grmas. Calculate the diameter of the sphere and the
relative errors of the direct measurement of its weight and the measurement
of the composite diameter.

Created by @AdrianSzklarski, 10.2023
'''

import numpy as np


class Bullet:
    def __init__(self):
        # Absolute error as the sensitivity of the measuring instrument[kg]
        self.e_a = 0.01 * 1e-3
        self.e_a2 = 0.1

        # Mass[kg]
        self.m = 5.2 * 1e-3

        # Density of lead[kg / m ^ 3]
        self.ro = 11300

        self.get_calculation()

    def get_calculation(self):
        x = (6 * self.m) / (np.pi * self.ro)
        Fi = round(np.cbrt(x) * 1000, 2)
        re = round(self.e_a / self.m, 7)
        re_p = round(re * 100, 2)
        ed = round(self.e_a2 / Fi, 6)
        ed_p = round(ed * 100, 2)
        return Fi, re, re_p, ed, ed_p

    def __str__(self):
        return f'Diameter Fi               [mm]: {self.get_calculation()[0]}\n' \
               f'Relative error                : {self.get_calculation()[1]}\n' \
               f'Relative error             [%]: {self.get_calculation()[2]}\n' \
               f'Error diameter measurement    : {self.get_calculation()[3]}\n' \
               f'Error diameter measurement [%]: {self.get_calculation()[4]}'


if __name__ == '__main__':
    bullet = Bullet()
    print(bullet)
