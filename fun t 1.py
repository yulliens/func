def print_label():
    print('Колледж Сириус')
    print('Имя:')
    print('Группа:')
    amount = int(input('Число учеников:'))
    for i in range(amount):
        print_label()
    print('Готово! Заберите бэйджики.')