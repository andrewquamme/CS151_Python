class Person:

    def __init__(self):
        ## Initialize variables on creation of class object
        name = ''
        age = 0
        sex = ''
        birthYear = 1900

    def getBirthYear(self):
        ## Calculate birth year based on age (year is hard coded)
        self.birthYear = 2018 - self.age

    def description(self):
        ## Create a string describing this "Person"
        desc_str = "%s is a %s year old %s born in %s." % (self.name, self.age,
                                                          self.sex, self.birthYear)
        return(desc_str)
            
Andrew = Person()
Andrew.name='Andrew'
Andrew.age=35
Andrew.sex='Male'
Andrew.getBirthYear()

Jax = Person()
Jax.name='Jax'
Jax.age=26
Jax.sex='Female'
Jax.getBirthYear()

print(Andrew.description())
print(Jax.description())

