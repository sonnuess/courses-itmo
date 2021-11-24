def fun(a: int, b: int):
    return a + b


s = fun

del fun

# print(fun(8,7)) error 'cause del
print(s(4, 6))



def sound(being: str):
    def quack():
        return 'quack-quack'

    def default():
        return 'Test Test'

    if being == duck:
        return quack
    else:
        return default

duck = sound("duck")
developer = sound("devloper")

print("duck")
print("developer")