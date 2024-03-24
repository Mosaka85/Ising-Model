# SAGE MATH Python Code

import random 
import numpy as np 
N=10  
A=np.zeros((N,N)) 
for i in range(N):
    
    for j in range(N):
        A[i][j]=random.choice([-1,1])
import matplotlib.pyplot as plt  
plt.imshow(A,cmap ='Greens') 
plt.show()


Ei=0
Ef=0
Etot_i=0
J=1
for x in range(N):
    for y in range(N):
        if x==0 and y==0 : 
            Etot_i += -J*A[x][y]*A[x,y+1] + (-J*A[x][y]*A[x+1,y]) + (-J*A[x][y]*A[N-1,N-1]) + (-J*A[x][y]*A[x,N-1])
        elif x==0 and y==N-1 :  
            Etot_i += -J*A[x][y]*A[x,y-1] +  (-J*A[x][y]*A[x+1,y]) + (-J*A[x][y]*A[N-1,x]) +  (-J*A[x][y]*A[x,x])
           
        elif y==0 and  x == N-1: 
            Etot_i += -J*A[x][y]*A[x,y+1] + (-J*A[x][y]*A[x-1,y])  + (-J*A[x][y]*A[y,N-1]) + -J*A[x][y]*A[N-1,N-1]
            
        elif y==N-1 and x==N-1: 
            Etot_i += -J*A[x][y]*A[x,y-1] +  (-J*A[x][y]*A[x-1,y]) + (-J*A[x][y]*A[N-1,0]) + -J*A[x][y]*A[0,0]
        elif x==0 and y != N-1 and y != 0: 
            Etot_i += -J*A[x][y]*A[x,y-1]  + (-J*A[x][y]*A[x,y+1])+  (-J*A[x][y]*A[x+1,y]) + (-J*A[x][y]*A[x-1,y])
        elif y==0 and x !=0   :  
            Etot_i += -J*A[x][y]*A[x,y+1]  + (-J*A[x][y]*A[x-1,y])+  (-J*A[x][y]*A[x+1,y]) + (-J*A[x][y]*A[x,y-1])
        elif x==N-1  and y != 0 :
            Etot_i += -J*A[x][y]*A[x,y+1]  + (-J*A[x][y]*A[x-1,y])+  (-J*A[x][y]*A[x,y-1]) +  (-J*A[x][y]*A[0,y])
           
        elif  y== N-1 and x != 0: 
            Etot_i += -J*A[x][y]*A[x+1,y]  + (-J*A[x][y]*A[x-1,y])+  (-J*A[x][y]*A[x,y-1]) + (-J*A[x][y]*A[x,0])
        else: 
            Etot_i += -J*A[x][y]*A[x,y-1] + (-J*A[x][y]*A[x-1,y]) + (-J*A[x][y]*A[x,y+1])+  (-J*A[x][y]*A[x+1,y])
Etot_i

