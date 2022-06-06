

def miniMaxSum(arr):
    # Write your code here
    arr_sum = 0
    min_el = max_el = arr[0]
    for a in arr:
        arr_sum += a

        if a < min_el:
            min_el = a
        if a > max_el:
            max_el = a

    print(arr_sum - max_el, arr_sum - min_el)


if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
