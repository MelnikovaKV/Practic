'''Задание №2
Создайте класс Черепашка, который хранит позиции x и y черепашки, а также
s - количество клеточек, на которое она перемещается за ход
у этого класс есть методы:
● go_up() - увеличивает y на s
● go_down() - уменьшает y на s
● go_left() - уменьшает x на s
● go_right() - увеличивает y на s
● evolve() - увеличивает s на 1
● degrade() - уменьшает s на 1 или выкидывает ошибку, когда s может
стать ≤ 0
● count_moves(x2, y2) - возвращает минимальное количество действий, за
которое черепашка сможет добраться до x2 y2 от текущей позиции'''

class Cherepashka(object):
    position1 = 4
    position2 = 5
    step = 1

    def __init__(self, x, y, s):
        self.position1 = x
        self.position2 = y
        self.step = s

    def go_up(self):
        self.position1 += self.step
        print(f'{self.position1},{self.position2},{self.step}')

    def go_down(self):
        self.position1 -= self.step
        print(f'{self.position1},{self.position2},{self.step}')

    def go_left(self):
        self.position2 -= self.step
        print(f'{self.position1},{self.position2},{self.step}')

    def go_right(self):
        self.position2 += self.step
        print(f'{self.position1},{self.position2},{self.step}')

    def evolve(self):
        self.step += 1
        print(f'{self.position1},{self.position2},{self.step}')

    def degrade(self):
        self.step -= 1
        if self.step < 0:
            return 'нет места для хода'

    def count_moves(self):
        m = (self.position1 - 2) // self.step
        n = (self.position1 - 2) % self.step
        o = (self.position2 - 2) // self.step
        p = (self.position2 - 2) % self.step

        if self.position1 == 2 and self.position2 == 2:
            print (f'находится в пункте назначения')
        elif self.position1 == 2 and self.position2 < 2:
            print (f'Минимум {self.step} ходов')
        elif self.position1 == 2 and self.position2 > 2:
            if p == 0:
                print (f'Минимум {o} ходов')
            else:
                print (f'Минимум {o+self.step-p+1} ходов')
        elif self.position1 > 2 and self.position2 == 2:
            if n == 0:
                print (f'Минимум {m} ходов')
            else:
                print (f'Минимум {m+self.step-n+1} ходов')
        elif self.position1 > 2 and self.position2 < 2:
            if n == 0:
                print (f'Минимум {m+self.step} ходов')
            else:
                print (f'Минимум {m+self.step-n+1+self.step} ходов')
        elif self.position1 > 2 and self.position2 > 2:
            if n == 0 and p == 0:
                print (f'Минимум {m+o} ходов')
            elif n == 0 and p > 0:
                print (f'Минимум {m+o+self.step-p+1} ходов')
            elif n > 0 and p == 0:
                print (f'Минимум {m+self.step-n+o+1} ходов')
            else:
                print (f'Минимум {m+self.step-n+o+self.step-p+1} ходов')
        elif self.position1 < 2 and self.position2 == 2:
            print (f'Минимум {self.step} ходов')
        elif self.position1 < 2 and self.position2 < 2:
            print (f'Минимум {self.step+1} ходов')
        else:
            if p == 0:
                print (f'Минимум {o+self.step} ходов')
            else:
                print (f'Минимум {self.step+o+self.step-p+1} ходов')   
        

k=Cherepashka(1, 17, 4)

k.go_up()
k.go_down()
k.go_left()
k.go_right()
k.evolve()
k.degrade()
k.count_moves()
        