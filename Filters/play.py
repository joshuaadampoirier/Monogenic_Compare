import numpy as np
import matplotlib.pyplot as plt
from vertical import dz
from horizontal import *

def plot_edges(size):
    # First Break - Hingeline
    plt.plot([-50, -25], [-15, -15], color='k', linewidth=size,
             linestyle='--')
    plt.plot([-25, -10], [-5, -5], color='k', linewidth=size,
             linestyle='--')
    plt.plot([-25, -25], [-30, 20], color='k', linewidth=size*0.2,
             linestyle='--')
    plt.plot([-10, -10], [-25, 25], color='k', linewidth=size*0.2,
             linestyle='--')
    plt.plot([-10, 10], [0, 0], color='k', linewidth=size,
             linestyle='--')
    plt.plot([10, 10], [-20, 20], color='k', linewidth=size*0.2,
             linestyle='--')
    plt.plot([10, 30], [-3, -3], color='k', linewidth=size,
             linestyle='--')
    plt.plot([30, 30], [-20, 20], color='k', linewidth=size*0.2,
             linestyle='--')
    plt.plot([30, 50], [-5, -5], color='k', linewidth=size,
             linestyle='--')

    # Continental Oceanic Boundary - COB
    plt.plot([-50, -25], [0, 0], color='w', linewidth=size,
             linestyle='--')
    plt.plot([-25, -10], [3, 3], color='w', linewidth=size,
             linestyle='--')
    plt.plot([-10, 10], [12, 12], color='w', linewidth=size,
             linestyle='--')
    plt.plot([10, 30], [15, 15], color='w', linewidth=size,
             linestyle='--')
    plt.plot([30, 50], [10, 10], color='w', linewidth=size,
             linestyle='--')

    # Intrusion
    plt.plot([0, 10], [30, 30], color='r', linewidth=size,
             linestyle='--')
    plt.plot([0, 0], [30, 40], color='r', linewidth=size,
             linestyle='--')
    plt.plot([0, 10], [40, 40], color='r', linewidth=size,
             linestyle='--')
    plt.plot([10, 10], [30, 40], color='r', linewidth=size,
             linestyle='--')

    # Dike
    plt.plot([-50, -0.95], [-35, -10], color='0.35', linewidth=2.5,
             linestyle='--')

# Open File "data.dat" and import data
data = np.loadtxt("data.dat")
xp = data[:, 0]
yp = data[:, 1]
zp = data[:, 2]
tf = data[:, 3]

grd_shape = (200, 200)

xp = np.reshape(xp, grd_shape)
yp = np.reshape(yp, grd_shape)
zp = np.reshape(zp, grd_shape)
tf = np.reshape(tf, grd_shape)

# Plotting the total-field anomaly
fig = plt.figure(figsize=(10, 10))
plt.title('Total Field Anomaly')
plt.gca().set_aspect('equal', adjustable='box')
plt.contourf(yp/1000, xp/1000, tf, 50, cmap=plt.cm.RdBu_r)
cb = plt.colorbar()
cb.set_label("nT", labelpad=30, rotation=0)
plt.xlabel('Easting Coordinate (km)')
plt.ylabel('Northing Coordinate (km)')
plot_edges(3)
fig.savefig('Total Field.png')

# first x and y derivatives using convolution
dx1con, dy1con = dxdy_conv(tf, xp, yp)

# Plotting the total-field anomaly
fig = plt.figure(figsize=(10, 10))
plt.title('dx1 - Convolution')
plt.gca().set_aspect('equal', adjustable='box')
plt.contourf(yp/1000, xp/1000, dx1con, 50, cmap=plt.cm.RdBu_r)
cb = plt.colorbar()
cb.set_label("nT/m", labelpad=30, rotation=0)
plt.xlabel('Easting Coordinate (km)')
plt.ylabel('Northing Coordinate (km)')
plot_edges(3)
fig.savefig('dx1 CONV.png')

# Plotting the total-field anomaly
fig = plt.figure(figsize=(10, 10))
plt.title('dy1 - Convolution')
plt.gca().set_aspect('equal', adjustable='box')
plt.contourf(yp/1000, xp/1000, dy1con, 50, cmap=plt.cm.RdBu_r)
cb = plt.colorbar()
cb.set_label("nT/m", labelpad=30, rotation=0)
plt.xlabel('Easting Coordinate (km)')
plt.ylabel('Northing Coordinate (km)')
plot_edges(3)
fig.savefig('dy1 CONV.png')

# first x and y derivatives using FFT
dx1fft, dy1fft = dx_fft(tf, xp, yp), dy_fft(tf, xp, yp)

# Plotting the total-field anomaly
fig = plt.figure(figsize=(10, 10))
plt.title('dx1 - FFT')
plt.gca().set_aspect('equal', adjustable='box')
plt.contourf(yp/1000, xp/1000, dx1fft, 50, cmap=plt.cm.RdBu_r)
cb = plt.colorbar()
cb.set_label("nT/m", labelpad=30, rotation=0)
plt.xlabel('Easting Coordinate (km)')
plt.ylabel('Northing Coordinate (km)')
plot_edges(3)
fig.savefig('dx1 FFT.png')

# Plotting the total-field anomaly
fig = plt.figure(figsize=(10, 10))
plt.title('dy1 - FFT')
plt.gca().set_aspect('equal', adjustable='box')
plt.contourf(yp/1000, xp/1000, dy1fft, 50, cmap=plt.cm.RdBu_r)
cb = plt.colorbar()
cb.set_label("nT/m", labelpad=30, rotation=0)
plt.xlabel('Easting Coordinate (km)')
plt.ylabel('Northing Coordinate (km)')
plot_edges(3)
fig.savefig('dy1 FFT.png')

# first vertical derivatives
dz1 = dz(tf, xp, yp)

# Plotting the total-field anomaly
fig = plt.figure(figsize=(10, 10))
plt.title('First Vertical Derivative')
plt.gca().set_aspect('equal', adjustable='box')
plt.contourf(yp/1000, xp/1000, dz1, 50, cmap=plt.cm.RdBu_r)
cb = plt.colorbar()
cb.set_label("nT/m", labelpad=30, rotation=0)
plt.xlabel('Easting Coordinate (km)')
plt.ylabel('Northing Coordinate (km)')
plot_edges(3)
fig.savefig('dz1.png')
