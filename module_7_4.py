print(f'Задача - "Способы форматирования строк"')

team1 = 'Мастера кода'
team2 = 'Волшебники данных'


def number(team1_num=0, team2_num=0):
    print('В команде %s участников: %s, в команде %s участников: %s !' % (team1, team1_num, team2, team2_num))
    print('Итого сегодня в командах  %s и %s участников!' % (team1_num, team2_num))


def time(team1_time=0, team2_time=0,):
    time1 = team1_time
    time2 = team2_time

    print(f'Команды решили {score1} и {score2} задач')
    print('Команда {} решила задач: {}'.format(team2, score2),
          ', а команда {} решила {} задач !'.format(team1, score1))

    time1_average = time1 / score1
    time2_average = time2 / score2
    tasks_total = score1 + score2
    time_avg = tasks_total/(time1+time2)

    print('Команда {} решили задачи за {:.2f} минут '.format(team2, time2),
          ', среднее время {} составило  {:.2f} минут'.format(team2, time2_average))
    print('Команда {} потратила на решение {:.2f} минут !'.format(team1, time1),
          ', среднее время {} составило  {:.2f} минут'.format(team1, time1_average))

    print('Сегодня было решено {} задач, в среднем по {:.2f} минуты на задачу'.format(tasks_total,time_avg))
    if time1_average == time2_average:
        print(f'Победила - "ДРУЖБА!!!"')

    elif time1_average < time2_average:
        print(f'Результат битвы: победа команды {team1} !')

    else:
        print(f'Результат битвы: победа команды {team2} !')



number(team1_num=7, team2_num=6)
score1 = 22
score2 = 26
time(team1_time=132.508314, team2_time=138.56)
# challenge_result()
