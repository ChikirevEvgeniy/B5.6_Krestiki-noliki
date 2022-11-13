board = list(range(1, 10))

win_war = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (7, 5, 3)]


def func_board():
    print('-------------')
    for i in range(3):
        print('|', board[0 + i * 3], '|', board[1 + i * 3], '|', board[2 + i * 3], '|')
        print('-------------')


def func_input(simbol):
    while True:
        value = input(f'Введите номер клетки для {simbol}: ')
        if not value in '123456789':
            print('Неверный ввод. Введите число от 1 до 9.')
            continue
        if int(value) > 9:
            print('Неверный ввод. Введите число от 1 до 9.')
            continue
        value = int(value)
        if str(board[value - 1]) in 'XO':
            print('Данная клетка занята. Выберите другую.')
            continue
        board[value - 1] = simbol
        break


def func_win():
    for each in win_war:
        if (board[each[0] - 1]) == (board[each[1] - 1]) == (board[each[2] - 1]):
            return board[each[0] - 1]


def main():
    cnt = 0
    winner = None
    while True:
        func_board()
        if cnt % 2 == 0:
            func_input('X')
        else:
            func_input('O')
        if cnt > 3:
            winner = func_win()
            if winner:
                func_board()
                print(f'Победил {winner}!')
                break
        cnt += 1
        if cnt > 8:
            func_board()
            print('Ничья!')
            break


main()
