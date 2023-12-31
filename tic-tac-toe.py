from colorama import init
from colorama import Fore, Back, Style


def read_data(filename) -> list:
    '''
    Чтение поля конфигурации из файла "input.txt" в список списков
    '''
    with open(filename) as file:
        tic_tac_toe = [list(line.rstrip()) for line in file]
    return tic_tac_toe


def print_mx(config) -> None:
    '''
    Печать конфигурации поля для игры
    '''
    print()
    for i in config:
        print("\t\t\t \t\t\t\t\t", end="")
        str_to_print = ""
        for j in range(5):
            str_to_print += i[j] + " "
        print(Fore.BLACK + Back.WHITE + str_to_print)
    print()


def transpose(lst) -> list:
    '''
    Транспонирование матрицы
    '''
    zipped_mx = zip(*lst)
    transpose_mx = [list(row) for row in zipped_mx]
    return transpose_mx


def put_x(config, x="x") -> None:
    '''
    Вставляем элемент на первое пустое место в поле
    '''
    for i in range(1, 4):
        for j in range(1, 4):
            if config[i][j] == " ":
                config[i][j] = x
                return


def do_first_round(config, x="x") -> bool:
    '''
    Функция отрабатывает первый раунд алгоритма
    и возвращает True или False в зависимости от того, нашли ли мы подходящий ход

    Из чего состоит раунд:
    1. Ищем линии, где больше одного (x) и ставим (x) в эту же линию
    на пустое место, на чем и заканчиваем работу

    Снизу начинается первый раунд
    '''
    # config - не транспонирован
    for i in range(1, 4):  # проходимся по центральным строкам
        cnt = 0  # счетчик одинаковых (x) в линии
        gap = [-1, -1]  # храним индексы пустого поля в линии
        for j in range(1, 4):  # проходимся по центральным столбцам
            if config[i][j] == " ":
                gap[0], gap[1] = i, j  # получаем индексы пустого поля в линии
            if config[i][j] == x:
                cnt += 1  # увеличиваем счетчик при нахождении (x)
        if cnt > 1 and sum(
                gap) != -2:  # если счетчик больше одного, то сразу ставим (x) в пустое поле и заканчиваем работу
            config[gap[0]][gap[1]] = x
            return True

    transposed_config = transpose(config)  # транспонируем матрицу, чтобы пройтись по столбцам оригинального config
    for i in range(1, 4):  # проходимся по центральным строкам
        cnt = 0  # счетчик одинаковых (x) в линии
        gap = [-1, -1]  # храним индексы пустого поля в линии
        for j in range(1, 4):  # проходимся по центральным столбцам
            if transposed_config[i][j] == " ":
                gap[0], gap[1] = i, j  # получаем индексы пустого поля в линии
            if transposed_config[i][j] == x:
                cnt += 1  # увеличиваем счетчик при нахождении (x)
        if cnt > 1 and sum(
                gap) != -2:  # если счетчик больше одного, то сразу ставим (x) в пустое поле и заканчиваем работу
            transposed_config[gap[0]][gap[1]] = x
            transposed_config = transpose(transposed_config)
            print_mx(transposed_config)
            for x in range(5):
                for y in range(5):
                    config[x][y] = transposed_config[x][y]
            return True

    main_diagonal = [(1, 1), (2, 2), (3, 3)]  # сохраняем индексы элементов из главной диагонали
    sec_diagonal = [(1, 3), (2, 2), (3, 1)]  # сохраняем индексы элементов из побочной диагонали
    cnt = 0  # счетчик одинаковых (x) в линии
    gap = [-1, -1]  # храним индексы пустого поля в линии

    for i in main_diagonal:  # проходимся по главной диагонали
        if config[i[0]][i[1]] == " ":
            gap[0], gap[1] = i[0], i[1]  # получаем индексы пустого поля в линии
        if config[i[0]][i[1]] == x:
            cnt += 1  # увеличиваем счетчик при нахождении (x)
    if cnt > 1 and sum(gap) != -2:  # если счетчик больше одного, то сразу ставим (x) в пустое поле и заканчиваем работу
        config[gap[0]][gap[1]] = x
        return True

    cnt = 0  # счетчик одинаковых (x) в линии
    gap = [-1, -1]  # храним индексы пустого поля в линии
    for i in sec_diagonal:  # проходимся по побочной диагонали
        if config[i[0]][i[1]] == " ":
            gap[0], gap[1] = i[0], i[1]  # получаем индексы пустого поля в линии
        if config[i[0]][i[1]] == x:
            cnt += 1  # увеличиваем счетчик при нахождении (x)
    if cnt > 1 and sum(gap) != -2:  # если счетчик больше одного, то сразу ставим (x) в пустое поле и заканчиваем работу
        config[gap[0]][gap[1]] = x
        return True

    # Возвращаем False, т.к. не нашли лучшего хода
    return False


