def f(x):
    f = (4*x**3)+7*x+3 
    return f

def metode_biseksi(a, b , e, N):
    i = 0

    while(i <= N):
        mid = (a+b)/2
        i = i-1

        if abs(f(mid)) < e:
            print("Iterasi ke ",i)
            print("Solusi : %.3f"%mid)
            break
        else:
            if f(mid)*f(a) < 0:
                b = mid
            elif f(mid)*f(b) < 0:
                a = mid
    return

metode_biseksi(-0.5, 0, 0.0001, 10000)