def Metropolis_lattice(lattice,n,temp_B, J):
    for w in range(n):  
        Ei=0 
        Ef=0 
        E=Etot_i 
        x = ZZ.random_element(0,N) 
        y= ZZ.random_element(0,N)  
        SpinI = lattice[x,y] 
        # Flip the spin 
        SpinF = (-1)*SpinI
        #definie the conditions 
        # After choosing a random spin the we flip the spin
        # After fliping the spin sum the energy of the neighbouring spins 
        # We sum energy of the  4 neighouring spins  but if the spin is the the edgewe take spin the the other edge 
        if x==0 and y==0 : #The spin is at the corner we take spins on the opposide corners as the neighbors

            Ei += -J*SpinI*lattice[x,y+1] + (-J*SpinI*lattice[x+1,y]) + (-J*SpinI*lattice[N-1,N-1]) + (-J*SpinI*lattice[x,N-1])  
            Ef += -J*SpinF*lattice[x,y+1] + (-J*SpinF*lattice[x+1,y]) + (-J*SpinI*lattice[N-1,N-1]) + (-J*SpinI*lattice[x,N-1]) 
        elif x==0 and y==N-1 : #The spin is at the corner we take spins on the opposide corners as the neighbors

            Ei += -J*SpinI*lattice[x,y-1] +  (-J*SpinI*lattice[x+1,y]) + (-J*SpinI*lattice[N-1,x]) +  (-J*SpinI*lattice[x,x])
            Ef += -J*SpinF*lattice[x,y-1] +  (-J*SpinF*lattice[x+1,y]) +  (-J*SpinI*lattice[N-1,x]) +  (-J*SpinI*lattice[x,x])
        elif y==0 and  x == N-1: 
   
            Ei += -J*SpinI*lattice[x,y+1] + (-J*SpinI*lattice[x-1,y])  + (-J*SpinI*lattice[y,N-1]) + -J*SpinI*lattice[N-1,N-1]
            Ef += -J*SpinF*lattice[x,y+1] + (-J*SpinF*lattice[x-1,y]) + (-J*SpinI*lattice[y,N-1]) + -J*SpinI*lattice[N-1,N-1]
        elif y==N-1 and x==N-1:
            Ei += -J*SpinI*lattice[x,y-1] +  (-J*SpinI*lattice[x-1,y]) + (-J*SpinI*lattice[N-1,0]) + -J*SpinI*lattice[0,0]
            Ef += -J*SpinF*lattice[x,y-1] +  (-J*SpinF*lattice[x-1,y]) +  (-J*SpinI*lattice[N-1,0]) + -J*SpinI*lattice[0,0]
        elif x==0 and y != N-1 and y != 0: # the spin is on the edge it only has 3 neighbours  we take one on the oppside edge as neigbor
  
            Ei += -J*SpinI*lattice[x,y-1]  + (-J*SpinI*lattice[x,y+1])+  (-J*SpinI*lattice[x+1,y]) + (-J*SpinI*lattice[x-1,y])
            Ef += -J*SpinF*lattice[x,y-1]  + (-J*SpinF*lattice[x,y+1])+  (-J*SpinF*lattice[x+1,y])  +(-J*SpinI*lattice[x-1,y])
        elif y==0 and x !=0   : 

            Ei += -J*SpinI*lattice[x,y+1]  + (-J*SpinI*lattice[x-1,y])+  (-J*SpinI*lattice[x+1,y]) + (-J*SpinI*lattice[x,y-1])
            Ef += -J*SpinF*lattice[x,y+1]  + (-J*SpinF*lattice[x-1,y])+  (-J*SpinF*lattice[x+1,y]) + (-J*SpinI*lattice[x,y-1])
        elif x==N-1  and y != 0 : 
            Ei += -J*SpinI*lattice[x,y+1]  + (-J*SpinI*lattice[x-1,y])+  (-J*SpinI*lattice[x,y-1]) +  (-J*SpinI*lattice[0,y])
            Ef += -J*SpinF*lattice[x,y+1]  + (-J*SpinF*lattice[x-1,y])+  (-J*SpinF*lattice[x,y-1]) +  (-J*SpinI*lattice[0,y])
        elif  y== N-1 and x != 0: 

            Ei += -J*SpinI*lattice[x+1,y]  + (-J*SpinI*lattice[x-1,y])+  (-J*SpinI*lattice[x,y-1]) + (-J*SpinI*lattice[x,0])
            Ef += -J*SpinF*lattice[x+1,y]  + (-J*SpinF*lattice[x-1,y])+  (-J*SpinF*lattice[x,y-1]) + (-J*SpinI*lattice[x,0]) 
        else:
            Ei += -J*SpinI*lattice[x,y-1] + (-J*SpinI*lattice[x-1,y]) + (-J*SpinI*lattice[x,y+1])+  (-J*SpinI*lattice[x+1,y])
            Ef += -J*SpinF*lattice[x,y-1] + (-J*SpinF*lattice[x-1,y]) + (-J*SpinF*lattice[x,y+1])+  (-J*SpinF*lattice[x+1,y])
        
        Delta_E= Ef - Ei  
        if Delta_E <=0:  
            E += Delta_E  
            lattice[x,y]=SpinF  
        else:
            z = random.random()  # choose a random number between 0and 1 (0 < z < 1) 
            if z < e^(-temp_B*Delta_E): 
                E += Delta_E 
                lattice[x,y]=SpinF 
    plt.title('Lattice after   ' + str(   n) +'    flips' + '   for temperature betha ='+ str( temp_B)) #imshow title
    plt.imshow(lattice,cmap ='Greens')   # White means spin down and green is spin up
    plt.show()  
        



for i in range(0,1): 
    Metropolis_lattice(A,10000,i,1.2)

beta=[i for i in srange(0,1.5,0.1)]  


