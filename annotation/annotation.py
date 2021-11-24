# annotation
class Account:
    amount: int

    def __init__(self, amount: int) -> None:   # need to annotate
        self.amount = amount


def fun(a: int, b: int) -> int:
    return a * b


a: int = 5
print(a)

a = 'hello!'
print(a)

print(fun(4,5))
print(fun(4.6,5))

mike = Account(50)
mikel = Account(150.0)
