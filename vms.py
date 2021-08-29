import os
import time

os.system("pkg install python")
os.system("pkg install figlet")
os.system("clear")

os.system("figlet VmStaT")

print("#########################################")
print(f'''
1• active/inactive memory
2• number of forks since boot
3• do not redisplay header
4• event counter statistics
5• disk statistics
6• summarize disk statistics
7• wide output
8• show times
9• show all
10• exit
    ''')
    
while True:
    data = int(input("Number Choice: "))
    
    if data == 1:
        os.system("vmstat -a")
    elif data == 2:
        os.system("vmstat -f")
    elif data == 3:
        os.system("vmstat -n")
    elif data == 4:
        os.system("vmstat -s")
    elif data == 5:
        os.system("vmstat -d")
    elif data == 6:
        os.system("vmstat -D")
    elif data == 7:
        os.system("vmstat -w")
    elif data == 8:
        os.system("vmstat -t")
    elif data == 9:
        os.system("vmstat -a")
        time.sleep(2)
        os.system("vmstat -f")
        time.sleep(2)
        os.system("vmstat -n")
        time.sleep(2)
        os.system("vmstat -s")
        time.sleep(2)
        os.system("vmstat -d")
        time.sleep(2)
        os.system("vmstat -D")
        time.sleep(2)
        os.system("vmstat -w")
        time.sleep(2)
        os.system("vmstat -t")
    elif data == 10:
        break
