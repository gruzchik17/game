def meet_up(obj1,obj2):
    if obj1.x == obj2.x and obj1.y == obj2.y:
        print('Встреча')
        fight(obj1,obj2)

def meet_up2(obl):
    for i in obl:
        for j in obl:
            if i == j:
                pass
            else:
                if i.x == j.x and i.y == j.y:
                    print('Встреча')
                    fight(i, j)
                    break
                else:
                    pass


def fight(obj1,obj2):
    print('Бой начался!')