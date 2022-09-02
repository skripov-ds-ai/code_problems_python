def remove_smiles(s):
    if len(s) <= 2:
        return s
    i = 0
    j = 2
    sc1 = False
    sc2 = False
    arr = []
    while i < len(s):
        # print(f'"{s}"')
        # print(f'"{s[i:]}"')
        # print(i, j)
        if s[i] != ":":
            arr.append(s[i])
            # sc1 = False
            # sc2 = False
            i += 1
            j = i + 2
            continue

        if len(s) != i + 1 and s[i + 1] != "-":
            if len(s) == i + 2:
                arr.append(s[i:i+2])
                break
            else:
                arr.append(s[i:i+1])
            i += 1
            j = i + 2
            # sc1 = False
            # sc2 = False
            continue

        if j == i + 2 and (j >= len(s) or s[j] not in ["(", ")"]):
            arr.append(s[i:i+2])
            i += 2
            j = i + 2
            # sc1 = False
            # sc2 = False
            continue

        if j == i + 2 and s[j] == "(":
            sc1 = True
            j += 1
            continue
        if j == i + 2 and s[j] == ")":
            sc2 = True
            j += 1
            continue

        if (sc1 or sc2) and j >= len(s):
            # print("!")
            break

        if sc1 and s[j] == "(":
            j += 1
            continue
        if sc2 and s[j] == ")":
            j += 1
            continue

        if sc1 and s[j] != "(":
            sc1 = False
            i = j
            j = i + 2
            continue
        if sc2 and s[j] != ")":
            sc2 = False
            i = j
            j = i + 2
            continue
    return "".join(arr)


def remove_smiles_from_face(s):
    if len(s) <= 2:
        return s
    p_types = {"(", ")"}
    i = 0
    j = 2
    p_type = None
    arr = []
    while i < len(s):
        if p_type and j >= len(s):
            break

        if s[i] != ":" or len(s) != i + 1 and s[i + 1] != "-":
            arr.append(s[i])
            i += 1
            j = i + 2
            continue

        if j == i + 2:
            if j >= len(s) or s[j] not in p_types:
                arr.append(s[i:i+2])
                i += 2
                j = i + 2
                continue
            if s[j] in p_types:
                p_type = s[j]

        if p_type and s[j] != p_type:
            p_type = None
            i = j
            j = i + 2
            continue
        j += 1
    return "".join(arr)

# ":-\)+|:-\(+"
cases = [
    "aa :-))( a",
    # -> aa ( a
    ":-:-)))(((",
    # -> :-(((
    "a :-)",
    ":-) a",
    ":-) a :-",
    ":-) a :-)",
    ":-) a :-((( :",
    # неверно, правильно - " a  :"
    ":-)a :-((( :-",
    ":-",
    ":-:",
    ":-:)",
    # неверно, правильно - ":-:)"
    ":--)",
    ":-(-)",
    ":--:()",
    # неверно, правильно - ":--:()"
]

for case in cases:
    tmp = remove_smiles(case)
    tmp1 = remove_smiles_from_face(case)
    print()
    print(f'"{case}" vs "{tmp}"')
    print(f'"{tmp}" vs "{tmp1}"')
    print(tmp == tmp1)
    # print()