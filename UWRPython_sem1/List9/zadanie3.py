from matplotlib import pyplot as plt
import math as M

def rzut_ukosny():
    #V = float(input('Podaj prędkość rzutu:\n'))
    #alpha = float(input('Podaj kąt rzutu(deg):\n'))
    V = 10 # m/s
    alpha = 45 #deg
    g = 9.81
    Vx = M.cos(alpha*M.pi/180)
    Vy = M.sin(alpha*M.pi/180)
    #H_max = Vy*Vy/2/g
    H_max = (V*V*M.sin(alpha/180*M.pi)*M.sin(alpha/180*M.pi))/(2*g)
    Range_max = V*V/g*M.sin(2*alpha/180*M.pi)
    Time_max = 2*Vy/g
    print('MAX WYSOKOŚĆ = ',H_max)
    print('MAX ZASIĘG = ',Range_max)
    print('CZAS LOTU = ',Time_max)
    X = []
    Y = []
    T = []
    Vy_temp = []
    Vx_temp = []
    t = 0
    while(t <= Time_max):
        y = float(((Vy*t)-(g*(t*t)/2)))
        x = float(Vx*t*M.cos(alpha*M.pi/180))
        X.append(x)
        Y.append(y)
        T.append(t)
        Vy_temp.append(Vy - g * t)
        Vx_temp.append(Vx)
        t += 0.01
    plt.subplot(3, 1, 1) # Pierwszy wykres
    plt.plot(T,Vx_temp)
    plt.plot(T,Vy_temp)
    plt.title('Prędkość chwilowa w ruchu')
    plt.xlabel("t[s]")
    plt.ylabel("v[m/s]")
    plt.subplot(3,1,3) # Drugi wykres
    plt.plot(X,Y)
    plt.title('Tor w funkcji')
    plt.xlabel("x[m]")
    plt.ylabel("y[m]")
    plt.subplot(3,1,2) # Trzeci wykres
    plt.plot(T,X)
    plt.title('Tor w funkcji')
    plt.xlabel("t[s]")
    plt.ylabel("x[m]")
    plt.show()
    
rzut_ukosny();
