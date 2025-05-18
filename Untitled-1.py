# mandelbrot

def mandelbrot(c):
    z = list()
    z.append(0+0j)
    for n in range(1, 100+1):
        z.append(z[n-1]*z[n-1] + c)
    if c in z:
        return True

mandelbrot(1+1j)