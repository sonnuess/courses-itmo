
# 1

def divide(a, b):
   return a / b

try:
    x, y = [int(x) for x in input().split()]
    result = divide(x, y)
    print(result)
except ZeroDivisionError as error:
    print(error)

except ValueError as error:
    print(error)

# 2

def fun(a,b):
    try:
         if a > b:
             return a + b
         else:
             raise ValueError
    except ValueError:
        return 0
    finally:
        return -1

print((fun(2,9)))
