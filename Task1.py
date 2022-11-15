# Задача 1. Создайте программу для игры в "Крестики-нолики".
from random import randint

#объявим глобальные переменные
X = 'X'
O = 'O'
position_max_number = 9

print('Перед началом игры ознакомьтесь,пожалуйста, с правилами:')
print("""
Эта игра называется "Крестики-Нолики". Для того чтобы сделать ход,
нажмите цифру от 0 до 8. Это число будет обозначать номеру ячкейки
на игровой доске, как показано внизу на рисунке:

                    0 | 1 | 2
                    ---------
                    3 | 4 | 5
                    ---------
                    6 | 7 | 8

А теперь давайте начинать игру!
""")

def turn():
    print('Для начала определим, кто первый будет ходить с помощью жеребьевки.')
    turn = randint(1,2)
    return turn

def position(ask,min,max):
    position = None
    while position not in range(min,max):
        position = int(input(ask))#до тех пор пока пользователь не введет число в заданном диапозоне , мы будет запрашивать у него ввод
    return position

def get_turn():
    first = turn()
    if first == 1:
        print('Поздравляю, Вы ходите первым')
        player = X
        bot = O
    else:
        print('Бот ходит первым')
        bot = X
        player = O
    return bot,player

def get_new_board():#создаем новую пустую игровую доску
    play_board = []
    for i in range(position_max_number):
        play_board.append(' ')
    return play_board

def show_board(play_board):#выводим игровую доску на экран, элементами на этой доске уже будут Х, О и пробелы
    print('\n\t',play_board[0],'|',play_board[1],'|',play_board[2])
    print('\t','---------')
    print('\n\t',play_board[3],'|',play_board[4],'|',play_board[5])
    print('\t','---------')
    print('\n\t',play_board[6],'|',play_board[7],'|',play_board[8],'\n')

def get_acceptable_moves(play_board):#функция для определения оставшихся доступных ходов для пользователя и бота
    acceptable_moves = []
    for i in range(position_max_number):
        if play_board[i] == ' ':
            acceptable_moves.append(i)
    return acceptable_moves

def player_move(play_board,player):#функция для запроса хода от пользователя , на вход принимает игровую доску и тип хода от пользователя 
    acceptable = get_acceptable_moves(play_board)#рассчитваем список с позициями доступных ходов 
    move = None
    while move not in acceptable:#до тех пор пока пользователь не введет число из доступных ходов, запрашиваем у него ввести позицию на доске из доступных
        move = position('Введите позицию на доске от 0-8: ',0, position_max_number)
        if move not in acceptable:
            print('К сожалению, эта позиция уже занята, пожалуйста, введите, другое число.')
    return move

def get_winner(play_board):#принимаем на вход игровую доску, анализируем ее и возвращаем победителя в игре
    winner_positions = ((0,1,2),
                        (3,4,5),
                        (6,7,8),
                        (0,4,8),
                        (2,4,6),
                        (0,3,6),
                        (1,4,7),
                        (2,5,8))
    for i in winner_positions:#цикл, который перебирает все возможные варианты набора фишек на выигрышных позициях
        if play_board[i[0]] == play_board[i[1]] == play_board[i[2]] != ' ':# проверяем равны ли все фишки игрока равны одному значению и находятся ли они на выигрышных позициях

            winner = play_board[i[0]]
            return winner
        if ' ' not in play_board:#если не осталось пробелов на доске и никто не выиграл - возвращаем "ничью"
            return 'Ничья'
    return None # если результат игры не достигнут, не определен победитель, то функция просто возвращает None
        

def bot_move(play_board,bot,player):
    play_board = play_board[:]#создадим копию имеющейся уже доски, так как мы будем менять внутри нее значения
    win_position = (4,0,2,6,8,1,3,5,7)
    print('Теперь ходит бот', end= ' ')
    for move in get_acceptable_moves(play_board):#цикл, который перебирает все допустимые(пустые) позиции, куда боту можно сходить
        play_board[move] = bot
        if get_winner(play_board) == bot:#если следующий ход выигрышный, то бот сделает этот ход и функция останавливается
            print(move)
            return move
        play_board[move] = ' '#после проверки, отменяет внесенные изменения и пробуем следующий ход
    for move in get_acceptable_moves(play_board):
        play_board[move] = player
        if get_winner(play_board) == player:
            print(move)
            return(move)
        play_board[move] = ' '
    
    for move in win_position:#если из всех проверок выше мы не нашли подходящий ход, тогда из списка выигрышных позиций выбираем подходящий ход и как только номер ячейки на поле обнаруживается пустым, то выбираем этот ход
        if move in get_acceptable_moves(play_board):
            print(move)
            return move

def next_turn(the_turn):# принимаем на вход тип фишки (Х или О), который был сделан в качестве последнего хода и возвращает тип фишки, который должен сделать ход следующим
    if the_turn == X:
        return O
    else:
        return X

def play():
    bot,player = get_turn()
    the_turn = X
    play_board = get_new_board()
    show_board(play_board)
    while not get_winner(play_board):#пока не определим победителя, ходит по очереди пользователь и бот
        if the_turn == player:
            move = player_move(play_board,player)
            play_board[move] = player
        else:
            move = bot_move(play_board,bot,player)
            play_board[move] = bot
        show_board(play_board)
        the_turn = next_turn(the_turn)
    
    winner = get_winner(play_board)
    if winner != 'Ничья':
        print('Победитель: ',winner)
    else:
        print('У нас ничья')
    if winner == player:
        print('Вы победили, поздравляем!')
    elif winner == bot:
        print('К сожалению, Вы проиграли')
    elif winner == 'Ничья':
        print('У нас нет победителя на этот раз.')

play()

    
    

    


    








