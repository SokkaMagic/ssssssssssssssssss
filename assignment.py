# Exercise 1
def find_closest(data, target):
    if target <= data[0]:
        return data[0]
    if target >= data[-1]:
        return data[-1]
    
    left = 0
    right = len(data) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if data[mid] == target:
            return target
        elif data[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    val1 = data[right]
    val2 = data[left]
    
    diff1 = abs(val1 - target)
    diff2 = abs(val2 - target)
    
    if diff1 < diff2:
        return val1
    elif diff2 < diff1:
        return val2
    else:
        return min(val1, val2)


# Exercise 2
def integer_sqrt(n):
    if n == 0:
        return 0
        
    left = 0
    right = n
    ans = 0
    
    while left <= right:
        mid = (left + right) // 2
        if mid * mid <= n:
            ans = mid
            left = mid + 1
        else:
            right = mid - 1
            
    return ans
