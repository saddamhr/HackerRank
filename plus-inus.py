
def plusMinus(arr):
    positive = negative = zero = 0
    len_arr = len(arr)
    for a in arr:
        if a > 0:
            positive += 1
        elif a < 0:
            negative += 1
        elif a == 0:
            zero += 1
    print("{:.6f}".format(positive/len_arr))
    print("{:.6f}".format(negative/len_arr))
    print("{:.6f}".format(zero/len_arr))


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
