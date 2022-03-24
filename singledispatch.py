import functools

def add_sem_functools(a, b):
    if type(a) and type(b) == int:
        return f"A soma e: {a + b}"

    elif type(a) and type(b) == str:
        return f"Concatenando fica: {a + b}"

@functools.singledispatch
def add(a, b):
    raise NotImplementedError("Nao suportado")

@add.register(float)
@add.register(int)
def _(a, b):
    return f"A soma e: {a + b}"

@add.register(str)
def _(a, b):
    return f"Concatenando fica: {a + b}"