import functools
from datetime import date


class User:
    def __init__(self, date_of_birth: date):
        self.date_of_birth = date_of_birth

    @property
    def age(self) -> int:
        today = date.today()
        return today.year - self.date_of_birth.year - (
            (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day)
        )


def check_adult(func):

    @functools.wraps(func)
    def wrapper(user: User, *args, **kwargs):
        if not isinstance(user, User):
            raise TypeError("El parámetro debe ser un objeto User")
        
        if user.age < 18:
            print("El usuario no es mayor de edad")

        return func(user, *args, **kwargs)
    return wrapper

@check_adult
def create_func(user: User):
    print(f"Este usuario tiene : {user.age} años")


user_1 = User(date(1990,5,10))
user_2 = User(date(2005,4,10))
user_3 = User(date(2000,11,15))
user_4 = User(date(2010,10,25))


create_func(user_1)
create_func(user_2)
create_func(user_3)
create_func(user_4)
