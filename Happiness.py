import numpy as np
c1 = 51
c2 = 400
c3 = 10000

def get_hap(child,gift):

    #hapiness of child
    h4c = dict()
    n   = child.shape[1]

    for i in range(0, c1):
        node = i - (i % 3)
        for j in range(n):
            if (node, child[i][j]) in h4c:
                h4c[(node, child[i][j])] += 10 * (1 + (n - j) * 2)
            else:
                h4c[(node, child[i][j])] = 10 * (1 + (n - j) * 2)

    for i in range(c1, c1+c2):
        node = i + (i % 2)
        for j in range(n):
            if (node, child[i][j]) in h4c:
                h4c[(node, child[i][j])] += 10 * (1 + (n - j) * 2)
            else:
                h4c[(node, child[i][j])] = 10 * (1 + (n - j) * 2)

    for i in range(c1+c2, c3):
        for j in range(n):
            h4c[(i, child[i][j])] = 10 * (1 + (n - j) * 2)

    # hapiness for santa
    h4s = dict()
    for i in range(gift.shape[0]):
        for j in range(gift.shape[1]):
            cur_child = gift[i][j]
            if cur_child < c1:
                cur_child -= cur_child % 3
            elif cur_child < c1+c2:
                cur_child += cur_child % 2
            h4s[(cur_child, i)] = (1 + (gift.shape[1] - j) * 2)


    # for cutting some edges, if they ain't liked by each other.
    positive_cases = list(set(h4c.keys()) | set(h4s.keys()))
    print('Positive case tuples (child, gift): {}'.format(len(positive_cases)))

    # final happiness dictionary
    h = dict()
    for p in positive_cases:
        h[p] = 0
        if p in h4c:
            a = h4c[p]
            h[p] += int((a ** 3) * 4)
        if p in h4s:
            b = h4s[p]
            h[p] += int((b ** 3) / 4)

    return h
