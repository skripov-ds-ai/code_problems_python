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


# s1 = "()()"
# r1 = right_parentheses_sequence(s1, parentheses)
# print(r1)


def postfix(s, ops, ps):
    # ps_inv = {v: k for k, v in ps.items()}
    # s1 = Stack()
    # s2 = Stack()
    # for c in s:
    #     if c in ps:
    #
    #     # if c.isdigit():
    #     #     s1.
    pass


def eval_postfix(s, ops):
    eq = '='
    stack1, stack2 = Stack(), Stack()
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
                stack1.push(num)
            num = 0
            prev_zero = False
        elif c in ops:
            stack1.push(c)
        elif c == eq:
            stack1.push(c)
    tmp = Stack()
    while stack1.size() > 0:
        tmp.push(stack1.pop())
    stack1 = tmp
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


eval_postfix("1 1 + 1 * =", operations)
