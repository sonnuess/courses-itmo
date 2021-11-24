print(5 + 7)
print('Hello ' + 'World!')
print([1, 2, 3] + [4, 5, 6])

class Duck:
    def sound(self):
        print('Quack Quack')

class Dog:
    def sound(self):
        print('Bark Bark')

for animal in Dog(), Duck():
    print(animal.sound())