import map
import person
import enemy
import global_def

map = map.Map()
obl = []
obl.append(person.Person(map.map,map.x,map.y))
print()
map.show_map()
for i in range(0,int(input('Введите кол-во врагов'))):
    obl.append(enemy.Enemy(map.map,map.x,map.y))
print(obl)
print()
map.show_map()
while True:
    for i in obl:
        i.move(map.map,map.x,map.y)
        global_def.meet_up2(obl)
    map.show_map()