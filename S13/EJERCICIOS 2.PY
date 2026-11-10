import functools


def check_num (func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        
        for value in args:
            if not isinstance(value, (int, float)):
                raise TypeError(f"El parámetro '{value}' no es un número")
        
        for key,value in kwargs.items():
            if not isinstance(value, (int, float)):
                raise TypeError(f"El parámetro '{key}={value}' no es un número")
        

        return func(*args, **kwargs)
    return wrapper

@check_num
def create_fun(*args,**kwargs):
    result = (args,kwargs)
    print(result)
    return result

create_fun(1,2,3,4, value=1, number=2)
            