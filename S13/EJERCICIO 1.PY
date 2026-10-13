import functools


def print_wrapper (func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        param_names = func.__code__.co_varnames
        all_params = {param_names[i]: arg for i, arg in enumerate(args)}
        all_params.update(kwargs)
        param_str = " -- ".join(f"{k}: {v}" for k, v in all_params.items())
        print(f"{param_str}")   
        # print(args)
        # print(kwargs)
        result = func(*args,**kwargs)
        print (result)
        return result
    return wrapper
    
@print_wrapper
def create_print(name,age,type, attack=0, defense=0):
    
    return f"Este pokemon se llama; {name}, es de tipo: {type}, posee un ataque de: {attack}, una defensa de: {defense}, y una edad aproximada de: {age} años"


create_print("Avalugg", 5, "fuerza", attack=50, defense=200)