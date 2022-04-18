def f(x):
    f = (4*x**3)+7*x+3 
    return f

def metode_secant(a, b , e, N):
    i = 0

    while(i <= N):
        x2 = b - f(b)*(b-a)/(f(b)-f(a))
        i = i+1

        if abs(f(x2)) < e:
            print("Iterasi ke ",i)
            print("Solusi : %.3f"%x2)
            break
        else:
            a = b
            b = x2
    return

metode_secant(-0.5, 0, 0.0001, 10000)