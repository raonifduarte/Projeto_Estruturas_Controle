
def fibonacci(quantidade, sequencia=(0, 1)):
    # importante: COndição de parada
    if len(sequencia) == quantidade:
        return sequencia
    return fibonacci(quantidade, sequencia + (sum(sequencia[-2:]),))


if __name__ == '__main__':
    for fib in fibonacci(12):
        print(fib)
