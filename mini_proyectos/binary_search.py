#Forma mala
def naive_search(l, target):
    for i in range(len(l)):
        if l[i] == target:
            return i

    return -1

#Forma buena
def binary_search(l, target, high = None, low = None):
    if high == None:
        high = len(l) - 1

    if low == None:
        low = 0

    mid_point = (low + high) // 2

    if target > l[-1] or target < l[0]:
        return -1

    if l[mid_point] == target:
        return mid_point

    if l[mid_point] > target:
        return binary_search(l, target, low, mid_point - 1)

    return binary_search(l, target, mid_point + 1, high)


if __name__ == "__main__":
    lis = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(binary_search(lis, 9))
