from stack import Stack


class Expression:
    def __init__(self, phrase, type):
        self.type = type
        self.phrase = phrase


def infix_to_postfix(phrase):
    postfix = []
    output = []
    stack = Stack(len(phrase))
    phrase = phrase.split(" ")
    b = True
    for i in range(len(phrase)):
        if phrase[i].isalpha() or phrase[i].isdigit():
            output.append(phrase[i])
            postfix.append(" ".join(output))
            postfix.append(" ".join(stack.array))
            if (not stack.is_empty()) and stack.peek() == '?' and b:
                stack.pop()
                output.append('?')
                postfix.append(" ".join(output))
                postfix.append(" ".join(stack.array))
        elif phrase[i] == '(':
            stack.push(phrase[i])
        elif phrase[i] == ')':
            while not stack.is_empty() and stack.peek() != '(':
                output.append(stack.peek())
                postfix.append(" ".join(output))
                stack.pop()
            stack.pop()
            postfix.append(" ".join(stack.array))
        elif phrase[i] != " ":
            try:
                if phrase[i] == '-':
                    if phrase[i - 1] == '(' or (stack.is_empty() and len(output) == 0):
                        stack.push('?')
                    else:
                        while not stack.is_empty() and stack.not_greater(phrase[i]):
                            output.append(stack.peek())
                            postfix.append(" ".join(output))
                            postfix.append(" ".join(stack.array))
                            stack.pop()
                        stack.push(phrase[i])
                else:
                    while (not stack.is_empty()) and (stack.not_greater(phrase[i])):
                        output.append(stack.pop())
                        postfix.append(" ".join(output))
                        postfix.append(" ".join(stack.array))
                    stack.push(phrase[i])
            except IndexError:
                stack.push('?')
    while not stack.is_empty():
        output.append(stack.pop())
        postfix.append(" ".join(output))
        postfix.append(" ".join(stack.array))
    return postfix


def postfix_to_infix(phrase):
    stack = Stack(len(phrase))
    infix = []
    for i in phrase.split(" "):
        if i.isalpha() or i.isdigit():
            stack.push(i)
            infix.append(" ".join(stack.array))
        elif i == "?":
            op1 = stack.pop()
            stack.push("(-" + op1 + ")")
            infix.append(" ".join(stack.array))
        else:
            op1 = stack.pop()
            op2 = stack.pop()
            stack.push("(" + op2 + i + op1 + ")")
            infix.append(" ".join(stack.array))
    return infix


def infix_to_prefix(phrase):
    prefix = []
    output = []
    reverse = phrase.split(" ")
    reverse.reverse()
    print(reverse)
    for i in range(len(reverse)):
        if reverse[i] == '(':
            output.append(')')
        elif reverse[i] == ')':
            output.append('(')
        else:
            if reverse[i] == '-' and i == len(reverse) - 1:
                output[- 1] = '( ' + '- ' + output[- 1] + ' )'
            elif reverse[i] == '-' and reverse[i + 1] == '(':
                output[- 1] = '( ' + '- ' + output[- 1] + ' )'
            else:
                output.append(reverse[i])
    output1 = infix_to_postfix(" ".join(output))
    for i in output1:
        output = list(i.split())
        output.reverse()
        prefix.append(" ".join(output))
    return prefix


def prefix_to_infix(phrase):
    stack = Stack(len(phrase))
    reverse = phrase.split(" ")
    reverse.reverse()
    infix = []
    for i in reverse:
        if i.isalpha() or i.isdigit():
            stack.push(i)
            infix.append(" ".join(stack.array))
        else:
            if i == "?":
                op = stack.pop()
                stack.push("(-" + op + ")")
                infix.append(" ".join(stack.array))
            else:
                op1 = stack.pop()
                op2 = stack.pop()
                stack.push("(" + op1 + i + op2 + ")")
                infix.append(" ".join(stack.array))
    return infix


def prefix_to_postfix(phrase):
    stack = Stack(len(phrase))
    reverse = phrase.split(" ")
    reverse.reverse()
    postfix = []
    for i in reverse:
        if i.isalpha() or i.isdigit():
            stack.push(i)
            postfix.append(i)
        elif i == "?":
            op = stack.pop()
            stack.push(op + " " + i)
            postfix.append(op + " " + i)
        else:
            op1 = stack.pop()
            op2 = stack.pop()
            stack.push(op1 + " " + op2 + " " + i)
            postfix.append(op1 + " " + op2 + " " + i)
    return postfix


def postfix_to_prefix(phrase):
    stack = Stack(len(phrase))
    prefix = []
    for i in phrase.split(' '):
        if i.isalpha() or i.isdigit():
            stack.push(i)
            prefix.append(i)
        elif i == '?':
            op = stack.pop()
            stack.push(i + " " + op)
            prefix.append(i + " " + op)
        else:
            op1 = stack.pop()
            op2 = stack.pop()
            stack.push(i + " " + op2 + " " + op1)
            prefix.append(i + " " + op2 + " " + op1)
    return prefix


def isvalid(expression):
    phrase = expression.phrase.split()
    if expression.type == "infix":
        if len(phrase) < 3:
            return False
        elif (phrase[0] in "+*/^?") or (phrase[len(phrase) - 1] in "+-*/^?"):
            return False
        for i in range(len(phrase) - 1):
            if (phrase[i].isalpha() or phrase[i].isdigit()) and (phrase[i + 1].isalpha() or phrase[i + 1].isdigit()):
                print(phrase[i])
                return False
    elif expression.type == "postfix":
        if len(phrase) < 3:
            return False
        elif (phrase[0] in "+-*/^?") or (phrase[len(phrase) - 1].isdigit() or phrase[len(phrase) - 1].isalpha()):
            return False
        for i in range(len(phrase) - 1):
            if phrase[i] in "()":
                return False
    elif expression.type == "prefix":
        if len(phrase) < 3:
            return False
        elif (phrase[len(phrase) - 1] in "+-*/^") or (phrase[0].isdigit() or phrase[0].isalpha()):
            return False
        for i in range(len(phrase) - 1):
            if phrase[i] in "()":
                return False
    return True


def split_checker(phrase):
    for i in phrase.split(' '):
        if ("+" in i or "-" in i or "*" in i or "/" in i or "(" in i or ")" in i or "?" in i) and len(i) > 1:
            return False
    return True
# infix to postfix
# exp = Expression("( ( A - ( B / C ) ) * ( ( A / K ) - L ) )", "infix")  # a + b * ( c ^ d - e ) ^ ( f + g * h ) - i
# print(exp.phrase)
# print("\n".join(infix_to_postfix(exp.phrase)))
# postfix to infix
# exp1 = Expression("A B C / - A K L - / *", "postfix")
# print(exp1.phrase)
# print("\n".join(postfix_to_infix(exp1.phrase)))
# infix to prefix
# exp2 = Expression(" ", "infix")
# print(exp2.phrase)
# print("\n".join(infix_to_prefix(exp2.phrase)))
# prefix to infix
# exp3 = Expression("* - A / B C - / A K L", "prefix")
# print(exp3.phrase)
# print("\n".join(prefix_to_infix(exp3.phrase)))
# prefix to postfix
# exp4 = Expression("* - ? A / B C - / A K L", "prefix")
# print(exp4.phrase)
# print("\n".join(prefix_to_postfix(exp4.phrase)))
# postfix to prefix
# exp5 = Expression("A ? B C / - A K / L - *", "postfix")
# print(exp5.phrase)
# print("\n".join(postfix_to_prefix(exp5.phrase)))
