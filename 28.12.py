class Checker:
    def __set_first_name__(self, owner, first_name):
        self.first_name__= first_name
    
    def __get__(self, obj, type=None) -> object:
        return


class Person:
    first_name = Checker()

people = Person()
people.first_name = "Aziz"
print(people.first_name)

