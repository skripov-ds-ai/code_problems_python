def form_balanced_bst_array(a, idx):
    result_idxs = []
    if a:
        median = len(a) // 2
        result_idxs.append((idx, a[median]))
        new_idx = 2 * idx + 1
        left = form_balanced_bst_array(a[:median], new_idx)
        result_idxs.extend(left)
        right = form_balanced_bst_array(a[median + 1:], new_idx + 1)
        result_idxs.extend(right)
    return result_idxs


def GenerateBBSTArray(a):
    a = sorted(a)
    result = [None] * len(a)
    idxs_tuple = form_balanced_bst_array(a, 0)
    for i, j in idxs_tuple:
        result[i] = j
    return result