def Metropolis_lattice_plotting(lattice,n,temp_B, J):
    for g in range(len(beta)):
        Es=0
        E_list=[]
        for k in beta:  
            temp_B = k
            for w in range(n): 
                tot_spins= w
                Ei=0 
                Ef=0 
                E=Etot_i 
                x = ZZ.random_element(0,N) 
                y= ZZ.random_element(0,N)  
                SpinI = lattice[x,y] 
                SpinF = (-1)*SpinI
               
                if x==0 and y==0 : 
                    Ei += -J*SpinI*lattice[x,y+1] + (-J*SpinI*lattice[x+1,y]) + (-J*SpinI*lattice[N-1,N-1]) + (-J*SpinI*lattice[x,N-1])  
                    Ef += -J*SpinF*lattice[x,y+1] + (-J*SpinF*lattice[x+1,y]) + (-J*SpinI*lattice[N-1,N-1]) + (-J*SpinI*lattice[x,N-1]) 
                elif x==0 and y==N-1 : 
                    Ei += -J*SpinI*lattice[x,y-1] +  (-J*SpinI*lattice[x+1,y]) + (-J*SpinI*lattice[N-1,x]) +  (-J*SpinI*lattice[x,x])
                    Ef += -J*SpinF*lattice[x,y-1] +  (-J*SpinF*lattice[x+1,y]) +  (-J*SpinI*lattice[N-1,x]) +  (-J*SpinI*lattice[x,x])
                elif y==0 and  x == N-1: 
                    Ei += -J*SpinI*lattice[x,y+1] + (-J*SpinI*lattice[x-1,y])  + (-J*SpinI*lattice[y,N-1]) + -J*SpinI*lattice[N-1,N-1]
                    Ef += -J*SpinF*lattice[x,y+1] + (-J*SpinF*lattice[x-1,y]) + (-J*SpinI*lattice[y,N-1]) + -J*SpinI*lattice[N-1,N-1]
                elif y==N-1 and x==N-1:
                    Ei += -J*SpinI*lattice[x,y-1] +  (-J*SpinI*lattice[x-1,y]) + (-J*SpinI*lattice[N-1,0]) + -J*SpinI*lattice[0,0]
                    Ef += -J*SpinF*lattice[x,y-1] +  (-J*SpinF*lattice[x-1,y]) +  (-J*SpinI*lattice[N-1,0]) + -J*SpinI*lattice[0,0]
                elif x==0 and y != N-1 and y != 0: 
                    Ei += -J*SpinI*lattice[x,y-1]  + (-J*SpinI*lattice[x,y+1])+  (-J*SpinI*lattice[x+1,y]) + (-J*SpinI*lattice[x-1,y])
                    Ef += -J*SpinF*lattice[x,y-1]  + (-J*SpinF*lattice[x,y+1])+  (-J*SpinF*lattice[x+1,y])  +(-J*SpinI*lattice[x-1,y])
                elif y==0 and x !=0   :  
                    Ei += -J*SpinI*lattice[x,y+1]  + (-J*SpinI*lattice[x-1,y])+  (-J*SpinI*lattice[x+1,y]) + (-J*SpinI*lattice[x,y-1])
                    Ef += -J*SpinF*lattice[x,y+1]  + (-J*SpinF*lattice[x-1,y])+  (-J*SpinF*lattice[x+1,y]) + (-J*SpinI*lattice[x,y-1])
                elif x==N-1  and y != 0 : 
                    Ei += -J*SpinI*lattice[x,y+1]  + (-J*SpinI*lattice[x-1,y])+  (-J*SpinI*lattice[x,y-1]) +  (-J*SpinI*lattice[0,y])
                    Ef += -J*SpinF*lattice[x,y+1]  + (-J*SpinF*lattice[x-1,y])+  (-J*SpinF*lattice[x,y-1]) +  (-J*SpinI*lattice[0,y])
                elif  y== N-1 and x != 0: 
                    Ei += -J*SpinI*lattice[x+1,y]  + (-J*SpinI*lattice[x-1,y])+  (-J*SpinI*lattice[x,y-1]) + (-J*SpinI*lattice[x,0])
                    Ef += -J*SpinF*lattice[x+1,y]  + (-J*SpinF*lattice[x-1,y])+  (-J*SpinF*lattice[x,y-1]) + (-J*SpinI*lattice[x,0]) 
                else: 
                    Ei += -J*SpinI*lattice[x,y-1] + (-J*SpinI*lattice[x-1,y]) + (-J*SpinI*lattice[x,y+1])+  (-J*SpinI*lattice[x+1,y])
                    Ef += -J*SpinF*lattice[x,y-1] + (-J*SpinF*lattice[x-1,y]) + (-J*SpinF*lattice[x,y+1])+  (-J*SpinF*lattice[x+1,y])
                Delta_E= Ef - Ei  
                if Delta_E <=0:  
                    E += Delta_E    
                    lattice[x,y]=SpinF  
                else:
                    z = random.random()  
                    if z < e^(-temp_B*Delta_E):  
                        E += Delta_E 
                        lattice[x,y]=SpinF 

                    if  tot_spins > 0.6* 10000 :
                        Es += E
            E_list.append(Es)
    return E_list
