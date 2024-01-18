def squares(*n) -> list:

    return [pow(i, 2) for i in n]

def run_function(f, *number) -> list:
    return f(*number)

print(squares(7, 5, 2))
print(run_function(squares, 9))
