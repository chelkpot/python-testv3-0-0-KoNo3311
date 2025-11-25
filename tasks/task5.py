# tasks/task5.py

def solve():
# Ниже пишите решение задачи
    seconds = int(input()) % 86400 
    hours, seconds = divmod(seconds, 3600) 
    minutes, seconds = divmod(seconds, 60) 
 
    print(f"{hours:2}:{minutes:02}:{seconds:02}") 


   
# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()