EP=Metropolis_lattice_plotting(A,10000,0.6,1)
EP

plt.figure(figsize=(20,10))
plt.plot(beta,EP,'g')
plt.title('PLot of Beta vs Energy of the lattice')
plt.ylabel('Energy of lattice')
plt.xlabel('Beta')

def Metropolis_lattice_plotting_mg(lattice,n,temp_B, J):
    for g in range(len(beta)):
        Es=0
        magnetisation=0
        Magnetisation=[]
        Sl = []
        E2_avg = 0
        E_avg  = 0
        Cv=[]
        X=[]
        S=0
        S2=0
        for k in beta:  
            temp_B = k
            for w in range(n):
                tot_spins= w
                Ei=0 
                Ef=0  
                E=Etot_i 

                x = ZZ.random_element(0,N)
                y= ZZ.random_element(0,N)  
                SpinI = lattice[x,y]  

                SpinF = (-1)*SpinI
                if x==0 and y==0 : 
                    Ei += -J*SpinI*lattice[x,y+1] + (-J*SpinI*lattice[x+1,y]) + (-J*SpinI*lattice[N-1,N-1]) + (-J*SpinI*lattice[x,N-1])  
                    Ef += -J*SpinF*lattice[x,y+1] + (-J*SpinF*lattice[x+1,y]) + (-J*SpinI*lattice[N-1,N-1]) + (-J*SpinI*lattice[x,N-1]) 
                elif x==0 and y==N-1 :
                    Ei += -J*SpinI*lattice[x,y-1] +  (-J*SpinI*lattice[x+1,y]) + (-J*SpinI*lattice[N-1,x]) +  (-J*SpinI*lattice[x,x])
                    Ef += -J*SpinF*lattice[x,y-1] +  (-J*SpinF*lattice[x+1,y]) +  (-J*SpinI*lattice[N-1,x]) +  (-J*SpinI*lattice[x,x])
                elif y==0 and  x == N-1: 
                    Ei += -J*SpinI*lattice[x,y+1] + (-J*SpinI*lattice[x-1,y])  + (-J*SpinI*lattice[y,N-1]) + -J*SpinI*lattice[N-1,N-1]
                    Ef += -J*SpinF*lattice[x,y+1] + (-J*SpinF*lattice[x-1,y]) + (-J*SpinI*lattice[y,N-1]) + -J*SpinI*lattice[N-1,N-1]
                elif y==N-1 and x==N-1:
                    Ei += -J*SpinI*lattice[x,y-1] +  (-J*SpinI*lattice[x-1,y]) + (-J*SpinI*lattice[N-1,0]) + -J*SpinI*lattice[0,0]
                    Ef += -J*SpinF*lattice[x,y-1] +  (-J*SpinF*lattice[x-1,y]) +  (-J*SpinI*lattice[N-1,0]) + -J*SpinI*lattice[0,0]
                elif x==0 and y != N-1 and y != 0: 
                    Ei += -J*SpinI*lattice[x,y-1]  + (-J*SpinI*lattice[x,y+1])+  (-J*SpinI*lattice[x+1,y]) + (-J*SpinI*lattice[x-1,y])
                    Ef += -J*SpinF*lattice[x,y-1]  + (-J*SpinF*lattice[x,y+1])+  (-J*SpinF*lattice[x+1,y])  +(-J*SpinI*lattice[x-1,y])
                elif y==0 and x !=0   :  
                    Ei += -J*SpinI*lattice[x,y+1]  + (-J*SpinI*lattice[x-1,y])+  (-J*SpinI*lattice[x+1,y]) + (-J*SpinI*lattice[x,y-1])
                    Ef += -J*SpinF*lattice[x,y+1]  + (-J*SpinF*lattice[x-1,y])+  (-J*SpinF*lattice[x+1,y]) + (-J*SpinI*lattice[x,y-1])
                elif x==N-1  and y != 0 : 
                    Ei += -J*SpinI*lattice[x,y+1]  + (-J*SpinI*lattice[x-1,y])+  (-J*SpinI*lattice[x,y-1]) +  (-J*SpinI*lattice[0,y])
                    Ef += -J*SpinF*lattice[x,y+1]  + (-J*SpinF*lattice[x-1,y])+  (-J*SpinF*lattice[x,y-1]) +  (-J*SpinI*lattice[0,y])
                elif  y== N-1 and x != 0: 
                    Ei += -J*SpinI*lattice[x+1,y]  + (-J*SpinI*lattice[x-1,y])+  (-J*SpinI*lattice[x,y-1]) + (-J*SpinI*lattice[x,0])
                    Ef += -J*SpinF*lattice[x+1,y]  + (-J*SpinF*lattice[x-1,y])+  (-J*SpinF*lattice[x,y-1]) + (-J*SpinI*lattice[x,0]) 
                else: 
                    Ei += -J*SpinI*lattice[x,y-1] + (-J*SpinI*lattice[x-1,y]) + (-J*SpinI*lattice[x,y+1])+  (-J*SpinI*lattice[x+1,y])
                    Ef += -J*SpinF*lattice[x,y-1] + (-J*SpinF*lattice[x-1,y]) + (-J*SpinF*lattice[x,y+1])+  (-J*SpinF*lattice[x+1,y])
                Delta_E= Ef - Ei  
                if Delta_E <=0: 
                    E += Delta_E   
                    lattice[x,y]=SpinF  
                else:
                    z = random.random() 
                    if z < e^(-temp_B*Delta_E):  
                        E += Delta_E
                        lattice[x,y]=SpinF 

                    if  tot_spins > 0.6* 10000 :
                        Es += E^2
                        E_avg += (1/w*E)^2
                        E2_avg += (1/w*Es)
            Sl.append(sum(lattice))
            S=1/N^2*sum(lattice)
            S2=1/N^2*sum(lattice^2)
            Cv.append(1/N^2*(temp_B*J)^2*(E2_avg-E_avg))
            X.append(1/N^2*temp_B*J*(S2 - S^2))
            magnetisation= 1/N^2*(sum(lattice))
            Magnetisation.append(magnetisation)
    return Sl , Magnetisation , Cv  , X
                    
