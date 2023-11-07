""" Determination of the weight of the projectile while maintaining the
condition of minimum exit energy Ew

Created by @SzklarskiAdrian, 11.2023 """

# Projectile caliber [mm]
D = 122

# Range [m]
X = 11800

class Bullet:
    def __init__(self, d, x):
        self.d = d
        self.x = x

    def __str__(self):
        pass


if __name__ == '__main__':
    app = Bullet(D, X)
    print(app)
