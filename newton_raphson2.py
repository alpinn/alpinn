def metode_newtonRaphson(f,df, x0):
    e = 0.0001
    i = 0
    n = 10000

    while(i<=n):
        x0 = x0 - f(x0)/df(x0)
        i=i+1

        if abs(f(x0)) < e:
            print("Iterasi ke ",i)
            print("Solusi : %.3f"%x0)
            break
        else:
            if df(x0) == 0:
                print("Zero derivative")
                return None
    return x0

f = lambda x:(4*x**3)+7*x+3 
df = lambda x: 12*x**2+7
x0 = -0.05
x_root = metode_newtonRaphson(f,df,x0)
        