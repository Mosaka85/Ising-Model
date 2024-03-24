
# ###  Abstract 
# 
# In this project, python was used to investigate the problem called an Ising model. A random lattice was created consisting of spins UP(+1) and Down(-1). Using the Metropolis algorithm a random spin was chosen and flipped following the Metropolis Algorithm. After numerous amount of spins, all spins in the lattice have the same spin. Metropolis Algorithm was defined as a function that returns the spins in the lattice after several spins.  During the process, a change in energy was calculated followed by total spin, Magnetisation, Specific heat, and the paramagnetic state of the lattice.
# 
# 
# ### Introduction
# 
# Before we begin the investigation of the Ising Model let us understand the Metropolis Algorithm. Considering we have a state i we then change the state to j. The equilibrium flow from i to j must be balanced by the flow from i to j and this can be expressed as 
# 
# $ \displaystyle  p_i T_{i -> j} = p_j T_{j -> i}   $
# 
# where
# - $p_i$ is the propability that the system is in state i
# 
# - $p_j$ is the propability that the system is in state j
# 
# - $T_{i -> j}$ is the propability that the system will transition from state i to j
# 
# - $T_{j -> i} $  is the propability that the system will transition from state j to i
# 
# Rearranging the equation we have that 
# 
# 
# $ \displaystyle \frac{T_{i -> j}}{T_{j -> i}}  = \frac{p_i}{p_j}   $
# 
# 
# According to the principles of Statistical physics. The  probability that a system  at a temperature T should be in a particular state with energy $E_r$ is given by 
# 
# 
# $  \displaystyle  P_r = \frac{1}{Z}  e^{-\beta E_r}    $
# 
# Where Z is the partition function  given by  
# 
# 
# $ \displaystyle Z= \Sigma_r e^{-\beta E_r} $ 
# 
# 
# and
# 
# 
# $ \displaystyle \beta = \frac{1}{k_B T}  $
# 
# therefore   simplifying the equation we have 
# 
# $  \displaystyle \frac{T_{i -> j}}{T_{j -> i}} =   e^{-\beta (E_i - E_j) }   $
# 
# During the computation, we want to choose states which obey the distribution  $ p_i $. Therefore we chose the transition rates such that
# 
# $ \displaystyle \frac{T_{i -> j}}{T_{j -> i}} = \begin{cases} 
#          1 & \textrm{ if $\Delta$E < 0 } \\
#      e^{-\beta (E_i - E_j) }  & \textrm{ if  $\Delta$E > 0} \\
#    \end{cases} $
#    
# To do this random number Z will be chosen such that  $0<Z<1$ 
# 
# and the  system will be moved from state $i$ to $j $ if  
# 
# $\displaystyle Z <  e^{-\beta (E_i - E_j)} $
# 

