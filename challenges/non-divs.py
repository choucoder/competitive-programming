def solve(s, subset, k):
    if not s:
        print(f"subset: {subset}")
        return

    si = s.pop(0)
    lsubset = subset[: ]
    lsubset.append(si)
    rsubset = subset[: ]

    solve(s[:], lsubset, k)
    solve(s[:], rsubset, k)

def non_divisible_subset(s, subset, k):
    if not s:
        print(f"Divisible subset: {subset}")
        return len(subset)

    s0 = s.pop(0)
    is_non_divisible_subset = True

    for si in subset:
        if ((s0 + si) % k) == 0:
            is_non_divisible_subset = False
            break

    len_left = -1
    if is_non_divisible_subset:
        left_subset = subset[:]
        left_subset.append(s0)
        len_left = non_divisible_subset(s[:], left_subset, k)

    right_subset = subset[: ]
    len_right = non_divisible_subset(s[: ], right_subset, k)

    return max(len_left, len_right)

if __name__ == '__main__':
    s = [19, 10, 12, 10, 24, 25, 22]
    k = 4
    print(f"Case #1: {non_divisible_subset(s, [], k)}")