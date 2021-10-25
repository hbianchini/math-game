from models.calculator import Calculator


def play(game_points: int) -> None:
    diffilculty: int = int(input('Enter the desired difficulty level [1, 2, 3, 4]: '))
    calc: Calculator = Calculator(diffilculty)

    print('Enter the result of the next operation: ')
    calc.show_operation()

    result: int = int(input())
    if calc.check_result(result):
        game_points += 1
        print(f'You have {game_points} point(s)!')

    continue_game: int = int(input('Do you want to continue the game? [1 - Yes, 0 - No]'))

    if continue_game:
        play(game_points)
    else:
        print(f'You finished the game with: {game_points} point(s).')
        print('See you!')
