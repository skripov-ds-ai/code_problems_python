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
    ok = True
    for c in s:
        if c in ps:
            stack.push(c)
        if c in ps_inv:
            if stack.size() == 0:
                ok = False
                break
            else:
                if ps[stack.peek()] != c:
                    ok = False
                    break
                else:
                    stack.pop()
    if stack.size() > 0:
        ok = False
    return ok


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

