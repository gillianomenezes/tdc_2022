import itertools

def agrupador(inputs, n):
    iters = [iter(inputs)]*n
    return itertools.zip_longest(*iters, fillvalue=None)


def agrupador_naive(iterator, n):
    num_grupos = len(iterator) // n
    return [
      tuple(iterator[i*n:(i+1)*n])  for i in range(num_grupos)
    ]


if __name__ == '__main__':
    agrupador(range(100_000_000), n=2)