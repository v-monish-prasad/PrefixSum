def prefixSum(array):
    if not array:
        return "Empty Array."

    prefixSum = []
    prefixSum.append(array[0])

    for i in range(1, len(array)):
        prefixSum.append(prefixSum[i - 1] + array[i])

    return prefixSum


if __name__ == "__main__":
    array = list(map(int, input().strip('[').strip(']').split(',')))
    print(prefixSum(array))
