import sys

def solve():
    n , t = list(map(int , input().split()))
    list1 = list(map(int , input().split()))

    left = 0
    current_time = 0
    max_books = 0
    
    for right in range(n):
        current_time += list1[right]
        
        while current_time > t:
            current_time -= list1[left]
            left += 1
            
        max_books = max(max_books, right - left + 1)
            
    print(max_books)

if __name__ == '__main__':
    solve()