def do_second_round(config, x="x") -> bool:
    '''
    Функция отрабатывает второй раунд алгоритма
    и возвращает True или False в зависимости от того, нашли ли мы подходящий ход

    Из чего состоит раунд:
    1. Ищем линии, где больше одного (x) и ставим противоположный (x) элемент в эту же линию
    на пустое место, на чем и заканчиваем работу

    Снизу начинается второй раунд
    '''
    # config - не транспонирован
    for i in range(1, 4):  # проходимся по центральным строкам
        cnt = 0  # счетчик одинаковых (x) в линии
        gap = [-1, -1]  # храним индексы пустого поля в линии
        for j in range(1, 4):  # проходимся по центральным столбцам
            if config[i][j] == " ":
                gap[0], gap[1] = i, j  # получаем индексы пустого поля в линии
            if config[i][j] == x:
                cnt += 1  # увеличиваем счетчик при нахождении (x)
        if cnt > 1 and sum(
                gap) != -2:  # если счетчик > 1, то сразу ставим противоположный (x) элемент в пустое поле и заканчиваем работу
            config[gap[0]][gap[1]] = ("o" if x == "x" else "x")
            return True

    transposed_config = transpose(config)  # транспонируем матрицу, чтобы пройтись по столбцам оригинального config
    for i in range(1, 4):  # проходимся по центральным строкам
        cnt = 0  # счетчик одинаковых (x) в линии
        gap = [-1, -1]  # храним индексы пустого поля в линии
        for j in range(1, 4):  # проходимся по центральным столбцам
            if transposed_config[i][j] == " ":
                gap[0], gap[1] = i, j  # получаем индексы пустого поля в линии
            if transposed_config[i][j] == x:
                cnt += 1  # увеличиваем счетчик при нахождении (x)
        if cnt > 1 and sum(
                gap) != -2:  # если счетчик > 1, то сразу ставим противоположный (x) элемент в пустое поле и заканчиваем работу
            transposed_config[gap[0]][gap[1]] = ("o" if x == "x" else "x")
            transposed_config = transpose(transposed_config)
            for x in range(5):
                for y in range(5):
                    config[x][y] = transposed_config[x][y]
            return True

    main_diagonal = [(1, 1), (2, 2), (3, 3)]  # сохраняем индексы элементов из главной диагонали
    sec_diagonal = [(1, 3), (2, 2), (3, 1)]  # сохраняем индексы элементов из побочной диагонали
    cnt = 0  # счетчик одинаковых (x) в линии
    gap = [-1, -1]  # храним индексы пустого поля в линии

    for i in main_diagonal:  # проходимся по главной диагонали
        if config[i[0]][i[1]] == " ":
            gap[0], gap[1] = i[0], i[1]  # получаем индексы пустого поля в линии
        if config[i[0]][i[1]] == x:
            cnt += 1  # увеличиваем счетчик при нахождении (x)
    if cnt > 1 and sum(
            gap) != -2:  # если счетчик > 1, то сразу ставим противоположный (x) элемент в пустое поле и заканчиваем работу
        config[gap[0]][gap[1]] = ("o" if x == "x" else "x")
        return True

    cnt = 0  # счетчик одинаковых (x) в линии
    gap = [-1, -1]  # храним индексы пустого поля в линии
    for i in sec_diagonal:  # проходимся по побочной диагонали
        if config[i[0]][i[1]] == " ":
            gap[0], gap[1] = i[0], i[1]  # получаем индексы пустого поля в линии
        if config[i[0]][i[1]] == x:
            cnt += 1  # увеличиваем счетчик при нахождении (x)
    if cnt > 1 and sum(
            gap) != -2:  # если счетчик > 1, то сразу ставим противоположный (x) элемент в пустое поле и заканчиваем работу
        config[gap[0]][gap[1]] = ("o" if x == "x" else "x")
        return True

    # Возвращаем False, т.к. не нашли лучшего хода
    return False


