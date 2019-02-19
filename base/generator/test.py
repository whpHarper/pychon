'''
nested=[[1,2],[3,4],[5]]

def flatten(nested):
    for sublist in nested:
        for element in sublist:
            yield element
'''
info =[0,1,2,3,4,5,6,7,8,9]
a=[i+1 for i in range(10)]
print(a)

####列表生成
list=[x*x for x in range(10)]
print(list)

#生成器
generator_ex=(x*x for x in range(10))
print(next(generator_ex))
print(next(generator_ex))
for i in generator_ex:
    print(i)

def fib(max):
    n,a,b=0,0,1
    while n<max:
        yield b
        a,b,a1,b1=b,a+b,a,b
        print('a1=='+str(a1)+" b1=="+str(b1))
        n+=1

for i in fib(6):
    print(i)