# ## The Ising Model Computational method  
# 
# To do this experiment generate a 10 x 10 matrix call it matrix A which will contain an array of numbers +1 or -1. When a spin has +1  say points  Upwards and when a Spin has -1  say points downwards.  
# 
# 
# Generating a random 10 x 10 matrix with spins chosen randomly. We begin by choosing a random X and Y value where X represents a row number and Y represents a column number in the matrix. Selecting a random spin based on X and Y values. We calculate the energy of the nearest spins where the Equation is given by 
# 
# $  \displaystyle  E = -J \sum_{i,j_i} S_i \cdot S_{j_i}  $
# 
# Using The Metropolis Method 
# 
# Calculate the energy of Spin below, above and on the sides of the spin which means each spin has 4 neighbours. But since we have a square matrix a pin can be on the edge or the corner.  If a matrix is on the edge we sum the energy of the three neighbours and take a spin at the opposite edge as the neighbour. To illastrate, imagine having folding a piece of paper as shown below.
# 
# Figure 1:  let this paper represend the lattice we have 
# <img src="Lattice1.jpeg"  width="200" height="200">
# 
# To find the neighbours of the spins on the cornder we fold  the paper as shown below
# Figure 2:
# <img src="Lattice2.jpeg"  width="200" height="200">
# 
# A spin on the edge has a neighbour on the opposite edge of the paper. Folding both ends of the paper in  Figure 2 we have a Doughnut shape means that the spin in the corner will have 2 neighbours on the opposite corners of the lattice one on the side and one below/above. Now Each spin will have 4 neighbours. 
# 
# The Chone spin gets flipped then we calculate the energy after the spin was flipped call this final energy. Calculate the change in energy before and after a flip. We use the metropolis Algorithm to determine whether to flip the spin or not using the equation below.
# 
# 
# $ \displaystyle \frac{T_{i -> j}}{T_{j -> i}} = \begin{cases} 
#          1 & \textrm{ if $\Delta$E < 0 } \\
#      e^{-\beta (E_i - E_j) }  & \textrm{ if  $\Delta$E > 0} \\
#    \end{cases} $
#  
# random number Z will be chosen such that  $0<Z<1$ 
# 
# and the  system will be moved from state $i$ to $j $ if  
# 
# $\displaystyle Z <  e^{-\beta (E_i - E_j)} $
#    
# Then we update the spin in the Lattice and repeat the process
# while performing the flips we record the change in energy as we flip the spins to calculate the Total energy.
# 
# To Calculate the magnetisation of the system  we use the following equation 
# 
# 
# $ \displaystyle    M = \frac{1}{M} \sum_i S_i     $
# 
# If we Calculate $<E>^2$ and $<E^2>$ the averages of energy of the system 
# 
# we can calculate the specific heat of the system   using 
# 
# 
# 
# 
# $ \displaystyle  C_v = \frac{1}{N^2}(\frac{J}{k_B T})^2(<E^2>-<E>^2)  $
# 
# 
# 
# Finally the Paramagnetic state 
# 
# 
# $\displaystyle  X = \frac{J}{N^2 k_B T}(<S^2>-<S>^2)   $  where $  \displaystyle S = \sum_i S_i   $

# In[9]:


import random # module used to generate random numbers
import numpy as np 
N=10  # We will be dealing with N x N matrix
A=np.zeros((N,N)) # Defining a 10x10 matrix with zero entries
for i in range(N):
    
    for j in range(N):
        A[i][j]=random.choice([-1,1]) # subtituting the entry with ether -1 or 1 
# The matrix generated consist of +1 and -1 chosen randomly
A


# In[10]:


import matplotlib.pyplot as plt  #module used to virtualize our lattice 
plt.imshow(A,cmap ='Greens') # Plotting  The matrix A
plt.show()


# In[11]:


# In this cell I want to calculate the energy of the system before any flips
Ei=0
Ef=0
Etot_i=0
J=1
for x in range(N):
    for y in range(N):
        if x==0 and y==0 : #The spin is at the corner we take spins on the opposite corners as the neighbours
            # sum energy of the neighbouring spins
            Etot_i += -J*A[x][y]*A[x,y+1] + (-J*A[x][y]*A[x+1,y]) + (-J*A[x][y]*A[N-1,N-1]) + (-J*A[x][y]*A[x,N-1])
        elif x==0 and y==N-1 :   #The spin is at the corner we take spins on the opposite corners as the neighbours
            # sum energy of the neighbouring spins
            Etot_i += -J*A[x][y]*A[x,y-1] +  (-J*A[x][y]*A[x+1,y]) + (-J*A[x][y]*A[N-1,x]) +  (-J*A[x][y]*A[x,x])
           
        elif y==0 and  x == N-1: #The spin is at the corner we take spins on the opposite corners as the neighbours 
            # sum energy of the neighbouring spins
            Etot_i += -J*A[x][y]*A[x,y+1] + (-J*A[x][y]*A[x-1,y])  + (-J*A[x][y]*A[y,N-1]) + -J*A[x][y]*A[N-1,N-1]
            
        elif y==N-1 and x==N-1: #The spin is at the corner we take spins on the opposite corners as the neighbours
            # sum energy of the neighbouring spins
            Etot_i += -J*A[x][y]*A[x,y-1] +  (-J*A[x][y]*A[x-1,y]) + (-J*A[x][y]*A[N-1,0]) + -J*A[x][y]*A[0,0]
            
        elif x==0 and y != N-1 and y != 0: # the spin is on the edge it only has 3 neighbours  we take one on the opposite edge as a neighbour
            # sum energy of the neighbouring spins 
            Etot_i += -J*A[x][y]*A[x,y-1]  + (-J*A[x][y]*A[x,y+1])+  (-J*A[x][y]*A[x+1,y]) + (-J*A[x][y]*A[x-1,y])
            
        elif y==0 and x !=0   :  # th# the spin is on the edge it only has 3 neighbours  we take one on the opposite edge as a neighbour
            # sum energy of the neighbouring spins
            Etot_i += -J*A[x][y]*A[x,y+1]  + (-J*A[x][y]*A[x-1,y])+  (-J*A[x][y]*A[x+1,y]) + (-J*A[x][y]*A[x,y-1])
           
        elif x==N-1  and y != 0 :# the spin is on the edge it only has 3 neighbours  we take one on the opposite edge as a neighbour
            # sum energy of the neighbouring spins
            Etot_i += -J*A[x][y]*A[x,y+1]  + (-J*A[x][y]*A[x-1,y])+  (-J*A[x][y]*A[x,y-1]) +  (-J*A[x][y]*A[0,y])
           
        elif  y== N-1 and x != 0: # the spin is on the edge it only has 3 neighbours  we take one on the opposite edge as a neighbour
            # sum energy of the neighbouring spins
            Etot_i += -J*A[x][y]*A[x+1,y]  + (-J*A[x][y]*A[x-1,y])+  (-J*A[x][y]*A[x,y-1]) + (-J*A[x][y]*A[x,0])

        else: # the spin is inside the lattice not on the edge and not in the corner it has 4 neighbours
            # sum energy of the neighbouring spins
            Etot_i += -J*A[x][y]*A[x,y-1] + (-J*A[x][y]*A[x-1,y]) + (-J*A[x][y]*A[x,y+1])+  (-J*A[x][y]*A[x+1,y])
