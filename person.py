import lists
import random

class Person:
    x = 0
    y = 0
    hp = 0
    res_type = 0
    rp = 0
    name = ''
    sname = 'Y'
    stats = [0,0,0,0,0]
    race = ''

    def __init__(self, map, map_x, map_y):
        self.x = random.randint(0, map_x - 1)
        self.y = random.randint(0, map_y - 1)
        map[self.x][self.y] = self.sname

    def move(self, map, map_x, map_y):
        move = input('Куда вы пойдете?')
        if move == 'w':
            if self.x == 0:
                print('Прохода нет!')
            else:
                map[self.x][self.y] = '0'
                self.x -= 1
                map[self.x][self.y] = self.sname
        elif move == 's':
            if self.x == map_x - 1:
                print('Прохода нет!')
            else:
                map[self.x][self.y] = '0'
                self.x += 1
                map[self.x][self.y] = self.sname
        elif move == 'a':
            if self.y == 0:
                print('Прохода нет!')
            else:
                map[self.x][self.y] = '0'
                self.y -= 1
                map[self.x][self.y] = self.sname
        elif move == 'd':
            if self.y == map_y - 1:
                print('Прохода нет!')
            else:
                map[self.x][self.y] = '0'
                self.y += 1
                map[self.x][self.y] = self.sname
