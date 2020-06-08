#Top-down descendente
memoria = {1:1,2:1,3:2}

def fibonacci2(num):
    a = 1
    b= 1
    
    for i in range(1,num-1):
        a,b = b, a+b
    return b

def fibonacci_top_down(num):
    if num in memoria:
        return memoria[num]
    
    f = fibonacci2(num-1)+fibonacci2(num-2)
    memoria[num] = f
    return memoria[num]

print(fibonacci_top_down(4))
print(memoria)