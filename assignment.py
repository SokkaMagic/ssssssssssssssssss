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
    if left == 0:
        return data[0]

    if left == len(data):
        return data[-1]

    smaller = data[left - 1]
    larger = data[left]

    if target - smaller <= larger - target:
        return smaller
    else:
        return larger

# Exercise 2

def integer_sqrt(n):
    left = 0
    right = n
    result = 0

    while left <= right:
        mid = (left + right) // 2

        if mid * mid <= n:
            result = mid       # Valid answer, try bigger
            left = mid + 1
        else:
            right = mid - 1    # Too big, try smaller

    return result


print(integer_sqrt(16))  # 4
print(integer_sqrt(24))  # 4
print(integer_sqrt(0))   # 0
