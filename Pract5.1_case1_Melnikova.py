'''Задание №1
Создайте класс Касса, который хранит текущее количество денег в кассе, у
него есть методы:
● top_up(X) - пополнить на X
● count_1000() - выводит сколько целых тысяч осталось в кассе
● take_away(X) - забрать X из кассы, либо выкинуть ошибку, что не
достаточно денег'''

class kassa(object):
    many = 153125
    
    def __init__(self, many):
        self.many = many
        

    def top_up(self):
        m = int(input('Какую сумму вносите? '))
        self.many += m
        print(f'сумма в кассе {self.many} рублей')

    def count_1000(self):
        print(f'В кассе осталось ', {self.many//1000}, ' целых тысяч рублей')

    def take_away(self):
        change = int(input('Какую сумму выдать? '))
        self.many -= change
        if self.many < 0:
            print('В кассе не достаточно денег ')
        else:
            print('Операция выполняется...')

ostatok = kassa(15123)
ostatok.top_up()
ostatok.count_1000()
ostatok.take_away()
