import numpy as np
import matplotlib.pyplot as plt
from scipy import constants


def calcula_siguiente(delta_t, tita, v_tita, a_tita, F):
    Masa_M = 2      # Masa del carro
    Masa_m = 1      # Masa del pendulo
    Longitud_L = 1  # Longitud del pendulo

    # Calcula la aceleracion en el siguiente instante de tiempo dado el angulo y la velocidad angular actual, y la fuerza ejercida
    num = constants.g * np.sin(tita) + np.cos(tita) * ((-F - Masa_m * Longitud_L * np.power(v_tita, 2) * np.sin(tita)) / (Masa_M + Masa_m))
    den = Longitud_L * (4/3 - (Masa_m * np.power(np.cos(tita), 2) / (Masa_M + Masa_m)))
    a_tita = num/den
    v_tita = v_tita + a_tita * delta_t
    tita = tita + v_tita * delta_t + a_tita * np.power(delta_t, 2) / 2
    return tita, v_tita, a_tita


class Fuzzy_Logic:
    def __init__(self,dominio):
        self.dominio = dominio
        self.conjunto = []
        self.PF = []


    def fuzyfy(self): 
    # el dominio esta considerado con solapamiento de 50% 
        dx = (self.dominio[1]-self.dominio[0])/5 # defino 5 intervalos NG,NP,Z,PP,PG
        Z = [-dx,dx]
        PP = [0,2*dx]
        PG = [dx,self.dominio[1]]
        NP = [-2*dx,0]
        NG = [self.dominio[0],-dx]
        self.conjunto = [NG,NP,Z,PP,PG]
        return self.conjunto


    def valor_pertenencia(self,x):
    #analiza en orden NG,NP,Z,PP,PG para saber en cuales esta numero y les asigna su valor de pertenencia.
        i = 0
        pertenencia = [0,0,0,0,0]
        for intr in self.conjunto: 
            x0 = intr[0] #extremo menor
            x1 = intr[1] #extremo mayor
            centro = (x0+x1)/2 #centro
            
            if x < x0:
                pertenencia[i] = 0
            
            if x > x1:
                pertenencia[i] = 0
            
            if x0 <= x <= centro:
                if i==0:
                    pertenencia[0] = 1
                else:
                    pertenencia[i] = (x-x0)/(centro-x0)
            
            if centro < x <= x1:
                if i==4:
                    pertenencia[4] = 1
                else:
                    pertenencia[i] = (x-x1)/(centro-x1)
            
            i = i+1    
        return pertenencia


    def tabla(self, pert_tita, pert_v_tita): 
    #ingreso el valor de pertenencia de tita y tita' para obtener los valores de pertenencia de la Fuerza
        F=[0,0,0,0,0]
        #las 25 sentencias de tabla
        
    #columna de tita NG
        if pert_tita[0]!=0 and pert_v_tita[0]!=0: #NG
            minimo=min(pert_tita[0],pert_v_tita[0])
            F[4]=max(minimo,F[4])
        if pert_tita[0]!=0 and pert_v_tita[1]!=0: #NP
            minimo=min(pert_tita[0],pert_v_tita[1])
            F[4]=max(minimo,F[4])
        if pert_tita[0]!=0 and pert_v_tita[2]!=0: #Z
            minimo=min(pert_tita[0],pert_v_tita[2])
            F[4]=max(minimo,F[4])
        if pert_tita[0]!=0 and pert_v_tita[3]!=0: #PP
            minimo=min(pert_tita[0],pert_v_tita[3])
            F[4]=max(minimo,F[4])
        if pert_tita[0]!=0 and pert_v_tita[4]!=0: #PG
            minimo=min(pert_tita[0],pert_v_tita[4])
            F[3]=max(minimo,F[3])
        
    #columna de tita NP
        if pert_tita[1]!=0 and pert_v_tita[0]!=0: #NG
            minimo=min(pert_tita[1],pert_v_tita[0])
            F[4]=max(minimo,F[4])
        if pert_tita[1]!=0 and pert_v_tita[1]!=0: #NP
            minimo=min(pert_tita[1],pert_v_tita[1])
            F[4]=max(minimo,F[4])
        if pert_tita[1]!=0 and pert_v_tita[2]!=0: #Z
            minimo=min(pert_tita[1],pert_v_tita[2])
            F[3]=max(minimo,F[3])
        if pert_tita[1]!=0 and pert_v_tita[3]!=0: #PP
            minimo=min(pert_tita[1],pert_v_tita[3])
            F[2]=max(minimo,F[2])
        if pert_tita[1]!=0 and pert_v_tita[4]!=0: #PG
            minimo=min(pert_tita[1],pert_v_tita[4])
            F[1]=max(minimo,F[1])

    #columna de tita Z
        if pert_tita[2]!=0 and pert_v_tita[0]!=0: #NG
            minimo=min(pert_tita[2],pert_v_tita[0])
            F[4]=max(minimo,F[4])
        if pert_tita[2]!=0 and pert_v_tita[1]!=0: #NP
            minimo=min(pert_tita[2],pert_v_tita[1])
            F[3]=max(minimo,F[3])
        if pert_tita[2]!=0 and pert_v_tita[2]!=0: #Z
            minimo=min(pert_tita[2],pert_v_tita[2])
            F[2]=max(minimo,F[2])
        if pert_tita[2]!=0 and pert_v_tita[3]!=0: #PP
            minimo=min(pert_tita[2],pert_v_tita[3])
            F[1]=max(minimo,F[1])
        if pert_tita[2]!=0 and pert_v_tita[4]!=0: #PG
            minimo=min(pert_tita[2],pert_v_tita[4])
            F[0]=max(minimo,F[0])

    #columna de tita PP
        if pert_tita[3]!=0 and pert_v_tita[0]!=0: #NG
            minimo=min(pert_tita[3],pert_v_tita[0])
            F[3]=max(minimo,F[3])
        if pert_tita[3]!=0 and pert_v_tita[1]!=0: #NP
            minimo=min(pert_tita[3],pert_v_tita[1])
            F[2]=max(minimo,F[2])
        if pert_tita[3]!=0 and pert_v_tita[2]!=0: #Z
            minimo=min(pert_tita[3],pert_v_tita[2])
            F[1]=max(minimo,F[1])
        if pert_tita[3]!=0 and pert_v_tita[3]!=0: #PP
            minimo=min(pert_tita[3],pert_v_tita[3])
            F[0]=max(minimo,F[0])
        if pert_tita[3]!=0 and pert_v_tita[4]!=0: #PG
            minimo=min(pert_tita[3],pert_v_tita[4])
            F[0]=max(minimo,F[0])

    #columna de tita PG
        if pert_tita[4]!=0 and pert_v_tita[0]!=0: #NG
            minimo=min(pert_tita[4],pert_v_tita[0])
            F[1]=max(minimo,F[1])
        if pert_tita[4]!=0 and pert_v_tita[1]!=0: #NP
            minimo=min(pert_tita[4],pert_v_tita[1])
            F[0]=max(minimo,F[0])
        if pert_tita[4]!=0 and pert_v_tita[2]!=0: #Z
            minimo=min(pert_tita[4],pert_v_tita[2])
            F[0]=max(minimo,F[0])
        if pert_tita[4]!=0 and pert_v_tita[3]!=0: #PP
            minimo=min(pert_tita[4],pert_v_tita[3])
            F[0]=max(minimo,F[0])
        if pert_tita[4]!=0 and pert_v_tita[4]!=0: #PG
            minimo=min(pert_tita[4],pert_v_tita[4])
            F[0]=max(minimo,F[0])
        
        pert_F = F
        aux1 = [0,0,0,0,0]

    #calculo por media de centros
        for i in range(5):
            if pert_F[i]!=0:
                conjunto = self.conjunto[i]
                centro = (conjunto[0]+conjunto[1])/2     # calculo del centro del intervalo
                aux1[i] = centro*pert_F[i]               # multiplicamos por la funcion de pertenencia y sumamos
        
        if sum(aux1)!=0 and sum(pert_F)!=0:
            mediadc = sum(aux1)/sum(pert_F)
        else:
            mediadc = 0

        return mediadc


