import time
from datetime import timedelta

#print repr(time) #watch out for this

print(("\n{}MUF - Mobile Unicode Fuzzer\n{}By Zadew!\n{}\n").format((" "*10),(" "*19),("="*47)))

time.sleep(2)
#fireup_time = time.monotonic()

laggy = []
buggy = []

for i in range(1, 100000):
    start_time = time.time()
    try:
       # print(i, "", unichr(i)) #2.7
       print(i, "", chr(i))    #3.6
    except:
        buggy.append(i)
        continue
    end_time = time.time()
    lag = (end_time - start_time)
    print(lag)
    if (lag >= 0.15): #determine
        laggy.append(i)

#shutdown_time = time.monotonic()

dump = ("laggy:\n{}\n\n\nbuggy:\n{}").format(laggy[:],buggy[:])
file = open("dumpfile.txt","w")
file.write(dump)

#print("\n[*] {} Dangerous Chars found in -- {} --").format(str((len(laggy)+len(buggy))), (timedelta(shutdown_time - fireup_time)))  

