class Person:
    arms_count = 2

    def __init__(self):
        self.name = 'test'

    def greet(self):
        print(f'hi {self.name}!')



me = Person()
you = Person()

print(me.arms_count, you.arms_count)

me.arms_count = 5
print(me.arms_count, you.arms_count)

me.name = 'nick'
you.name = 'vasya'

print(me.name,you.name)
me.greet()
you.greet()

me.age = 23
you.age = 45
print(me.age, you.age)