

# 华为笔试题，逆波兰式求职，利用栈。# 后缀表达式求值

# A5-3+


def doMath(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2


def postfixEval(postfixExpr):
    operandStack = []
    # tokenList = postfixExpr.split()
    tokenList = list(postfixExpr)
    print(tokenList)
    for token in tokenList:
        if token in "0123456789":
            operandStack.append(int(token))
        elif token in "ABCDEF":
        	operandStack.append(ord(token)- ord('A') + 10)
        else:
            operand2 = operandStack.pop()  # 操作数2
            operand1 = operandStack.pop()  # 操作数1
            result = doMath(token, operand1, operand2)
            operandStack.append(result)
    return operandStack.pop()


if __name__ == "__main__":
	print(postfixEval('32+5-'))


