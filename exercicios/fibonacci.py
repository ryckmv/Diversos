def fibonacci(n):
    f=[1]
    
    for i in range(n):
        # poderia usar um if para caso meu fibonacci comece apenas com um ite
        p=f[-1]+ (f[-2] if len(f)> 1 else 0)
        f.append(p)

         
    print(f)

    
fibonacci(10)


def fibonacci(n):
    inicio=0
    proximo=1
    fibonaci=[1]
    for i in range(n):
        f= inicio+ proximo
        inicio= proximo
        proximo= f
        fibonaci.append(f)
    print(fibonaci)
       

    
    
fibonacci(10)
