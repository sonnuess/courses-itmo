from typing import List, Tuple, Dict, Union, Optional

Number = Union[int,float]

def fun(a: Number, b: Number) -> Number:
    return a * b


numbers: List[int] = [5, 7, 5]      # 3.8 version
numbers.append('8')

data: Tuple[str, int] = ('Nick', 23)

another: Dict[str, int] = {'a': 5, 'b': 7, 'c': 6, 'd': 4}

print(fun(5, 6))
print(fun(2, 9.8))

x: Optional[int] = 9
print(x)

x = None
print(x)