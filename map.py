class Map:
    x = 0
    y = 0
    map = []

    def __init__(self):
        self.create_map()
        self.show_map()

    def create_map(self):
        self.x = int(input('Введите ширину карты'))
        self.y = int(input('Введите длину карты'))
        for i in range(0, self.x):
            self.map.append([])
            for j in range(0, self.y):
                self.map[i].append(0)

    def show_map(self):
        st = ''
        for i in self.map:
            for j in i:
                st += str(j) + '  '
            else:
                print(st)
                st = ''