Etot_i


# - The energy of the system before performing any flips is 8.0
# 
# 
# We will define a function that will take in the Matrix (lattice) , Number of flips(n) , temp_B =$\beta$ and J 
# this function return  Matrix after a certain  number of spins.

# In[12]:


def Metropolis_lattice(lattice,n,temp_B, J):
    # Metropolis Algorithm
    for w in range(n):  # repeat the process n times 
        Ei=0 # initial energy  excluding energy before flips
        Ef=0 # final energy after flips 
        E=Etot_i  # Etot_i is initial  energy before flips 
        #choose a spin
        x = ZZ.random_element(0,N) # choosing a randoms value between 0 and 9
        y= ZZ.random_element(0,N)  # choosing a randoms value between 0 and 9
        SpinI = lattice[x,y]  # choosing a random spin in the lattice 
        # Flip the spin 
        SpinF = (-1)*SpinI
        #definie the conditions 
        # After choosing a random spin the we flip the spin
        # After fliping the spin sum the energy of the neighbouring spins 
        # We sum energy of the  4 neighouring spins  but if the spin is the the edgewe take spin the the other edge 
        if x==0 and y==0 : #The spin is at the corner we take spins on the opposide corners as the neighbors
            # sum energy of the neighbouring spins
            Ei += -J*SpinI*lattice[x,y+1] + (-J*SpinI*lattice[x+1,y]) + (-J*SpinI*lattice[N-1,N-1]) + (-J*SpinI*lattice[x,N-1])  
            Ef += -J*SpinF*lattice[x,y+1] + (-J*SpinF*lattice[x+1,y]) + (-J*SpinI*lattice[N-1,N-1]) + (-J*SpinI*lattice[x,N-1]) 
        elif x==0 and y==N-1 : #The spin is at the corner we take spins on the opposide corners as the neighbors
            # sum energy of the neighbouring spins
            Ei += -J*SpinI*lattice[x,y-1] +  (-J*SpinI*lattice[x+1,y]) + (-J*SpinI*lattice[N-1,x]) +  (-J*SpinI*lattice[x,x])
            Ef += -J*SpinF*lattice[x,y-1] +  (-J*SpinF*lattice[x+1,y]) +  (-J*SpinI*lattice[N-1,x]) +  (-J*SpinI*lattice[x,x])
        elif y==0 and  x == N-1: #The spin is at the corner we take spins on the opposide corners as the neighbors
            # sum energy of the neighbouring spins
            Ei += -J*SpinI*lattice[x,y+1] + (-J*SpinI*lattice[x-1,y])  + (-J*SpinI*lattice[y,N-1]) + -J*SpinI*lattice[N-1,N-1]
            Ef += -J*SpinF*lattice[x,y+1] + (-J*SpinF*lattice[x-1,y]) + (-J*SpinI*lattice[y,N-1]) + -J*SpinI*lattice[N-1,N-1]
        elif y==N-1 and x==N-1:#The spin is at the corner we take spins on the opposide corner as the neighbors
            # sum energy of the neighbouring spins
            Ei += -J*SpinI*lattice[x,y-1] +  (-J*SpinI*lattice[x-1,y]) + (-J*SpinI*lattice[N-1,0]) + -J*SpinI*lattice[0,0]
            Ef += -J*SpinF*lattice[x,y-1] +  (-J*SpinF*lattice[x-1,y]) +  (-J*SpinI*lattice[N-1,0]) + -J*SpinI*lattice[0,0]
        elif x==0 and y != N-1 and y != 0: # the spin is on the edge it only has 3 neighbours  we take one on the oppside edge as neigbor
            # sum energy of the neighbouring spins 
            Ei += -J*SpinI*lattice[x,y-1]  + (-J*SpinI*lattice[x,y+1])+  (-J*SpinI*lattice[x+1,y]) + (-J*SpinI*lattice[x-1,y])
            Ef += -J*SpinF*lattice[x,y-1]  + (-J*SpinF*lattice[x,y+1])+  (-J*SpinF*lattice[x+1,y])  +(-J*SpinI*lattice[x-1,y])
        elif y==0 and x !=0   :  # the spin is on the edge it only has 3 neighbours  we take one on the oppside edge as neigbor
            # sum energy of the neighbouring spins
            Ei += -J*SpinI*lattice[x,y+1]  + (-J*SpinI*lattice[x-1,y])+  (-J*SpinI*lattice[x+1,y]) + (-J*SpinI*lattice[x,y-1])
            Ef += -J*SpinF*lattice[x,y+1]  + (-J*SpinF*lattice[x-1,y])+  (-J*SpinF*lattice[x+1,y]) + (-J*SpinI*lattice[x,y-1])
        elif x==N-1  and y != 0 : # the spin is on the edge it only has 3 neighbours  we take one on the oppside edge as neigbor
            # sum energy of the neighbouring spins
            Ei += -J*SpinI*lattice[x,y+1]  + (-J*SpinI*lattice[x-1,y])+  (-J*SpinI*lattice[x,y-1]) +  (-J*SpinI*lattice[0,y])
            Ef += -J*SpinF*lattice[x,y+1]  + (-J*SpinF*lattice[x-1,y])+  (-J*SpinF*lattice[x,y-1]) +  (-J*SpinI*lattice[0,y])
        elif  y== N-1 and x != 0: # the spin is on the edge it only has 3 neighbours  we take one on the oppside edge as neigbor
            # sum energy of the neighbouring spins
            Ei += -J*SpinI*lattice[x+1,y]  + (-J*SpinI*lattice[x-1,y])+  (-J*SpinI*lattice[x,y-1]) + (-J*SpinI*lattice[x,0])
            Ef += -J*SpinF*lattice[x+1,y]  + (-J*SpinF*lattice[x-1,y])+  (-J*SpinF*lattice[x,y-1]) + (-J*SpinI*lattice[x,0]) 
        else: # the spin is inside the lattice not on the edge and not in the corner it has 4 neighbours
            # sum energy of the neighbouring spins
            Ei += -J*SpinI*lattice[x,y-1] + (-J*SpinI*lattice[x-1,y]) + (-J*SpinI*lattice[x,y+1])+  (-J*SpinI*lattice[x+1,y])
            Ef += -J*SpinF*lattice[x,y-1] + (-J*SpinF*lattice[x-1,y]) + (-J*SpinF*lattice[x,y+1])+  (-J*SpinF*lattice[x+1,y])
        # Calculating The chance in energy 
        Delta_E= Ef - Ei  
        if Delta_E <=0:  # check if the change in energy is positive
            E += Delta_E    # add the energy
            lattice[x,y]=SpinF  #Updating the flipped spin in the lattice
        else:
            z = random.random()  # choose a random number between 0and 1 (0 < z < 1) 
            if z < e^(-temp_B*Delta_E):  # check that if the random number is less than e^(beta*change_E)
                E += Delta_E # add the energy
                lattice[x,y]=SpinF  #Updating the flipped spin in the lattice
    # Vitualize The Lattice 
    # Using imshow from matplot libto vitualize the lattice
    plt.title('Lattice after   ' + str(   n) +'    flips' + '   for temperature betha ='+ str( temp_B)) #imshow title
    plt.imshow(lattice,cmap ='Greens')   # White means spin down and green is spin up
    plt.show()  # show the results
        


