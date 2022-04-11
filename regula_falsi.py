"""
a   = Xn
b   = Xn+1
x   = x*
e   = nilai error
N   = iterasi maksimum
"""
def f(x):
    f = (4*x**3)+7*x+3 
    return f

def metode_regulaFalsi(a, b , e, n):
    i = 0

    while(i <= n):
        x = (a*f(b)-b*f(a))/(f(b) - f(a))
        i = i+1

        if abs(f(x) < e):
            print(f"Iterasi ke {i-1}")
            print(f"Solusi : {x}")
            break
        else :
            if (f(a)*f(x) > 0):
                a = x
            else:
                b = x
    return

metode_regulaFalsi(-0.5, 0, 0.0001, 10000)