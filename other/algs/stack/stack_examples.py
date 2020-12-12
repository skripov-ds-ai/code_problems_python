from other.algs.stack.stack import Stack
parentheses = {
    '(': ')',
    '[': ']',
    '{': '}',
}


def right_parentheses_sequence(s, ps):
    ps_inv = {v: k for k, v in ps.items()}
    stack = Stack()
    ok = True
    for c in s:
        if c in ps:
            stack.push(c)
        if c in ps_inv:
            if ps[stack.peek()] != c:
                ok = False
            else:
                stack.pop()
    if stack.size() > 0:
        ok = False
    return ok


s1 = "(())"
r1 = right_parentheses_sequence(s1, parentheses)
print(r1)
