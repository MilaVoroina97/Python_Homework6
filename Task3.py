# Напишите программу, которая принимает на стандартный вход список игр футбольных команд с 
# результатом матча и выводит на стандартный вывод сводную таблицу результатов всех матчей.

import itertools
nn = int(input('Введите кол-во завершенных игр: '))
game_input = [input('Введите название команды и кол-во голов через точку с запятой: ').split(';') for x in range(nn)]

teams_vs= [(x[0],x[2])for x in game_input]

teams_name = set(itertools.chain.from_iterable(teams_vs))

game_results = {team : [0, 0, 0, 0, 0] for team in teams_name}#всего игр 0, победы 1, ничья 2, 
#поражения 3, всего очков 4

for team1, goal1, team2, goal2 in game_input:
    game_results[team1][0] +=1#определяем Всегоигр 
    game_results[team2][0] +=1#определяем Всегоигр 
    print(game_results)
    if int(goal1) > int(goal2):
        game_results[team1][1] += 1#кол-во побед
        game_results[team1][4] += 3#прибавляем очки за победы
        game_results[team2][3] += 1#прибавляем проигрыши второй команде
    
    elif int(goal1) < int(goal2):
        game_results[team2][1] += 1
        game_results[team2][4] += 3
        game_results[team1][3] += 1
    
    elif int(goal1) == int(goal2):
        game_results[team1][2] += 1
        game_results[team2][2] += 1
        game_results[team1][4] += 1
        game_results[team2][4] += 1
for team in teams_name:
    print('{}:{}'.format(team,' '.join(map(str,game_results[team]))))









