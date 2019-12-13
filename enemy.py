import random

class Enemy:
    x = 0
    y = 0
    sname = 'E'

    def __init__(self,map,map_x, map_y):
        while True:
            self.x = random.randint(0,map_x-1)
            self.y = random.randint(0,map_y-1)
            if map[self.x][self.y] == 0:
                map[self.x][self.y] = self.sname
                break
            else:
                pass

    def move(self, map, map_x, map_y):
        move = random.randint(0,4)
        if move == 0:
            if self.x == 0:
                pass
            else:
                map[self.x][self.y] = '0'
                self.x -= 1
                map[self.x][self.y] = self.sname
        elif move == 1:
            if self.x == map_x - 1:
                pass
            else:
                map[self.x][self.y] = '0'
                self.x += 1
                map[self.x][self.y] = self.sname
        elif move == 2:
            if self.y == 0:
                pass
            else:
                map[self.x][self.y] = '0'
                self.y -= 1
                map[self.x][self.y] = self.sname
        elif move == 3:
            if self.y == map_y - 1:
                pass
            else:
                map[self.x][self.y] = '0'
                self.y += 1
                map[self.x][self.y] = self.sname