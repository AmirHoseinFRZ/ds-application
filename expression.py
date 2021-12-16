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


def infix_to_postfix(expression):
    postfix = []
    output = []
    phrase = expression.phrase
    stack = Stack(len(phrase))
    # type = expression.type
    b = True
    for i in phrase.split(" "):
        if i.isalpha() or i.isdigit():
            output.append(i)
            postfix.append("output    : " + " ".join(output))
            postfix.append("operators : " + " ".join(stack.array))
            if (not stack.is_empty()) and stack.peek() == '?' and b:
                stack.pop()
                output.append('?')
                postfix.append("output    : " + " ".join(output))
                postfix.append("operators : " + " ".join(stack.array))
        elif i == '(':
            stack.push(i)
        elif i == ')':
            while not stack.is_empty() and stack.peek() != '(':
                output.append(stack.peek())
                postfix.append("output    : " + " ".join(output))
                postfix.append("operators : " + " ".join(stack.array))
                stack.pop()
            stack.pop()
        elif i != " ":
            try:
                if (i == '-' and stack.peek() == '(') or (i == '-' and stack.is_empty()):
                    stack.push('?')
                else:
                    while not stack.is_empty() and stack.not_greater(i):
                        output.append(stack.peek())
                        postfix.append("output    : " + " ".join(output))
                        postfix.append("operators : " + " ".join(stack.array))
                        stack.pop()
                    stack.push(i)
            except IndexError:
                stack.push('?')
    while not stack.is_empty():
        output.append(stack.pop())
        postfix.append("output    : " + " ".join(output))
        postfix.append("operators : " + " ".join(stack.array))
    return "\n".join(postfix)


def postfix_to_infix(expression):
    phrase = expression.phrase
    stack = Stack(len(phrase))
    infix = []
    for i in phrase.split(" "):
        if i.isalpha() or i.isdigit():
            stack.push(i)
            infix.append("output : " + " ".join(stack.array))
        elif i == "?":
            op1 = stack.pop()
            stack.push("(-" + op1 + ")")
            infix.append("output : " + " ".join(stack.array))
        else:
            op1 = stack.pop()
            op2 = stack.pop()
            stack.push("(" + op2 + i + op1 + ")")
            infix.append("output : " + " ".join(stack.array))
    return "\n".join(infix)


def infix_to_prefix(expression):
    pass


def postfix_to_prefix(expression):
    pass


def prefix_to_postfix(expression):
    pass


def prefix_to_infix(expression):
    pass


exp = Expression("- 222 + b * ( c ^ d - 3547 ) ^ ( - f + g * h ) - i", "infix")
# exp = Expression(" -2 + 3 ", "infix")
print(exp.phrase)
print((infix_to_postfix(exp)))
exp1 = Expression("222 ? b c d ^ 3547 - f ? g h * + ^ * + i -", "postfix")
print(exp1.phrase)
print(postfix_to_infix(exp1))
