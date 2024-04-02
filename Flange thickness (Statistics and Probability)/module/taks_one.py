"""The programme prepares data for the calculation as a sorted list"""


class TaskOne:
    def __init__(self, empty_list, memory):
        self.empty_list = empty_list
        self.memory = memory

if __name__ == '__main__':
    a = []
    m = int(input('Enter how many numbers you want to remember: '))
    TaskOne(a, m)
