#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import cv2
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread('download.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Use Canny edge detection to find edges in the image
edges = cv2.Canny(gray, 50, 150)

# Find contours in the edge-detected image
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Create an empty 3D point cloud
point_cloud = []

# Iterate through each contour and extract points to form the point cloud
for contour in contours:
    for point in contour:
        x, y = point[0]
        point_cloud.append([x, y, 0])  # Assuming z=0 for all points (no depth information)

# Convert the point cloud to a numpy array
point_cloud = np.array(point_cloud)

# Plot the point cloud in 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(point_cloud[:,0], point_cloud[:,1], point_cloud[:,2], c='b', marker='o')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()

