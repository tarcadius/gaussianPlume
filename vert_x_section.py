import numpy as np
import matplotlib.pyplot as plt
import GaussianPlume
from matplotlib.colors import LogNorm

concMesh = np.empty((100,100))
xMesh = np.empty((100,100))
zMesh = np.empty((100,100))

z_layers = np.linspace(0.1, 20, 100)
for i in range(len(z_layers)):
    rate = 0.4 # g/s/m2
    H = 1. # m
    U = 3. # m/s
    xGrid = np.linspace(0.1,500,100) # m
    yGrid = np.linspace(-0.001,0.001,100) # m
    zGrid = z_layers[i] #m

    areaSource = GaussianPlume.areaSource(0,1,50,-100,10,20,0,rate,H)
    pointSource = GaussianPlume.pointSource(0,0,0,rate,H)
    grid = GaussianPlume.receptorGrid(xGrid,yGrid,zGrid)
    stability = GaussianPlume.stabilityClass('D')

    a = GaussianPlume.gaussianPlume(pointSource,grid,stability,U)

    concField = a.calculateConcentration()
    concField_ppm = (concField*1000*24.45)/16.04

    concMesh[i] = concField_ppm[0][50]
    xMesh[i] = grid.xMesh[0][i]
    zMesh[i] = grid.zMesh[0][i]

fig = plt.figure()
ax = fig.add_subplot(111)
c = ax.contourf(xMesh,zMesh,concMesh,levels= np.arange(0, 10.5, 0.5), extend='both')
c2 = ax.contour(xMesh, zMesh, concMesh, [1], colors = "white")
c3 = ax.contour(xMesh, zMesh, concMesh, [0.5], colors = "white", linestyles = "dashed")
c4 = ax.contour(xMesh, zMesh, concMesh, [0.1], colors = "white", linestyles = "dotted")
c5 = ax.contour(xMesh, zMesh, concMesh, [0.01], colors = "gray", linestyles = "dotted")
plt.axhline(y=2, color='r', linestyle='-')
cb = fig.colorbar(c)
cb.set_label('Mixing Ratio (ppm)')
ax.set_xlabel('Distance from source [m]')
ax.set_ylabel('Height [m]')

fig.show()

fig.savefig("pltB.png")


