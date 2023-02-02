'''
Создайте программу для игры с конфетами человек против человека.
Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, 
чтобы забрать все конфеты у своего конкурента?
a) Добавьте игру против бота
b) Подумайте как наделить бота ""интеллектом""
'''
n_candy = 2021
import random

player_actual = random.randint(1,2)
if player_actual == 1:
    n_candy = 2021
    n=28
    xod_player1 = 0
    xod_player2 = 0
    while n_candy > 0:
        xod_player1+=1
        n_candy=n_candy-28
        if n_candy > 0:
            xod_player2+=1
            n_candy=n_candy-28
else:
    n_candy = 1990
    n=3
    xod_player2 = 1
    xod_player1 = 2
    while n_candy > 0:
        xod_player2+=1
        n_candy=n_candy-28
        if n_candy > 0:
            xod_player1+=1
            n_candy=n_candy-28
if xod_player1>xod_player2:
    print(f"Первому играку нужно взять {n} конфет!{player_actual,xod_player1, xod_player2}")