Data=Metropolis_lattice_plotting_mg(A,10000,0.6,1)

Spins ,  Maget , CV  , Xp  = Data 
plt.figure(figsize=(20,10))
plt.plot(beta,Spins)
plt.title('PLot of Beta vs Sum of all spins on the lattice')
plt.ylabel('Spins')
plt.xlabel('Beta')
plt.figure(figsize=(20,10))
plt.plot(beta,Maget)
plt.title('PLot of Beta vs Magnetisation of the lattice')
plt.ylabel('Magnetisation')
plt.xlabel('Beta')
plt.figure(figsize=(20,10))
plt.plot(beta,CV)
plt.title('PLot of Beta vs Specific Heat')
plt.ylabel('Specific Heat ')
plt.xlabel('Beta')
plt.figure(figsize=(20,10))
plt.plot(beta,Xp)
plt.title('PLot of Beta vs Paramagnetic State')
plt.ylabel('Paramagnetic State')
plt.xlabel('Beta')




# Completing the project of the Ising Model using the Metropolis Algorithm on the 2-dimensional lattice of N x N lattice. After performing 10 000 flips at different temperatures. When we decrease the temperature of the system reaches equilibrium much faster since there is not enough energy to flip the Spins. Calculating the magnetisation of the system as temperature decreases the  Magnetisations go to 1. But for Specific Heat as we decrease the temperature of the system the specific heat capacity goes to infinity and the Paramagnetic State goes to zero.]
# 
# 
# Comparing Plots of  Temperature vs Specific  heat of online source: http://astro.physics.ncsu.edu/urca/course_files/Lesson23/index.html
# 
# ![specificheat_of_temp.png](attachment:specificheat_of_temp.png)
# 
# 
# 
# [1] F. Mandl, Statistical Physics (second edition, 1988), Wiley, ISBN 0-471-91533-5
# 
# 
# [2] http://astro.physics.ncsu.edu/urca/course_files/Lesson23/index.html
# 
# [3] http://www.bdhammel.com/ising-model/
# 
# 
# 
# 
