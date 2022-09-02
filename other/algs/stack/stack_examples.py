from string import whitespace
from other.algs.stack.stack import Stack
parentheses = {
    '(': ')',
    '[': ']',
    '{': '}',
}
operations = {
    '+': lambda x, y: x + y,
    '*': lambda x, y: x * y,
}


def right_parentheses_sequence(s, ps):
    ps_inv = {v: k for k, v in ps.items()}
    stack = Stack()
    for c in s:
        if c in ps:
            stack.push(c)
        if c in ps_inv:
            if stack.size() == 0:
                return False
            else:
                if ps[stack.peek()] != c:
                    return False
                else:
                    stack.pop()
    if stack.size() > 0:
        return False
    return True


def eval_postfix(s, ops):
    eq = '='
    stack2 = Stack()
    # it is valid if number base is 10
    # what to do with unary/n-ary operations?
    base = 10
    num = 0
    prev_zero = False
    # stack1 and tmp stack use for moving from string to stack with postfix statement
    for c in s:
        if c.isdigit():
            num *= base
            num += int(c)
            prev_zero = not bool(int(c))
        elif c in whitespace:
            if prev_zero or num > 0:
                stack2.push(num)
            num = 0
            prev_zero = False
        elif c in ops:
            stack2.push(c)
        elif c == eq:
            stack2.push(c)
    stack1 = Stack()
    while stack2.size() > 0:
        stack1.push(stack2.pop())
    # stack1 = stack2
    # stack1.stack.print_all_nodes()
    # print()

    while stack1.size() > 0:
        elem = stack1.pop()
        if isinstance(elem, int):
            stack2.push(elem)
        elif elem in ops:
            # only binary operations
            a, b = stack2.pop(), stack2.pop()
            c = ops[elem](a, b)
            stack2.push(c)
            # stack2.stack.print_all_nodes()
            # print()
        elif elem == eq:
            stack2.stack.print_all_nodes()


def eval_postfix_simple(s):
    stack2 = Stack()
    num = 0
    prev_zero = False
    for c in s:
        if c.isdigit():
            num *= 10
            num += int(c)
            prev_zero = not bool(int(c))
        elif c == ' ':
            if prev_zero or num > 0:
                stack2.push(num)
            num = 0
            prev_zero = False
        elif c == '=' or c == '+' or c == '*':
            stack2.push(c)
    stack1 = Stack()
    while stack2.size() > 0:
        stack1.push(stack2.pop())

    while stack1.size() > 0:
        elem = stack1.pop()
        if elem == '+' or elem == '*':
            a, b = stack2.pop(), stack2.pop()
            c = a + b if elem == '+' else a * b
            stack2.push(c)
        elif elem == '=':
            stack2.stack.print_all_nodes()
        else:
            stack2.push(elem)


def right_parentheses_sequence_simple(s):
    stack = Stack()
    for c in s:
        if c == '(':
            stack.push(c)
        if c == ')':
            if stack.size() == 0:
                return False
            else:
                if stack.peek() != '(':
                    return False
                else:
                    stack.pop()
    if stack.size() > 0:
        return False
    return True


eval_postfix_simple("8 2 + 5 * 9 + =")
