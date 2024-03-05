import serial
import time
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pyvista as pv
try:
    tfmini_s = serial.Serial('/dev/AMA0',115200,timeout=1)
except Exception as e:
    print(f"Error occured with serial port, {e}")
    exit()
    
def convert_distance_data(data):
    dist_l = data[2]
    dist_h = data[3]
    dist_total = (dist_h << 8) + dist_l  
    return dist_total
i=0
def lidar(tfmini_s):
    while True:
        try:
            while tfmini_s.in_waiting < 9:
                pass
            data = tfmini_s.read(9)
            if len(data) >= 9 and data[0] == 0x59 and data[1] == 0x59:
                distance = convert_distance_data(data)
                return distance
height = 0
x=[]
y=[]
z=[]
points = [[]]
while height<20:
    while i<360:
        d= lidar(tfmini_s)
        L=[d,height,i]
        points.append(L)
        time.sleep(2)
        i+=1 #increment this based on the stepper motor count
    height+=1 #increment this based on the dc motor count
def convert_points(points,x,y,z):
    for i in points:
        x_d=points[i][0]
        y_=points[i][1]
        a=points[i][2]
        l_x.append(x*np.cos(a))
        l_y.append(y)
        l_z.append(x*np.sin(a))
        
convert_points(points,cord)
x = np.array(l_x)
y = np.array(l_y)
z = np.array(l_z)
# Visualize the point cloud
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x, y, z, c='b', marker='.')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Point Cloud Visualization')

# Save the point cloud to a PLY file
with open('point_cloud.ply', 'w') as f:
    f.write('ply\n')
    f.write('format ascii 1.0\n')
    f.write(f'element vertex {num_points}\n')
    f.write('property float x\n')
    f.write('property float y\n')
    f.write('property float z\n')
    f.write('end_header\n')
    for i in range(num_points):
        f.write(f'{x[i]:.6f} {y[i]:.6f} {z[i]:.6f}\n')


# Load point cloud data
point_cloud = pv.read('point_cloud.ply')

# Surface reconstruction
surface = point_cloud.delaunay_2d()

# Save the surface mesh
# surface.save('surface_mesh.obj')
# print("Saved surface_mesh succesfully")
# Visualize the surface mesh
plt.show()
surface.plot()