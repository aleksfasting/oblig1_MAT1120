import matplotlib.pyplot as plt
import numpy as np # importerer modulene

def sirkel(x,y,r): # definerer funksjonen som tegner sirkler
    t = np.linspace(0, 2 * np.pi, 100)
    plt.plot(x + r * np.cos(t), y + r * np.sin(t), linewidth = 2)

def finn_d(A): # definerer en funksjon som finner alle d_j
    d_list = [] # lager en tom liste som vi skal legge d-verdiene i
    for j in range(np.shape(A)[0]): # for-lokke for aa gaa gjennom alle radene
        d_list.append(A[j,j]) # legger til verdiene langs diagonalen

    return d_list

def finn_r(A): # definerer funksjonen som finner alle r_j
    r_list = [] # lager en tom liste som vi skal legge r_veridene i
    for j in range(np.shape(A)[0]): # for-lokke for aa gaa gjennom alle radene
        r_j = 0 # startverdi for r_j lik 0
        for i in range(np.shape(A)[1]): # for-lokke for aa gaa gjennom alle elementene i raden
            if j != i: # sjekker om elementet er paa diagonalen
                r_j = r_j + abs(A[j,i]) # legger elementet til i r_j (med absoluttverdi)hvis det ikke er i diagonalen
        r_list.append(r_j) # legger til en utregnet r_j i listen

    return r_list

def egensirkler(A):
    d_list = finn_d(A) # bruker funksjonen for aa finne d-verdier paa matrisen
    r_list = finn_r(A) # bruker funksjonen for aa finne r-verdier paa matrisen

    for i in range(np.shape(A)[1]): # for-lokke for aa gaa fjennom alle radene
        sirkel(d_list[i], 0, r_list[i]) # tegner egensirklene

    egenverdier = np.linalg.eig(A)[0]
    for i in range(len(egenverdier)):
        re = np.real(egenverdier[i])
        im = np.imag(egenverdier[i])
        plt.plot(re,im,'.',markersize = 30)


    plt.show() # viser plottet



B = np.matrix([
    [-2,0,1/2,0],
    [-1/4,1,1/4,0],
    [0,0,3,-1],
    [1/8,1/8,1/4,2]])

egensirkler(B)
