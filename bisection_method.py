"""
a   = Xn
b   = Xn+1
mid = Xmid
e   = nilai error
N   = iterasi maksimum
"""
def metode_biseksi(f, a, b, e=10**-4, N = 10000):
    if f(a)*f(b) >= 0:
        print("Nilai tidak teridentifikasi")
        quit()

    #memulai pengulangan iterasi
    for n in range (1,N):
        #nilai mid
        mid = (a+b)/2
        print('Iterasi',n,": %.4f"%abs(f(mid)))

        #Mengecek jika |f(Xmid|<=e
        if abs(f(mid)) < e:
            return (mid)
        else:
            if f(mid)*f(a) < 0:
                b = mid
            elif f(mid)*f(b) < 0:
                a = mid 

f = lambda x:(4*x**3)+7*x+3
a = -0.5
b = 0

hasil = metode_biseksi(f, a, b)
print('Solusi : %.3f'%hasil)