from random import randint


class Calculator:

    def __init__(self, difficulty_level: int) -> None:
        self.__difficulty_level: int = difficulty_level
        self.__first_value: int = self.__value_generator
        self.__second_value: int = self.__value_generator
        self.__operation: int = randint(1, 3)
        self.__result: int = self.__result_generator

    @property
    def difficulty(self: object) -> int:
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
        return 0

    @property
    def __result_generator(self) -> int:
        return 0

    def check_result(self, answer: int) -> bool:
        pass

    def show_operation(self) -> None:
        pass