# In[13]:


for i in range(0,1): # Changing temperature from  0.00   to 0.90000000000000
    Metropolis_lattice(A,10000,i,1.2) # plot imshow for different temperatures


# - We see that  when  we increase  $\beta$ the system tend to stabilize qucker.  The higher the value of beta the lower the temperature. If we decrease the temperature of the system  the is no longer enough energy to flip the spins
# 
# 
# Generate a list consisting values of $\beta$

# In[117]:


beta=[i for i in srange(0,1.5,0.1)]  


# Defining a function that retruns the Total energy of the system after N spins

# In[118]:


def Metropolis_lattice_plotting(lattice,n,temp_B, J):
    for g in range(len(beta)):
        Es=0
        E_list=[]
        for k in beta:  
            temp_B = k
            for w in range(n):  # repeat the process n times
                tot_spins= w
                Ei=0 # initial energy  excluding energy before flips
                Ef=0 # final energy after flips 
                E=Etot_i  # Etot_i is initial  energy before flips 
                #choose a spin
                x = ZZ.random_element(0,N) # choosing a randoms value between 0 and 9
                y= ZZ.random_element(0,N)  # choosing a randoms value between 0 and 9
                SpinI = lattice[x,y]  # choosing a random spin in the lattice 
                # Flip the spin 
                SpinF = (-1)*SpinI
                #definie the conditions 
                # After choosing a random spin the we flip the spin
                # After fliping the spin sum the energy of the neighbouring spins 
                # We sum energy of the  4 neighouring spins  but if the spin is the the edgewe take spin the the other edge 
                if x==0 and y==0 : #The spin is at the corner we take spins on the opposide corners as the neighbor
                    # sum energy of the neighbouring spins
                    Ei += -J*SpinI*lattice[x,y+1] + (-J*SpinI*lattice[x+1,y]) + (-J*SpinI*lattice[N-1,N-1]) + (-J*SpinI*lattice[x,N-1])  
                    Ef += -J*SpinF*lattice[x,y+1] + (-J*SpinF*lattice[x+1,y]) + (-J*SpinI*lattice[N-1,N-1]) + (-J*SpinI*lattice[x,N-1]) 
                elif x==0 and y==N-1 : #The spin is at the corner we take spins on the opposide corners as the neighbor
                    # sum energy of the neighbouring spins
                    Ei += -J*SpinI*lattice[x,y-1] +  (-J*SpinI*lattice[x+1,y]) + (-J*SpinI*lattice[N-1,x]) +  (-J*SpinI*lattice[x,x])
                    Ef += -J*SpinF*lattice[x,y-1] +  (-J*SpinF*lattice[x+1,y]) +  (-J*SpinI*lattice[N-1,x]) +  (-J*SpinI*lattice[x,x])
                elif y==0 and  x == N-1: #The spin is at the corner we take spins on the opposide corners as the neighbor
                    # sum energy of the neighbouring spins
                    Ei += -J*SpinI*lattice[x,y+1] + (-J*SpinI*lattice[x-1,y])  + (-J*SpinI*lattice[y,N-1]) + -J*SpinI*lattice[N-1,N-1]
                    Ef += -J*SpinF*lattice[x,y+1] + (-J*SpinF*lattice[x-1,y]) + (-J*SpinI*lattice[y,N-1]) + -J*SpinI*lattice[N-1,N-1]
                elif y==N-1 and x==N-1:#The spin is at the corner we take spins on the opposide corner as the neighbor
                    # sum energy of the neighbouring spins
                    Ei += -J*SpinI*lattice[x,y-1] +  (-J*SpinI*lattice[x-1,y]) + (-J*SpinI*lattice[N-1,0]) + -J*SpinI*lattice[0,0]
                    Ef += -J*SpinF*lattice[x,y-1] +  (-J*SpinF*lattice[x-1,y]) +  (-J*SpinI*lattice[N-1,0]) + -J*SpinI*lattice[0,0]
                elif x==0 and y != N-1 and y != 0: # the spin is on the edge it only has 3 neighbours  we take one on the oppside edge as neigbor
                    # sum energy of the neighbouring spins 
                    Ei += -J*SpinI*lattice[x,y-1]  + (-J*SpinI*lattice[x,y+1])+  (-J*SpinI*lattice[x+1,y]) + (-J*SpinI*lattice[x-1,y])
                    Ef += -J*SpinF*lattice[x,y-1]  + (-J*SpinF*lattice[x,y+1])+  (-J*SpinF*lattice[x+1,y])  +(-J*SpinI*lattice[x-1,y])
                elif y==0 and x !=0   :  # the spin is on the edge it only has 3 neighbours  we take one on the oppside edge as neigbor
                    # sum energy of the neighbouring spins
                    Ei += -J*SpinI*lattice[x,y+1]  + (-J*SpinI*lattice[x-1,y])+  (-J*SpinI*lattice[x+1,y]) + (-J*SpinI*lattice[x,y-1])
                    Ef += -J*SpinF*lattice[x,y+1]  + (-J*SpinF*lattice[x-1,y])+  (-J*SpinF*lattice[x+1,y]) + (-J*SpinI*lattice[x,y-1])
                elif x==N-1  and y != 0 : # the spin is on the edge it only has 3 neighbours  we take one on the oppside edge as neigbor
                    # sum energy of the neighbouring spins
                    Ei += -J*SpinI*lattice[x,y+1]  + (-J*SpinI*lattice[x-1,y])+  (-J*SpinI*lattice[x,y-1]) +  (-J*SpinI*lattice[0,y])
                    Ef += -J*SpinF*lattice[x,y+1]  + (-J*SpinF*lattice[x-1,y])+  (-J*SpinF*lattice[x,y-1]) +  (-J*SpinI*lattice[0,y])
                elif  y== N-1 and x != 0: # the spin is on the edge it only has 3 neighbours  we take one on the oppside edge as neigbor
                    # sum energy of the neighbouring spins
                    Ei += -J*SpinI*lattice[x+1,y]  + (-J*SpinI*lattice[x-1,y])+  (-J*SpinI*lattice[x,y-1]) + (-J*SpinI*lattice[x,0])
                    Ef += -J*SpinF*lattice[x+1,y]  + (-J*SpinF*lattice[x-1,y])+  (-J*SpinF*lattice[x,y-1]) + (-J*SpinI*lattice[x,0]) 
                else: # the spin is inside the lattice not on the edge and not in the corner it has 4 neighbours
                    # sum energy of the neighbouring spins
                    Ei += -J*SpinI*lattice[x,y-1] + (-J*SpinI*lattice[x-1,y]) + (-J*SpinI*lattice[x,y+1])+  (-J*SpinI*lattice[x+1,y])
                    Ef += -J*SpinF*lattice[x,y-1] + (-J*SpinF*lattice[x-1,y]) + (-J*SpinF*lattice[x,y+1])+  (-J*SpinF*lattice[x+1,y])
                Delta_E= Ef - Ei  
                if Delta_E <=0:  # check if the change in energy is positive
                    E += Delta_E    # add the energy
                    lattice[x,y]=SpinF  #Updating the flipped spin in the lattice
                else:
                    z = random.random()  # choose a random number between 0and 1 (0 < z < 1) 
                    if z < e^(-temp_B*Delta_E):  # check that if the random number is less than e^(beta*change_E)
                        E += Delta_E # add the energy
                        lattice[x,y]=SpinF  #Updating the flipped spin in the lattice

                    if  tot_spins > 0.6* 10000 :
                        Es += E
            E_list.append(Es)
    return E_list
                    
                
                
        
    


