from sympy import *
import math
def output(t,m):
    k,n=symbols('k n')
    a0=sqrt(8)/9801
    a1=factorial(4*k)*(1103+26390*k)
    a2=(factorial(k)**4)*(396**(4*k))
    a3=a0*a1/a2
    a4=summation(a3,(k,0,n))
    result=lambdify(n,a4,'sympy')
    return (abs(result(t).evalf(m)-1/math.pi))

for j in range(5,25 ):
    i = 10
    print("小数点保留%r且迭代%r次的结果是%r" % (j, i, output(i, j)))

print("---")
for i in range(15, 20):
    j = 3
    print("小数点保留%r且迭代%r次的结果是%r" % (j, i, output(i, j)))
