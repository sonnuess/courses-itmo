class GeometryError(ValueError):
    def __init__(self, description):
        self.description = description

    def __str__(self):
        return self.description

def fun(a,b):
    if isinstance(a,int):
        return a / b
    raise GeometryError('ошибка')

print(fun('a',5))


