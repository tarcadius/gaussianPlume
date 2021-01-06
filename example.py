import numpy as np
import matplotlib.pyplot as plt
import gaussianPlume

rate = 10. # g/s/m2
H = 2.38 # m
U = 1.75 # m/s
xGrid = np.linspace(0.1,60,100) # m
yGrid = np.linspace(-25,25,100) # m
zGrid = 6. #m

areaSource = gaussianPlume.areaSource(0,1,50,-100,10,20,0,rate,H)
pointSource = gaussianPlume.pointSource(0,0,0,rate,H)
grid = gaussianPlume.receptorGrid(xGrid,yGrid,zGrid)
stability = gaussianPlume.stabilityClass('D')

a = gaussianPlume.gaussianPlume(pointSource,grid,stability,U)

concField = a.calculateConcentration()
concField_ppm = (concField*1000*24.45)/16.04

fig = plt.figure()
ax = fig.add_subplot(111)
c = ax.contourf(grid.xMesh[0],grid.yMesh[0],concField_ppm[0],100)
cb = fig.colorbar(c)
cb.set_label('Mixing Ratio (ppm)')
ax.set_xlabel('X [m]')
ax.set_ylabel('Y [m]')

fig.show()
