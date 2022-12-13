# Создайте программу для игры с конфетами человек против человека.
'''Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку,
 чтобы забрать все конфеты у своего конкурента?'''
from random import randint

num_sweets =2021
max_swims = 28

def player_take(num):
    while True:
        try:
            num = int(num)
        except ValueError:
            num = input("Введите кол-во конфет заново. Цифру: ")
        else:
            if num>max_swims or num<1:
                num=input("Столько брать нельзя, заново: ")
            else:
                break
    return num

def lets_play_bot(cur_swets_num):
    if 0 < cur_swets_num <=max_swims:
        print(f'Выиграл игрок так как осталось {cur_swets_num} конфет')
        return
    print(f'У нас есть {cur_swets_num} конфет. Брать можно от 1 до 28 шт.')
    if cur_swets_num <=cur_swets_num*2:
        player1 = cur_swets_num - max_swims-1
    else:
        player1 = randint(1, max_swims+1)
    print(f'Бот взял {player1} конфет')
    if 0 <  cur_swets_num - player1 <=max_swims:
        print(f' Выиграл игрок так как осталось {cur_swets_num - player1} конфет')
        return
    else:
        player2 = player_take(input('Ходит игрок: '))
    lets_play_bot(cur_swets_num-(player1+player2))


def lets_play(cur_swets_num):
    if 0 < cur_swets_num <=max_swims:
        print(f'Выиграл первый так как осталось {cur_swets_num} конфет')
        return
    print(f'У нас есть {cur_swets_num} конфет. Брать можно от 1 до 28 шт.')
    player1 = player_take(input('Ходит первый игрок: '))
    cur_swets_num -= player1
    if cur_swets_num <= max_swims:
        print(f' Выиграл второй игрок так как осталось {cur_swets_num - player1} конфет')
        return
    else:
        player2 = player_take(input('Ходит второй игрок: '))
    lets_play(cur_swets_num=cur_swets_num - player2)

