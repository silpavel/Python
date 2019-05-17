#Lucky tiket
x1=x2=x3=x4=x5=x6=0
dsum=0
ddSum=[0]*28
for number in range(0,999999):
    x1=number // 100000
    x2=number // 10000 % 10
    x3=number // 1000 % 10
    x4=number // 100 % 10
    x5=number // 10 % 10
    x6=number % 10
    dsum=x1+x2+x3-(x4+x5+x6)
    if dsum<0: dsum*=-1
    ddSum[dsum]+=1
for i in range(0,28):
    print(i,' : ',ddSum[i]/10000,' %')









