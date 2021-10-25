from random import randint


class Calculator:

    def __init__(self, difficulty_level: int) -> None:
        self.__difficulty_level: int = difficulty_level
        self.__first_value: int = self.__value_generator
        self.__second_value: int = self.__value_generator
        self.__operation: int = randint(1, 3)
        self.__result: int = self.__result_generator

    @property
    def difficulty(self) -> int:
        return self.__difficulty_level

    @property
    def first_value(self) -> int:
        return self.__first_value

    @property
    def second_value(self) -> int:
        return self.__second_value

    @property
    def operation(self) -> int:
        return self.__first_value

    @property
    def result(self) -> int:
        return self.__result

    def __str__(self) -> str:
        opr: str = ''
        if self.__operation == 1:
            opr = 'Sum'
        elif self.__operation == 2:
            opr = 'Sub'
        elif self.__operation == 3:
            opr = 'Mult'
        return f'1st Value: {self.__first_value}\n' \
               f'2nd Value: {self.__second_value}\n' \
               f'Difficulty: {self.__difficulty_level}\n' \
               f'Operation: {opr}\n'

    @property
    def __value_generator(self) -> int:
        if self.__difficulty_level == 1:
            return randint(0, 10)
        elif self.__difficulty_level == 2:
            return randint(0, 100)
        elif self.__difficulty_level == 3:
            return randint(0, 1000)
        elif self.__difficulty_level == 4:
            return randint(0, 10000)
        else:
            return randint(0, 100000)

    @property
    def __result_generator(self) -> int:
        if self.__operation == 1:
            return self.__first_value + self.__second_value
        elif self.__operation == 2:
            return self.__first_value - self.__second_value
        else:
            return self.__first_value * self.__second_value

    @property
    def __op_symbol(self) -> str:
        if self.__operation == 1:
            return '+'
        elif self.__operation == 2:
            return '-'
        else:
            return '*'

    def check_result(self, answer: int) -> bool:
        check_answer: bool = False
        if self.__result == answer:
            print('Correct answer!')
            check_answer = True
        else:
            print('Wrong answer!')
        print(f'{self.__first_value} {self.__op_symbol} {self.__second_value} = {self.__result}')
        return check_answer

    def show_operation(self) -> None:
        print(f'{self.__first_value} {self.__op_symbol} {self.__second_value} = ?')
