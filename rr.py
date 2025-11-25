seconds = int(input()) % 86400 
hours, seconds = divmod(seconds, 3600) 
minutes, seconds = divmod(seconds, 60) 
 
print(f"{hours:02}:{minutes:02}:{seconds:02}") 
