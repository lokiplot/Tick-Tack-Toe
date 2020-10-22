import random


class Battlefield:

    def __init__(self, first_player_name, second_player_name):
        self.fields = [['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']]
        self.names = [first_player_name, second_player_name]
        self.number_of_steps = 0
        self.actual_step = random.randint(0, 1)
        print(str(self.names[self.actual_step]) + ' goes first, his symbol is x')

    def make_a_move(self, x, y):
        """
        (x, y) - the location of the cell, if the field is numbered as a two dimensional array
        :param x:
        :param y:
        :return printing 'accepted' or 'impossible step':
        """
        if max(y, x) > 2 or min(x, y) < 0 or self.fields[x][y] != '0':
            print('It\'s an impossible step')
        else:
            if self.number_of_steps % 2 == 0:
                self.fields[x][y] = 'x'
            else:
                self.fields[x][y] = 'o'
            print('Accepted, ' + str(self.names[self.actual_step]))
            self.actual_step = 1 - self.actual_step

    def print_battlefield(self):
        for line in self.fields:
            line_appearance = ''
            for field in line:
                line_appearance += field
            print(line_appearance)

    def print_whose_step(self):
        print('Now ' + str(self.names[self.actual_step]) + 'is stepping.')


b = Battlefield('1', '2')
b.make_a_move(0, 0)
b.print_battlefield()