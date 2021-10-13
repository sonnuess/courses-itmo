class Person:
    arms_count = 2

    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f'hi {self.name}!')


    def __del__(self):



me = Person('Nick')
you = Person('Vasya')

print(me.arms_count, you.arms_count)

me.arms_count = 5
print(me.arms_count, you.arms_count)


print(me.name, you.name)
me.greet()
you.greet()

me.age = 23
you.age = 45
print(me.age, you.age)