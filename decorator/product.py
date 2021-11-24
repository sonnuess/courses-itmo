def time_it(func):
    def how_long(*args, **kwargs):
        import time
        tic = time.thread_time()
        func(*args, **kwargs)
        toc = time.thread_time()
        print(f"lasts {toc - tic} second")
        return ' '
    return how_long


@time_it
def product(a, *args) -> int or None:
    result = a
    for i in args:
        result *= i
    return print(result)


print(product(1, 2, 3, 4))
