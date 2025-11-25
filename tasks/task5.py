# tasks/task5.py

def solve():
# Ниже пишите решение задачи
    n=int(input())
    n=n%(3600*24)
    h=n//3600
    m=n%3600//60
    s=n%60
    print(h,':',str(m//10)+str(m%10),':',str(s//10)+str(s%10))

   
# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()