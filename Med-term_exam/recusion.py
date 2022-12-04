
def matryoxhka(n):
    """A dummy docstring."""
    if n == 1:
        print("Матрешечка")
    else:
        print('Вверх матрешки n=', n)
        matryoxhka(n - 1)
        print('Низ матрешки n=', n)

matryoxhka(5)
# This is a placeholder for correct code for this message.
