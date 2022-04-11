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

    #jumlah iterasi sampai solusi ketemu
    while(i <= n):
        #algorithm : https://iq.opengenus.org/regula-falsi-method/#:~:text=Regula%20Falsi%20method%20or%20the,at%20a%20fairly%20slow%20speed.
        x = (a*f(b)-b*f(a))/(f(b) - f(a))
        i = i-1

        #jika f(x) < e maka program berhenti
        if abs(f(x) < e):
            print("Iterasi ke ",i)
            print("Solusi : %.3f"%x)
            break
        #jika tidak, x dan a sama tanda maka x ke a sedangkan tidak, x ke b 
        else :
            if (f(a)*f(x) > 0):
                a = x
            else:
                b = x
    return

metode_regulaFalsi(-0.5, 0, 0.0001, 10000)