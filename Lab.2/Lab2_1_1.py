import math

def output(n,t):
    x = 0
    for k in range(n):
        x+=(math.factorial(4*k)*(1103+26390*k))/(math.factorial(k)**4*396**(4*k))
    x=x*(2*2**0.5/9801)
    return  abs(round(1/x,t)-math.pi)


for j in range(10,20):
    i = 20
    print("小数点保留%r且迭代%r次的结果是%r" % (j, i, output(i, j)))
print("---")
for i in range(1,10):
    j = 15
    print("小数点保留%r且迭代%r次的结果是%r" % (j, i, output(i, j)))
