class Person:

    GENDER = ['male', 'female', 'notsure']

    def __init__(self, first_name, last_name, year_of_birth, gender, stress, coffeedrinker):
        for item in [first_name, last_name, year_of_birth, gender, stress, coffeedrinker]:
            if item == None or item == '':
                raise ValueError('No %s value was given' % item)
        if gender not in self.GENDER:
            raise ValueError('%s is not a valid gender.' % gender)

        self.first_name = first_name
        self.last_name = last_name
        self.year_of_birth = year_of_birth
        self.gender = gender
        self.stress = stress
        self.coffeedrinker = coffeedrinker

    @property
    def full_name(self):
        return '%s %s' % (self.first_name, self.last_name)
