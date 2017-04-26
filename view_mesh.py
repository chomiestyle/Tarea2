import scipy as sp
from mayavi import mlab

xyz = sp.loadtxt("aspa_nodos.txt")
elementos = sp.loadtxt("aspa_elementos.txt")

Nnodos = xyz.shape[0]
Nelems = elementos.shape[0]

print "Nnodos = ", Nnodos
print xyz
print "Nelems = ", Nelems
print elementos



mlab.triangular_mesh(xyz[:,0], xyz[:,1], xyz[:,2], elementos[:,1:])
mlab.show()