# In[119]:


EP=Metropolis_lattice_plotting(A,10000,0.6,1)
EP


# In[120]:


plt.figure(figsize=(20,10))
plt.plot(beta,EP,'g')
plt.title('PLot of Beta vs Energy of the lattice')
plt.ylabel('Energy of lattice')
plt.xlabel('Beta')


# In[128]:


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
            for w in range(n):  # repeat the process n times
                tot_spins= w
                Ei=0 # initial energy  excluding energy before flips
                Ef=0 # final energy after flips 
                E=Etot_i  # Etot_i is initial  energy before flips 
                #choose a spin
                x = ZZ.random_element(0,N) # choosing a randoms value between 0 and 9
                y= ZZ.random_element(0,N)  # choosing a randoms value between 0 and 9
                SpinI = lattice[x,y]  # choosing a random spin in the lattice 
                # Flip the spin 
                SpinF = (-1)*SpinI
                #definie the conditions 
                # After choosing a random spin the we flip the spin
                # After fliping the spin sum the energy of the neighbouring spins 
                # We sum energy of the  4 neighouring spins  but if the spin is the the edgewe take spin the the other edge 
                if x==0 and y==0 : #The spin is at the corner we take spins on the opposide corners as the neighbor
                    # sum energy of the neighbouring spins
                    Ei += -J*SpinI*lattice[x,y+1] + (-J*SpinI*lattice[x+1,y]) + (-J*SpinI*lattice[N-1,N-1]) + (-J*SpinI*lattice[x,N-1])  
                    Ef += -J*SpinF*lattice[x,y+1] + (-J*SpinF*lattice[x+1,y]) + (-J*SpinI*lattice[N-1,N-1]) + (-J*SpinI*lattice[x,N-1]) 
                elif x==0 and y==N-1 : #The spin is at the corner we take spins on the opposide corners as the neighbor
                    # sum energy of the neighbouring spins
                    Ei += -J*SpinI*lattice[x,y-1] +  (-J*SpinI*lattice[x+1,y]) + (-J*SpinI*lattice[N-1,x]) +  (-J*SpinI*lattice[x,x])
                    Ef += -J*SpinF*lattice[x,y-1] +  (-J*SpinF*lattice[x+1,y]) +  (-J*SpinI*lattice[N-1,x]) +  (-J*SpinI*lattice[x,x])
                elif y==0 and  x == N-1: #The spin is at the corner we take spins on the opposide corners as the neighbor
                    # sum energy of the neighbouring spins
                    Ei += -J*SpinI*lattice[x,y+1] + (-J*SpinI*lattice[x-1,y])  + (-J*SpinI*lattice[y,N-1]) + -J*SpinI*lattice[N-1,N-1]
                    Ef += -J*SpinF*lattice[x,y+1] + (-J*SpinF*lattice[x-1,y]) + (-J*SpinI*lattice[y,N-1]) + -J*SpinI*lattice[N-1,N-1]
                elif y==N-1 and x==N-1:#The spin is at the corner we take spins on the opposide corner as the neighbor
                    # sum energy of the neighbouring spins
                    Ei += -J*SpinI*lattice[x,y-1] +  (-J*SpinI*lattice[x-1,y]) + (-J*SpinI*lattice[N-1,0]) + -J*SpinI*lattice[0,0]
                    Ef += -J*SpinF*lattice[x,y-1] +  (-J*SpinF*lattice[x-1,y]) +  (-J*SpinI*lattice[N-1,0]) + -J*SpinI*lattice[0,0]
                elif x==0 and y != N-1 and y != 0: # the spin is on the edge it only has 3 neighbours  we take one on the oppside edge as neigbor
                    # sum energy of the neighbouring spins 
                    Ei += -J*SpinI*lattice[x,y-1]  + (-J*SpinI*lattice[x,y+1])+  (-J*SpinI*lattice[x+1,y]) + (-J*SpinI*lattice[x-1,y])
                    Ef += -J*SpinF*lattice[x,y-1]  + (-J*SpinF*lattice[x,y+1])+  (-J*SpinF*lattice[x+1,y])  +(-J*SpinI*lattice[x-1,y])
                elif y==0 and x !=0   :  # the spin is on the edge it only has 3 neighbours  we take one on the oppside edge as neigbor
                    # sum energy of the neighbouring spins
                    Ei += -J*SpinI*lattice[x,y+1]  + (-J*SpinI*lattice[x-1,y])+  (-J*SpinI*lattice[x+1,y]) + (-J*SpinI*lattice[x,y-1])
                    Ef += -J*SpinF*lattice[x,y+1]  + (-J*SpinF*lattice[x-1,y])+  (-J*SpinF*lattice[x+1,y]) + (-J*SpinI*lattice[x,y-1])
                elif x==N-1  and y != 0 : # the spin is on the edge it only has 3 neighbours  we take one on the oppside edge as neigbor
                    # sum energy of the neighbouring spins
                    Ei += -J*SpinI*lattice[x,y+1]  + (-J*SpinI*lattice[x-1,y])+  (-J*SpinI*lattice[x,y-1]) +  (-J*SpinI*lattice[0,y])
                    Ef += -J*SpinF*lattice[x,y+1]  + (-J*SpinF*lattice[x-1,y])+  (-J*SpinF*lattice[x,y-1]) +  (-J*SpinI*lattice[0,y])
                elif  y== N-1 and x != 0: # the spin is on the edge it only has 3 neighbours  we take one on the oppside edge as neigbor
                    # sum energy of the neighbouring spins
                    Ei += -J*SpinI*lattice[x+1,y]  + (-J*SpinI*lattice[x-1,y])+  (-J*SpinI*lattice[x,y-1]) + (-J*SpinI*lattice[x,0])
                    Ef += -J*SpinF*lattice[x+1,y]  + (-J*SpinF*lattice[x-1,y])+  (-J*SpinF*lattice[x,y-1]) + (-J*SpinI*lattice[x,0]) 
                else: # the spin is inside the lattice not on the edge and not in the corner it has 4 neighbours
                    # sum energy of the neighbouring spins
                    Ei += -J*SpinI*lattice[x,y-1] + (-J*SpinI*lattice[x-1,y]) + (-J*SpinI*lattice[x,y+1])+  (-J*SpinI*lattice[x+1,y])
                    Ef += -J*SpinF*lattice[x,y-1] + (-J*SpinF*lattice[x-1,y]) + (-J*SpinF*lattice[x,y+1])+  (-J*SpinF*lattice[x+1,y])
                Delta_E= Ef - Ei  
                if Delta_E <=0:  # check if the change in energy is positive
                    E += Delta_E    # add the energy
                    lattice[x,y]=SpinF  #Updating the flipped spin in the lattice
                else:
                    z = random.random()  # choose a random number between 0and 1 (0 < z < 1) 
                    if z < e^(-temp_B*Delta_E):  # check that if the random number is less than e^(beta*change_E)
                        E += Delta_E # add the energy
                        lattice[x,y]=SpinF  #Updating the flipped spin in the lattice

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
                    
                
                
        
    


