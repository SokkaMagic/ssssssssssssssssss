# Exercise 1
def find_closest(data, target):
    left = 0
    right = len(data) - 1

    while left <= right:
        mid = (left + right) // 2

        if data[mid] == target:
            return data[mid]
        elif data[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    if right < 0:
        return data[left]
    if left >= len(data):
        return data[right]

    if target - data[right] <= data[left] - target:
        return data[right]
    else:
        return data[left]


# Exercise 2
def integer_sqrt(n):
    left = 0
    right = n
    answer = 0

    while left <= right:
        mid = (left + right) // 2

        if mid * mid <= n:
            answer = mid
            left = mid + 1
        else:
            right = mid - 1

    return answer
