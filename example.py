import numpy as np
import matplotlib.pyplot as plt
import gaussianPlume

rates = np.array([0.004,0.04, 0.4, 4.0])

rate = 4. # g/s/m2
H = 1. # m
U = 3 # m/s
xGrid = np.linspace(0.1,2000,100) # m
yGrid = np.linspace(-150,150,100) # m
zGrid = 2. #m

areaSource = gaussianPlume.areaSource(0,1,50,-100,10,20,0,rate,H)
pointSource = gaussianPlume.pointSource(0,0,0,rate,H)
grid = gaussianPlume.receptorGrid(xGrid,yGrid,zGrid)
stability = gaussianPlume.stabilityClass('D')

a = gaussianPlume.gaussianPlume(pointSource,grid,stability,U)

concField = a.calculateConcentration()
concField_ppm = (concField*1000*24.45)/16.04

end = 5

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