# In[122]:


Data=Metropolis_lattice_plotting_mg(A,10000,0.6,1)


# In[123]:


Spins ,  Maget , CV  , Xp  = Data 


# In[124]:


plt.figure(figsize=(20,10))
plt.plot(beta,Spins)
plt.title('PLot of Beta vs Sum of all spins on the lattice')
plt.ylabel('Spins')
plt.xlabel('Beta')


# In[125]:


plt.figure(figsize=(20,10))
plt.plot(beta,Maget)
plt.title('PLot of Beta vs Magnetisation of the lattice')
plt.ylabel('Magnetisation')
plt.xlabel('Beta')


# - Magnetisation  converges to 1 

# In[126]:


plt.figure(figsize=(20,10))
plt.plot(beta,CV)
plt.title('PLot of Beta vs Specific Heat')
plt.ylabel('Specific Heat ')
plt.xlabel('Beta')


# -   The Specific Heat increases when $\beta$ increases  
# - Cv diverges

# In[127]:


plt.figure(figsize=(20,10))
plt.plot(beta,Xp)
plt.title('PLot of Beta vs Paramagnetic State')
plt.ylabel('Paramagnetic State')
plt.xlabel('Beta')


# ##  Conclusion
# 
# 

# Completing the project of the Ising Model using the Metropolis Algorithm on the 2-dimensional lattice of N x N lattice. After performing 10 000 flips at different temperatures. When we decrease the temperature of the system reaches equilibrium much faster since there is not enough energy to flip the Spins. Calculating the magnetisation of the system as temperature decreases the  Magnetisations go to 1. But for Specific Heat as we decrease the temperature of the system the specific heat capacity goes to infinity and the Paramagnetic State goes to zero.]
# 
# 
# Comparing Plots of  Temperature vs Specific  heat of online source: http://astro.physics.ncsu.edu/urca/course_files/Lesson23/index.html
# 
# ![specificheat_of_temp.png](attachment:specificheat_of_temp.png)
# 
# ![image.png](attachment:image.png)
# 
# ![monte-carlo-ising-7.png](attachment:monte-carlo-ising-7.png)
# Source : http://www.bdhammel.com/ising-model/
# 
# 
# The plots we obtained in our investigation are  similar to the ones above . The computation perfomed above is consistent.
# 
# 
# ### Referances 
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
