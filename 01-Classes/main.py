class Person:
    arms_count = 2

    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f'hi {self.name}!')


    def __str__(self):
        return f'Person<name={self.name}>'
    def __eq__(self, other):
        return self.name == other.name



me = Person('Nick')
clone = Person('Nick')
you = Person('Vasya')

print(me.arms_count, you.arms_count)

Person.arms_count = 5
print(me.arms_count, you.arms_count)


print(me, you)
print (me== clone)
me.greet()
you.greet()

me.age = 23
you.age = 45
print(me.age, you.age)



