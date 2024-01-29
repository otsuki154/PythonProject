import random
class People:
    def __init__(self, eyeColor, skinColor, hairColor):
        self.eyeColor = eyeColor
        self.skinColor = skinColor
        self.hairColor = hairColor

class EuropeanPeople(People):
    def __init__(self, country):
        People.__init__(self,'blue','white','blond')
        self.country = country

    def goodAtArtSport(self):
        print('%s good at Art and Sport' % self.country)

    def __str__(self):
        return "%s person has %s eye, %s skin, % hair" % (self.country, self.eyeColor, self.skinColor, self.hairColor)


class AsiaPeople(People):
    def __init__(self, country):
        People.__init__(self,'black','yellow','black')
        self.country = country

    def goodAtMath(self):
        print('%s good at Math' % self.country)

    def __str__(self):
        return "%s person has %s eye, %s skin, % hair" % (self.country, self.eyeColor, self.skinColor, self.hairColor)


swedishPeople = EuropeanPeople('Sweden')
print(swedishPeople)

japanesePeople = AsiaPeople('Japanese')
print(japanesePeople)


class EuroAsiaPeople(EuropeanPeople,AsiaPeople):
    def __init__(self, motherCountry, fatherCountry):
        self.country = "%s - %s" % (motherCountry, fatherCountry)
        self.eyeColor = random.choice(['blue','black','dark blue'])
        self.hairColor = random.choice(['blond','black','red'])
        self.skinColor = random.choice(['white','yellow','pink'])

    def __str__(self):
        return "%s person has %s eye, %s skin, %s hair" % (self.country, self.eyeColor, self.skinColor, self.hairColor)

japaneseSweden = EuroAsiaPeople('Swedish','Japanese')
print(japaneseSweden)

#Thua huong 2 phuong thuc cua class cha
japaneseSweden.goodAtArtSport()
japaneseSweden.goodAtMath()

#print cac doi tuong class
print(type(japaneseSweden).__name__)
print(japaneseSweden.__class__.__name__)

print(japaneseSweden.__class__.__base__)
print(japaneseSweden.__class__.__bases__)

print(japaneseSweden.__class__.__bases__[0].__name__)
print(japaneseSweden.__class__.__bases__[1].__name__)