def grafica_ind(V_tiempo, V_tita, V_vel, V_acel, V_fuerza):
    plt.figure(figsize=(5,5))
    plt.figure(1)
    plt.plot(V_tiempo,V_tita)
    plt.grid()
    plt.title("Valor de posicion")
    plt.xlabel("tiempo (s)")
    plt.ylabel("Tita(º)")
    
    plt.figure(figsize=(5,5))
    plt.figure(2)
    plt.plot(V_tiempo,V_vel)
    plt.grid()
    plt.title("Valor de velocidad")
    plt.xlabel("tiempo (s)")
    plt.ylabel("Velocidad (rad/s)")
    
    plt.figure(figsize=(5,5))
    plt.figure(3)
    plt.plot(V_tiempo,V_acel)
    plt.grid()
    plt.title("Valor de aceleracion")
    plt.xlabel("tiempo (s)")
    plt.ylabel("Aceleracion (rad/s^2)")

    plt.figure(figsize=(5,5))
    plt.figure(4)
    plt.plot(V_tiempo,V_fuerza)
    plt.grid()
    plt.title("Valor de fuerza")
    plt.xlabel("tiempo (s)")
    plt.ylabel("Fuerza (N)")
    plt.tight_layout()
    plt.show()


def simular(V_tiempo, tita_0, v_tita_0, a_tita_0, f):
    tita = (tita_0 * np.pi) / 180  # paso a radianes
    v_tita = v_tita_0    # en rad/s
    a_tita = a_tita_0    # en rad/s^2
    
    dom = (90 * np.pi) / 180
    dominio_tita = (-dom,dom)
    dominio_v_tita = (-6,6)
    dominio_fuerza = (-300,300)
    D1 = Fuzzy_Logic(dominio_tita)
    D2 = Fuzzy_Logic(dominio_v_tita)
    D3 = Fuzzy_Logic(dominio_fuerza)
    CD1 = D1.fuzyfy()
    CD2 = D2.fuzyfy()
    CD3 = D3.fuzyfy()
 
    # Simular
    V_tita = []
    V_vel = []
    V_acel = []
    V_fuerza = []
    for t in V_tiempo:
        tita, v_tita, a_tita = calcula_siguiente(delta_t, tita, v_tita, a_tita, -f)
        V_tita.append(tita*180/np.pi)
        V_vel.append(v_tita)
        V_acel.append(a_tita)
        aux1 = D1.valor_pertenencia(tita)
        aux2 = D2.valor_pertenencia(v_tita)
        f = D3.tabla(aux1,aux2)
        V_fuerza.append(f)

    grafica_ind(V_tiempo, V_tita, V_vel, V_acel, V_fuerza)
    
