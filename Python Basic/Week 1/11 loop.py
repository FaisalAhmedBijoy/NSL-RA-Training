
# while loop
i=0
while 1==1:
    print(i)
    i=i+1
    if i>=5:
        print("Breaking")
        break
print("Finished")

#for loop
#floot number iteration 
def frange(start,stop,step):
    i=start
    while i<stop:
        yield i
        i=i+step
for i in frange(0.5,1.0,0.1):
    print(i)