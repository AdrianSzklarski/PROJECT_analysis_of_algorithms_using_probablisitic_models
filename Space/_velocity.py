"""A program from determining the speed of a spacecraft on Proxima Centauri.
@AdrianSzklarski, 12.2023"""

import math, sys, os

# DISTANCE = 40E12  # [km] for Proxima Centauri
DISTANCE = 500E6  # [km] for Example
SEC = 1


class CalcVelocity:
    doc_help = """
    A programme that calculates the speed of a spacecraft in space. 

    The constant DISTANCE here is the distance to any object in [km].

    The flight time is given in years, e.g. þ half a year 0.6, two years and three months 2.3, etc.

    The result is the speed in [km/s]. The programme for the special part of the Alcubierre drive also 
    calculates a speed greater than the speed of light. 
    
    The programme is an introduction to a doctoral thesis. 
    
    Example:
    distance = 500,000,000 km
    time = approx. 7.1 months = 218.67 days = 5248 hours = 314 885 minutes = 18 893 088 seconds

    speed = distance / time

    speed = 500 000 000 km / 18 893 088 seconds = 26.5 km/second
    """

    def __init__(self, d, t, s):
        self.distance = d
        self.time = t
        self.sec = s
        self.min = 60 * self.sec
        self.hour = 60 * self.min
        self.day = 24 * self.hour
        self.week = 7 * self.day
        self.mounth = 4 * self.week
        self.year = 12 * self.mounth

    def get_year_to_sec(self):
        time = math.modf(self.time)
        full_year, mounth = time[1], round(time[0], 2)

        tab = []
        for i in list(range(0, 12)):
            elements = float('0.' + str(i))
            tab.append(elements)

        if mounth in tab:
            m = str(mounth).split('.')
            return full_year, int(m[1])
        else:

            print('Wrong value, after the dot you can only enter values up to 1 to 11 i.e.'
                  ' months up to January to November. December as number 12 represents '
                  'a full year. Correct the value!')

            os.execl(sys.executable, sys.executable, *sys.argv)

    def get_calc_time(self):
        time = self.get_year_to_sec()[0] * self.year
        div = self.get_year_to_sec()[1] * self.mounth

        velocity = self.distance / (time + div)  # km/s
        if velocity <= 299500:
            return velocity
        else:
            print('\nThe speed is greater than the laws of physics allow. If you want to count for such'
                  ' speeds switch to the code module for the Alcubierre drive.')
            while True:
                button = input('\n\nDo you want to count the speed below the speed of light?    If yes select: "y"'
                               '\nDo you want to count the velocity for the Alcubierre drive? If yes select: "a"'
                               '\nDo you want to exit the programme?                          If yes select: "e": > ')
                if button == 'y':
                    os.execl(sys.executable, sys.executable, *sys.argv)
                elif button == 'a':
                    print('This module is not available for this version of the programme.')
                    exit()
                elif button == 'e':
                    print('Thank you and see you there!')
                    exit()
                else:
                    print('Wrong choice, try again!')

    def __str__(self):
        return f'Velocity: {round(self.get_calc_time(), 2)} [km /s]'


if __name__ == '__main__':
    while True:
        try:
            time = input('In what time do you want to reach the star [years]? : ')
            app = CalcVelocity(DISTANCE, float(time), SEC)
            print(app)
            break
        except ValueError as e:
            print('Wrong Value', e)
