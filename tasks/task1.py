# tasks/task1.py

def solve():
# Ниже пишите решение задачи
    a=int(input())
    b=a // 100
    c=(a//10)%10
    d=a%10
    print(b+c+d)   

    
# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()