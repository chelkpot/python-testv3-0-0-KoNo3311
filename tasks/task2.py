# tasks/task2.py

def solve():
# Ниже пишите решение задачи
    a=int(input())
    a=a%1440
    hours=a//60
    min=a%60
    print(hours,min)
   

   
# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()