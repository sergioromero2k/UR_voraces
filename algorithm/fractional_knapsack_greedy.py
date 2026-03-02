#!/usr/bin/en python3

"""
def get_best_item(candidates, v, w):
    # O(n)
    best_item = 0
    best_radio = 0
    for c in candidates:
        ratio = v[c] / w[c]
        if ratio > best_radio:
            best_item = c
            best_radio = ratio
    return best_item


def greedy_knapsack(v, w, W):
    # Time Complexity: O(n^2)
    # Space Complexity: O(n)

    candidates = set()
    n = len(v)
    for i in range(n):
        candidates.add(i)
    sol = [0] * n
    weight = 0
    while candidates and weight < W:
        best = get_best_item(candidates, v, w)
        candidates.remove(best)
        if w[best] + weight < W:
            sol[best] = 1
            weight += w[best]
        else:
            sol[best] = (W -weight) / w[best]
            weight = W
    return sol
"""

def knapsack_greedy(w, v, capacity):
    """
    # Time Complexity: O(n log n)
    # Space Complexity: O(n)
    """
    n = len(w)
    idx = list(range(n))
    ratios = [v[i] / w[i] for i in range(n)]

    idx.sort(key=lambda i: ratios[i], reverse=True)
    x = [0] * n
    w_c = 0
    v_t = 0

    for i in idx:
        if capacity > 0:
            if w_c +w[i] <= capacity:
                x[i] = 1
                w_c += w[i]
                v_t += v[i]
            else:
                f = (capacity - w_c) / w[i]
                x[i] = round(f, 2)
                v_t += v[i] * f
                capacity = 0
    return x, v_t



def main() -> None:
    v = [20, 30, 66, 40, 60]
    w = [10, 20, 30, 40, 50]
    W = 100

    proporciones, valor_max = knapsack_greedy(w, v, W)
    print(f"Proporciones elegidas (x_i): {proporciones}")
    print(f"Valor total obtenido: {valor_max}")

if __name__ == '__main__':
    main()
