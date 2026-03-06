def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    
    has_even = False
    has_odd = False
    
    for num in arr:
        if num % 2 == 0:
            has_even = True
        else:
            has_odd = True
    
    if has_even and has_odd:
        arr.sort()
    
    print(*arr)
solve()