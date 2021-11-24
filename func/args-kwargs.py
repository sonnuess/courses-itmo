def fun1(a,b,c):
    return a + b + c


# print(fun(3,7,5))
# print(fun(3,b=7,c=5))
# print(fun(b=7,c=5,a=3))
# print(fun(a=3,7,5))

def fun(a, b, c, d, *args, **kwargs):
    print(args)
    print(kwargs)
    print(a, b, c, d)
    return ''

print(fun(3,7,8,5,6,0,9))
print(fun(3,7,8,5,6,0,9,e=7,f=0))
# homework print(sum(3,4,5))

data = (2, 7, 9, 4)
print(fun(*data))

print(*data, sep='')
print([*data])

another = {'a': 5, 'b': 7, 'c': 6, 'd': 4}
print(fun(**another))