def priority(token):
    if token[1] == '*' or token[1] == '/':
        return 2
    if token[1] == '+' or token [1] == '-':
        return 1
    if token[1] == 'neg':
        return 3
    return -1


def infix_to_postfix(tokens):
    queue = []
    stack = []
    for i in range(len(tokens)):
        if tokens[i][0] == "NUMBER":
            queue.append(tokens[i])
        elif tokens[i][0] == "OPERATOR":
            while len(stack) != 0 and priority(stack[-1]) >= priority(tokens[i]):
                tmp = stack.pop()
                queue.append(tmp)
            stack.append(tokens[i])

        elif tokens[i][0] == "LEFT_P":
            stack.append(tokens[i])
        elif tokens[i][0] == "RIGHT_P":
            while stack[-1][1] != '(':
                tmp = stack.pop()
                queue.append(tmp)
            if stack[-1][1] == '(':
                stack.pop()

        else:
            raise ValueError(f"Неизвестный тип символа: {tokens[i][0]}")
    while len(stack) != 0:
        tmp = stack.pop()
        queue.append(tmp)
    return queue        

def calc(tokens):
    stack = []
    for i in range(len(tokens)):
        if tokens[i][0] == "NUMBER":
            stack.append(tokens[i][1])
        elif tokens[i][1] == 'neg':
            a = float(stack.pop())
            stack.append(a * (-1))
        elif tokens[i][0] == "OPERATOR" and tokens[i][1] != 'neg':
            a = float(stack.pop())
            b = float(stack.pop())
            if tokens[i][1] == '+':
                stack.append(a + b)
            elif tokens[i][1] == '*':
                stack.append(a * b)
            elif tokens[i][1] == '/':
                if a == 0:
                    raise ZeroDivisionError("Ошибка деления на ноль")
                else:
                    stack.append(b / a)
            elif tokens[i][1] == '-':
                stack.append(b - a)

    result = stack.pop()
    return int(result) if result.is_integer() else result
# поддержка отриц чисел