def do_best_step_for_xs(config, x="x") -> None:
    '''
    Функция основного алгоритма

    Из чего состоит алгоритм:
    1. Отработка раундов:
        -Раунд №1 - нацелен на поиск линий в поле, где стоят два одинаковых (x),
        чтобы дополнить линию до трех одинаковых (x)
        -Раунд №2 - нацелен на поиск линий в поле, где стоят два одинаковых противоположных (x) элемента,
        чтобы не дать противнику собрать три одинаковых элемента в линии, мы вставляем в пустое поле (x)
    '''
    # отрабатываем первый раунд
    if do_first_round(config, x) is False:  # если не нашли лучший ход, отрабатываем второй раунд
        if do_second_round(config, x=("o" if x == "x" else "x")) is False:  # если не нашли лучший ход за второй раунд
            '''
            Вставляем элемент на первое пустое место по приоритетности

            Приоритеты:
            1. Центр
            2. Углы или Ребра
            '''
            if config[2][2] == " ":
                config[2][2] = x
            else:
                put_x(config, x)
        else:
            return
    else:
        return


if __name__ == "__main__":
    '''
    Основная функция программы.

    file_data -- двумерный массив (хранит в себе все конфигурации полей)
    '''
    init(autoreset=True)

    print(Style.BRIGHT + """
    ╔══════════════════════════════════════════════════════════════════╗
    ║   Программа по нахождению лучшего ходя для игры крестики-нолики  ║
    ╚══════════════════════════════════════════════════════════════════╝
    """)

    # считываем данные из файла
    file_data = read_data(r"input.txt")
    for i in range(0, len(file_data), 5):  # проходимся по file_data, чтобы найти лучший ход для каждой конфигурации
        config_for_x = []  # инициализация списка, для хранения конфигурации поля
        j = i  # инициализация индекса для работы цикла
        while j < (i + 5):  # проходимся по отрезку списка file_data, чтобы считать кон-цию поля
            config_for_x.append(file_data[j])  # обновляем список
            j += 1  # увеличиваем индекс

        # начинается работа с, уже хранящейся в config_for_x, кон-цией
        print(
            "\t\t\t " + Style.BRIGHT + "======================" + Fore.YELLOW + "ORIG" + Fore.RESET + "======================")
        print_mx(config_for_x)  # Выводим изначальную конфигурацию
        config_for_o = config_for_x.copy()  # Создаем копию

        print(
            "\t\t\t " + Style.BRIGHT + "==================" + Fore.GREEN + "BEST_FOR_X's" + Fore.RESET + "==================")
        do_best_step_for_xs(config_for_x, x="x")  # выполняем алгоритм для нахождения лучшего хода, играя за "x"
        print_mx(config_for_x)

        # print("==================BEST_FOR_O's======================")
        # do_best_step_for_xs(config_for_o, x="o")  # выполняем алгоритм для нахождения лучшего хода, играя за "o"
        # print_mx(config_for_o)

        print(
            "\t\t\t " + Style.BRIGHT + "====================" + Fore.RED + "THE_END" + Fore.RESET + "=====================\n\n\n\n\n")
