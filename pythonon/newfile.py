class Animal:
    def __init__(self, can_move, heterotrophs, glikogen):
        self.can_move = 'can move'
        self.heteretrophs = 'heterotrophs'
        self.glikogen = 'glikogen'

    def __str__(self):
        return f'\n Animals - {self.can_move}\n'\
               f'nutrition type - {self.heteretrophs}\n'\
               f'compound of cells - {self.glikogen}'


class Reptilies(Animal):
    def __init__(self, can_move, heterotrophs, glikogen, name, family, reproduction, avarage_height, skin, bloodtemperature):
        super().__init__(can_move, heterotrophs, glikogen)
        self.name = name
        self.family = family
        self.reproduction = reproduction
        self.avarage_height = avarage_height
        self.skin = skin
        self.bloodtemp = bloodtemperature

    def condition(self, temperature ):
        if temperature <= -1 :
            print (f'{self.name} gets anabios')
        else:
            print (f'{self.name} does not get anabios')

    def __str__(self):
        return super(Animal, self).__str__()+f'\nName - {self.name}\n' \
                                            f'familly - {self.family}\n' \
                                            f'reproduction - {self.reproduction}\n'\
                                            f'avarage height - {self.avarage_height}\n'\
                                            f'skin - {self.skin}\n'\
                                            f'temperature of blood - {self.bloodtemp}'

class Mammals(Animal):
    def __init__(self, can_move, heterotrophs, glikogen, wood, name, families, glans, reproduction, avarage_heiht, feeding_with_milk):
        super().__init__(can_move, heterotrophs, glikogen)
        self.wood = wood
        self.glans = glans
        self.feed = feeding_with_milk
        self.avarageh = avarage_heiht
        self.repr = reproduction
        self.name = name
        self.fammilies = families
        self.reproduction = reproduction

    def food(self, food):
        if food == 'plants':
            print (f'{self.name} - herbovarous')
        else:
            print (f'{self.name} - predator')

    def __str__(self):
        return super(Animal, self).__str__()+f'\n Name - {self.name}\n' \
                                            f'familly - {self.fammilies}\n' \
                                            f'reproduction - {self.reproduction}\n'\
                                            f'avarage height - {self.avarageh}\n'\
                                            f'feeding with - {self.feed}\n'\
                                            f'glans - {self.glans}\n' \
                                            f'wool - {self.wood}\n'

b = Mammals(can_move='can move', heterotrophs='heteerotrophs', glikogen='glikogen', name='cat', families ='felidae', reproduction='3-4 kittens per year', avarage_heiht='24 cm', feeding_with_milk='milk', glans='sweeting', wood='short wool')
c = Reptilies('can move', 'heteerotrophs', 'glikogen','python', 'pythonidea', '3-11 eggs per year', '2 m', 'scales', '60F')
a = Animal('can move', 'heteerotrophs', 'glikogen')
print(a)
print (b)
b.food('meat')

print(c)
c.condition(-1)

