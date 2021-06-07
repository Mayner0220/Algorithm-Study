def fibo_A(num: int) -> int:
    if num == 0:
        return 0
    elif num == 1 or num == 2:
        return 1
    else:
        return fibo_A(num-1) + fibo_A(num-2)

def fibo_B(num: int) -> int:
    _curr, _next = 0, 1
    for _ in range(num):
        _curr, _next = _next, _curr + _next

    return _curr

nums = [1, 2, 3, 4, 5, 6]
for num in nums:
    print("Num: %s" % num)
    print("fibo_A: %s" % fibo_A(num))
    print("fibo_B: %s" % fibo_B(num))
    print()