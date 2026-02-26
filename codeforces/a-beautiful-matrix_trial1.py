import sys

def solve():
    matrix_data = sys.stdin.read().split()
    
    for index, value in enumerate(matrix_data):
        if value == '1':
            r = (index // 5) + 1
            c = (index % 5) + 1
            
            ans = abs(r - 3) + abs(c - 3)
            print(ans)
            break

if __name__ == "__main__":
    solve()