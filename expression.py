from stack import Stack


class Expression:
    def __init__(self, phrase, type):
        self.type = type
        self.phrase = phrase
    # def get_type(self):
    #     return self.type
    #
    # def get_statement(self):
    #     return self.phrase

    def is_infix(self):
        pass

    def is_prefix(self):
        pass

    def is_postfix(self):
        pass


def infix_to_postfix(phrase):
    postfix = []
    output = []
    stack = Stack(len(phrase))
    # type = expression.type
    b = True
    for i in phrase.split(" "):
        if i.isalpha() or i.isdigit():
            output.append(i)
            postfix.append(" ".join(output))
            postfix.append(" ".join(stack.array))
            if (not stack.is_empty()) and stack.peek() == '?' and b:
                stack.pop()
                output.append('?')
                postfix.append(" ".join(output))
                postfix.append(" ".join(stack.array))
        elif i == '(':
            stack.push(i)
        elif i == ')':
            while not stack.is_empty() and stack.peek() != '(':
                output.append(stack.peek())
                postfix.append(" ".join(output))
                postfix.append(" ".join(stack.array))
                stack.pop()
            stack.pop()
        elif i != " ":
            try:
                if (i == '-' and stack.peek() == '(') or (i == '-' and stack.is_empty()):
                    stack.push('?')
                else:
                    while not stack.is_empty() and stack.not_greater(i):
                        output.append(stack.peek())
                        postfix.append(" ".join(output))
                        postfix.append(" ".join(stack.array))
                        stack.pop()
                    stack.push(i)
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
        output = list(i)
        output.reverse()
        prefix.append("".join(output))
    return prefix


def prefix_to_infix(expression):
    pass


def postfix_to_prefix(expression):
    pass


def prefix_to_postfix(expression):
    pass


exp = Expression("- x + y * z / ( - w + b ) + u", "infix")
# exp = Expression("222 + b * ( c ^ d - 3547 ) ^ ( f + g * h ) - i", "infix")
# exp = Expression(" -2 + 3 ", "infix")
# print(exp.phrase)
# print("\n".join(infix_to_postfix(exp.phrase)))
# exp1 = Expression("222 ? b c d ^ 3547 - f ? g h * + ^ * + i -", "postfix")
# print(exp1.phrase)
# print("\n".join(postfix_to_infix(exp1.phrase)))
print(exp.phrase)
print("\n".join(infix_to_prefix(exp.phrase)))
