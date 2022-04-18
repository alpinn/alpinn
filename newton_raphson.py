def newtons(f,df,x0, N=10000):
  e = 10**-4
  N = 100
  i=0
  while(i<=N):
    if abs(f(x0)) < e:
      return x0
    if df(x0) == 0:
      print("Zero derivative")
      return None
    x0 = x0 - f(x0)/df(x0)
    i=i+1
    print("Iterasi ke ",i)
    print("Solusi : %.3f"%x0)
  return x0

f = lambda x: x**3+x**2-3
df = lambda x: 3*x**2+2*x
x0 = 3.5
x_root = newtons(f,df,x0)
print('Result : ', x_root)