def prueba_en_vacio():
    delta_t = 0.0001
    tita = 45
    v_tita = 0
    a_tita = 0
    f = 0
    V_tiempo = np.arange(0, 10, delta_t)
    V_tita = []
    V_vel = []
    V_acel = []
    V_fuerza = []

    for t in V_tiempo:
        tita, v_tita, a_tita = calcula_siguiente(delta_t, tita, v_tita, a_tita, -f)
        V_tita.append(tita*180/np.pi)
        V_vel.append(v_tita)
        V_acel.append(a_tita)
    """
    plt.figure(figsize=(10,10))
    plt.figure(1)
    plt.plot(V_tiempo,V_tita)
    plt.grid()
    plt.title("Valor de posicion en vacio")
    plt.xlabel("tiempo (s)")
    plt.ylabel("Tita(º)")
    """
    plt.figure(figsize=(10,10))
    plt.figure(2)
    plt.plot(V_tiempo,V_vel)
    plt.grid()
    plt.title("Valor de velocidad en vacio (dt = 0.0001)")
    plt.xlabel("tiempo (s)")
    plt.ylabel("Velocidad (rad/s)")
    
    """
    plt.figure(figsize=(10,10))
    plt.figure(3)
    plt.plot(V_tiempo,V_acel)
    plt.grid()
    plt.title("Valor de aceleracion en vacio")
    plt.xlabel("tiempo (s)")
    plt.ylabel("Aceleracion (rad/s^2)")
    """
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
# Simula el modelo del carro-pendulo.
# Parametros:
#   tiempo_max: tiempo maximo (inicia en 0)
#   delta_t: incremento de tiempo en cada iteracion
#   tita_0: Angulo inicial (grados)
#   v_tita_0: Velocidad angular inicial (radianes/s)
#   a_tita_0: Aceleracion angular inicial (radianes/s2)
#   f: Fuerza aplicada al carro (Newton)
    
    tiempo_max = 10
    delta_t = 1e-3
    prueba_en_vacio()
    #p_prueba = 90   # POSICION INICIAL
    #v_prueba = 4   # VELOCIDAD INICIAL
    p_prueba = int(input("Posicion angular inicial (en grados):"))
    v_prueba = int(input("Velocidad angular inicial (en rad/s):"))
    
    V_tiempo = np.arange(0, tiempo_max, delta_t)

# simular(tiempo_max, delta_t, tita_0, v_tita_0, a_tita_0, f)
    
    simular(V_tiempo, p_prueba, v_prueba, 0, 0)
