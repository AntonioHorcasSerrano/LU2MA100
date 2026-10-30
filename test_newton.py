def newton(F, DF, x0, eps=1e-12, N=10000):
    x = x0.copy()
    for i in range(N):
        # calcule F(x) et DF(x)
        Fx = F(x)
        DFx = DF(x)
        # teste si la précision est suffisante
        if np.linalg.norm(Fx) < eps:
            return x
        # teste si la dérivée n'est pas trop petite
        if np.linalg.norm(DFx) < eps:
            raise Exception(f"La dérivée |DF| = {np.linalg.norm(DFx)} est trop petite")
        # résout l'équation d = DFx^{-1} Fx puis itération de Newton
        x -= np.linalg.solve(DFx, Fx)
    # si la boucle termine alors on n'a pas convergé
    raise Exception(f"L'erreur après {N} itérations est {abs(Fx)} > {eps}")

def euler_implicit(f, Dxf, x0, t):
    # initialise le vecteur de la solution
    x = np.zeros((len(t),len(x0)))
    # donnée initiale
    x[0] = x0
    # boucle en temps
    for i in range(1,len(t)):
        # fonction dont il faut trouver le zéro
        F = lambda xi: xi - x[i-1] - (t[i]-t[i-1])*f(t[i],xi)
        # dérivée de la fonction dont il faut trouver le zéro
        DF = lambda xi: np.identity(len(x0)) - (t[i]-t[i-1])*Dxf(t[i],xi)
        # solution par la méthode de Newton
        x[i] = newton(F, DF, x[i-1])
    return x

def euler_explicit(f, x0, t):
    x = np.zeros((len(t), len(x0)))
    x[0] = x0
    for i in range(len(t) - 1):
        x[i + 1] = x[i] + (t[i+1] - t[i])*f(t[i],x[i])
    return x


import matplotlib.pyplot as plt
import numpy as np

# définit les données du problème
f = lambda t,x : np.array([np.sin(t)-np.cos(x[1]), -np.cos(x[0])])
Dxf = lambda t,x : np.array([[0, np.sin(x[1])],[np.sin(x[0]),0]])
x0 = np.array([1,0])
# taille de la figure
plt.figure(figsize=(8,5))
plt.title(r"Solution de $\dot{x}+\cos(y)=\sin(t)$ et $\dot{y}+\cos(x)=0$")
# résolution
t = np.linspace(0,10,20)
sol = euler_explicit(f, x0, t)
print(sol)
plt.plot(t, sol[:,0], label=r"Euler explicite : $x(t)$")
plt.plot(t, sol[:,1], label=r"Euler explicite : $y(t)$")
# sol = euler_implicit(f, Dxf, x0, t)
# plt.plot(t, sol[:,0], label=r"Euler implicite : $x(t)$")
# plt.plot(t, sol[:,1], label=r"Euler implicite : $y(t)$")
plt.legend()
plt.show()