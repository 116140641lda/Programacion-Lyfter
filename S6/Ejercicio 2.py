def call_var (var):
    for index, number in enumerate(var):
        var[index] = number * 5


def call_outside ():
    var = [80,50,100]
    call_var(var)
    print(var)


call_outside()