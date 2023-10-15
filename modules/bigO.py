import math
import matplotlib.pyplot as plt
from abc import abstractmethod


class BigO:

    def __init__(self, axisX):
        self.axisX = list(range(1, 101, 1))
        self.link = r'/home/adrian/Pulpit/GitHub/Analysis_of_algorithms_using_probablisitic_models/fig'
        self.FONT_SIZE = 8
        self.get_plot_first()
        self.get_plot_second()
        self.get_plot_third()
        self.get_plot_fourth()
        self.get_show()

    @abstractmethod
    def get_data(ABC):
        #  The abstract class was added for possible further code extension and data reuse.
        x_ver1 = [1] * 100
        x_ver2 = list(range(1, 101, 1))
        x_ver3 = [math.log(x) for x in x_ver2]
        x_ver4 = [x * math.log(x) for x in x_ver2]
        x_ver5 = [math.pow(x, 2) for x in x_ver2]
        x_ver6 = [math.pow(2, x) for x in x_ver2]
        return x_ver1, x_ver2, x_ver3, x_ver4, x_ver5, x_ver6

    def get_plot_first(self):
        plt.subplot(2, 2, 1)
        plt.text(40, 3.8, 'BigO = O(1)', fontsize=self.FONT_SIZE)
        plt.plot(self.axisX, self.get_data()[0])

        plt.text(40, 44, 'BigO = O(log(n))', rotation=36,
                 rotation_mode='anchor', fontsize=self.FONT_SIZE)
        plt.plot(self.axisX, self.get_data()[1])
        plt.ylabel("Iteration steps", fontsize=self.FONT_SIZE)

    def get_plot_second(self):
        plt.subplot(2, 2, 2)
        plt.text(30, 3.6, 'BigO = O(n)', rotation=20,
                 rotation_mode='anchor', fontsize=self.FONT_SIZE)
        plt.plot(self.axisX, self.get_data()[2])


    def get_plot_third(self):
        plt.subplot(2, 2, 3)
        plt.text(40, 300, 'BigO = O(n*log(n))', rotation=2,
                 rotation_mode='anchor', fontsize=self.FONT_SIZE)
        plt.plot(self.axisX, self.get_data()[3])

        plt.text(40, 1785, 'BigO = O(n**2)', rotation=38,
                 rotation_mode='anchor', fontsize=self.FONT_SIZE)
        plt.plot(self.axisX, self.get_data()[4])
        plt.xlabel("Trajectory points on the x-axis", fontsize=self.FONT_SIZE)
        plt.ylabel("Iteration steps", fontsize=self.FONT_SIZE)

    def get_plot_fourth(self):
        plt.subplot(2, 2, 4)
        plt.text(40, 1 * 1e28, 'BigO = O(2**n)', rotation=0,
                 rotation_mode='anchor', fontsize=self.FONT_SIZE)
        plt.plot(self.axisX, self.get_data()[5])
        plt.xlabel("Trajectory points on the x-axis", fontsize=self.FONT_SIZE)

    def get_show(self):
        # creating a dictionary
        font = {'size': 12}
        # using rc function
        plt.rc('font', **font)

        plt.savefig(self.link + '/figure1.png')
        plt.show()


if __name__ == '__main__':
    BigO(100)
