def closed_form_fibonacci(n):
    
    # Refer to https://en.wikipedia.org/wiki/Fibonacci_number for closed form

    phi = (1 + (5 ** (1/2.))) / 2.
    psi = (1 - (5 ** (1/2.))) / 2.

    return int((phi ** n - psi ** n) / (5 ** (1/2.)))


def generate_closed_form_fibonacci_sequence(n):
    return [closed_form_fibonacci(i) for i in range(n)]


def generate_fibonacci_sequence(n):

    F = [0, 1]
    fibonacci_sequence = list()

    for i in range(n):
        if i == 0:
            fibonacci_sequence.append(0)
        elif i == 1:
            fibonacci_sequence.append(1)
        else:
            new_F = F[1] + F[0]
            F[0] = F[1]
            F[1] = new_F
            fibonacci_sequence.append(new_F)
    return fibonacci_sequence

