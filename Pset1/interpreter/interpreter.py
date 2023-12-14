def main():

    expr = input('Expression: ')
    exprs = expr.split(' ')

    x, y, z = float(exprs[0]) , exprs[1], float(exprs[2])

    if y == '+':
        print(x + z)
    elif y == '-':
        print(x - z)
    elif y == '*':
        print(x * z)
    elif y == '/':
        print(x / z)

main()
