from typing import Any, Generator


def repeater(value: Any) -> Generator:
    while True:
        yield value


#for item in repeater(5):
#    print(5)

# Импортируем класс Iterator для аннотации
from collections.abc import Iterator    # либо ->  from typing import Any, Generator


# Функция-генератор для степеней двойки
def pow_twelve(max_pow: int) -> Iterator:
    cur_pow = 0

    while cur_pow <= max_pow:
        # Вот тут и происходит магия: когда функция
        # будет вызвана повторно, она начнётся не с начала,
        # а со строчки после yield
        yield 12 ** cur_pow
        cur_pow += 1


