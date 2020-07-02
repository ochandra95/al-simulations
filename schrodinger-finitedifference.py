import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg as la
#Finite Difference Approximations for solving the time-independent Schrodinger

#STEP 1: Build the mesh

#define number of grid points and mesh spacing

n=int(input('enter number of grid points: '))
a=float(input('enter lower limit of domain: '))
b=float(input('enter upper limit of domain: '))
v=str(input('enter potential type (constant, linear, or quadratic): '))
e=int(input('enter number of eigenfunctions to plot: '))
#n=100
#b=1
#a=0
#e=5
#v='quadratic'
xf=b-a
dx=xf/(n+1)
x = np.linspace(0,xf,n)
print(x)

#allocate space for the operator matrix
H=np.zeros(shape=(n,n))
#Define constants and potential
p=1
def V(x):
    if v=='constant':
        return 0*x
    if v=='linear':
        return x
    if v=='quadratic':
        return x**2
    else:
        print('Invalid potential! Try again.')
        exit()
potential=V(x)
print(len(potential))

#Define boundary conditions

H[0,0]=2*p+V(x[0])
H[0,1]=-p
H[n-1,n-2]=-p
H[n-1,n-1]=2*p+V(x[n-1])

#Fill in the rest of the matrix
for j in range (1, n):
    H[j-1,j-2]=-p
    H[j-1,j-1]=2*p+V(x[j-1])
    H[j-1,j]=-p
print(H)
#Solve for the eigenvalues and eigenvectors, sort them from smallest to largest (abs)
val, vec=np.linalg.eig(H)
z=np.argsort(val)
z=z[0:e]
print(z)
#normalize
energies=(val[z]/val[z][0])
print('the number of selected eigenvalues is:')
print(len(z))
print('The energies are:')
print(energies)



#Plot the eigenfunctions and the potential
plt.figure(figsize=(10,10))
for i in range(len(z)):
    y=[]
    y=np.append(y,vec[:,z[i]])
    print ('eigenvector number:')
    print(i+1)
    print(y)
    plt.plot(x,y,lw=3,label="{} ".format(i))
    plt.plot(x,potential, label='{}'.format(i))
    plt.xlabel('x', size=14)
    plt.xlim([0, 1])
    plt.ylabel('$\psi$(x)', size=14)
plt.legend()
plt.title('Normalized eigenfunctions',size=14)
plt.show()
