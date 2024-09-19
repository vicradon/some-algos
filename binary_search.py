def binary_search(target, elements):
    l, r = 0, len(elements) - 1

    while l <= r:
        m = (l+r)//2

        if elements[m] == target:
            return True, m
        
        if elements[m] < target:
            l = m + 1
        else:
            r = m - 1

    return False, None


target = -4
elements = [-4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

print(binary_search(target, elements))