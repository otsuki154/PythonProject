import random
class People:
    def __init__(self, eyeColor, skinColor, hairColor):
        self.eyeColor = eyeColor
        self.skinColor = skinColor
        self.hairColor = hairColor

class EuropeanPeople():
    def __init__(self, country):
        self.people = People('blue','white','blond')
        self.country = country

    def goodAtArtSport(self):
        print('%s good at Art and Sport' % self.country)

    def __str__(self):
        return "%s person has %s eye, %s skin, %s hair" % (self.country, self.people.eyeColor, self.people.skinColor, self.people.hairColor)


class AsiaPeople(People):
    def __init__(self, country):
        self.people = People('black','yellow','black')
        self.country = country

    def goodAtMath(self):
        print('%s good at Math' % self.country)

    def __str__(self):
        return "%s person has %s eye, %s skin, %s hair" % (
        self.country, self.people.eyeColor, self.people.skinColor, self.people.hairColor)


swedishPeople = EuropeanPeople('Sweden')
print(swedishPeople)

japanesePeople = AsiaPeople('Japanese')
print(japanesePeople)



