def heapify(data, k, swap):
    l = 2 * k + 1
    r = 2 * k + 2
    if l < len(data) and data[l] < data[k]:
        smallest = l
    else:
        smallest = k
    if r < len(data) and data[r] < data[smallest]:
        smallest = r
    if smallest != k:
        data[k], data[smallest] = data[smallest], data[k]
        swap.append(int(k))
        swap.append(int(smallest))
        heapify(data, smallest, swap)


def build_heap(data):
    swap = []
    n = int((len(data) // 2) - 1)
    for k in range(n, -1, -1):
        heapify(data, k, swap)
    return swap


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n
    swaps = build_heap(data)

    print(int(len(swaps) / 2))
    for i in range(len(swaps)):
        if i % 2 == 0:
            print(str(swaps[i]) + " " + str(swaps[i + 1]))


if __name__ == "__main__":
    main()
