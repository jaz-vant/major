import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Simulated data (replace with actual data)
num_points = 1000
vertical_positions = np.random.uniform(0, 10, num_points)
horizontal_positions = np.random.uniform(0, 2*np.pi, num_points)
distances = np.random.uniform(0.1, 10, num_points)

# Convert to Cartesian coordinates
x = distances * np.cos(horizontal_positions) * np.sin(vertical_positions)
y = distances * np.sin(horizontal_positions) * np.sin(vertical_positions)
z = distances * np.cos(vertical_positions)

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

plt.show()
