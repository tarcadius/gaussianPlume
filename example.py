import numpy as np
import matplotlib.pyplot as plt
import GaussianPlume

rate = 4. # g/s/m2
H = 1. # m
U = 3. # m/s
xGrid = np.linspace(0.1,2000,100) # m
yGrid = np.linspace(-150,150,100) # m
zGrid = 1. #m

areaSource = GaussianPlume.areaSource(0,1,50,-100,10,20,0,rate,H)
pointSource = GaussianPlume.pointSource(0,0,0,rate,H)
grid = GaussianPlume.receptorGrid(xGrid,yGrid,zGrid)
stability = GaussianPlume.stabilityClass('D')

a = GaussianPlume.gaussianPlume(pointSource,grid,stability,U)

concField = a.calculateConcentration()
concField_ppm = (concField*1000*24.45)/16.04

fig = plt.figure()
ax = fig.add_subplot(111)
c = ax.contourf(grid.xMesh[0],grid.yMesh[0],concField_ppm[0],100)
c2 = ax.contour(grid.xMesh[0], grid.yMesh[0], concField_ppm[0], [1], colors = "white")
c3 = ax.contour(grid.xMesh[0], grid.yMesh[0], concField_ppm[0], [0.5], colors = "white", linestyles = "dashed")
c4 = ax.contour(grid.xMesh[0], grid.yMesh[0], concField_ppm[0], [0.1], colors = "white", linestyles = "dotted")
c5 = ax.contour(grid.xMesh[0], grid.yMesh[0], concField_ppm[0], [0.01], colors = "gray", linestyles = "dotted")
cb = fig.colorbar(c)
cb.set_label('Mixing Ratio (ppm)')
ax.set_xlabel('X [m]')
ax.set_ylabel('Y [m]')

fig.show()

