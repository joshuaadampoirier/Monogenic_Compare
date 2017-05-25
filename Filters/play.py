import numpy as np
import matplotlib.pyplot as plt

from vertical import dz
from horizontal import dh
from total import dt
from tilt import tilt, hyperbolic_tilt

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

# first vertical derivatives
dz1 = dz(tf, xp, yp)
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

# second vertical derivative
dz2 = dz(tf, xp, yp, 2)
fig = plt.figure(figsize=(10, 10))
plt.title('Second Vertical Derivative')
plt.gca().set_aspect('equal', adjustable='box')
plt.contourf(yp/1000, xp/1000, dz2, 50, cmap=plt.cm.RdBu_r)
cb = plt.colorbar()
cb.set_label("nT/sq m", labelpad=30, rotation=0)
plt.xlabel('Easting Coordinate (km)')
plt.ylabel('Northing Coordinate (km)')
plot_edges(3)
fig.savefig('dz2.png')

# 1.5-order vertical derivative
dz1p5 = dz(tf, xp, yp, 1.5)
fig = plt.figure(figsize=(10, 10))
plt.title('1.5th-order Vertical Derivative')
plt.gca().set_aspect('equal', adjustable='box')
plt.contourf(yp/1000, xp/1000, dz1p5, 50, cmap=plt.cm.RdBu_r)
cb = plt.colorbar()
cb.set_label("nT/m^1.5", labelpad=30, rotation=0)
plt.xlabel('Easting Coordinate (km)')
plt.ylabel('Northing Coordinate (km)')
plot_edges(3)
fig.savefig('dz1p5.png')

# total horizontal derivative
thd = dh(tf, xp, yp)
fig = plt.figure(figsize=(10, 10))
plt.title('Total Horizontal Derivative')
plt.gca().set_aspect('equal', adjustable='box')
plt.contourf(yp/1000, xp/1000, thd, 50, cmap=plt.cm.RdBu_r)
cb = plt.colorbar()
cb.set_label("nT/m", labelpad=30, rotation=0)
plt.xlabel('Easting Coordinate (km)')
plt.ylabel('Northing Coordinate (km)')
plot_edges(3)
fig.savefig('thd.png')

# total derivative
td = dt(tf, xp, yp)
fig = plt.figure(figsize=(10, 10))
plt.title('Total Derivative')
plt.gca().set_aspect('equal', adjustable='box')
plt.contourf(yp/1000, xp/1000, td, 50, cmap=plt.cm.RdBu_r)
cb = plt.colorbar()
cb.set_label("nT/m", labelpad=30, rotation=0)
plt.xlabel('Easting Coordinate (km)')
plt.ylabel('Northing Coordinate (km)')
plot_edges(3)
fig.savefig('td.png')

# tilt angle
theta = tilt(tf, xp, yp)
fig = plt.figure(figsize=(10, 10))
plt.title('Tilt Angle')
plt.gca().set_aspect('equal', adjustable='box')
plt.contourf(yp/1000, xp/1000, theta, 50, cmap=plt.cm.RdBu_r)
cb = plt.colorbar()
cb.set_label("Radians", labelpad=30, rotation=0)
plt.xlabel('Easting Coordinate (km)')
plt.ylabel('Northing Coordinate (km)')
plot_edges(3)
fig.savefig('tilt.png')

# hyperbolic tilt angle
hta = hyperbolic_tilt(tf, xp, yp)
fig = plt.figure(figsize=(10, 10))
plt.title('Hyperbolic Tilt Angle')
plt.gca().set_aspect('equal', adjustable='box')
plt.contourf(yp/1000, xp/1000, hta, 50, cmap=plt.cm.RdBu_r)
cb = plt.colorbar()
cb.set_label("Radians", labelpad=30, rotation=0)
plt.xlabel('Easting Coordinate (km)')
plt.ylabel('Northing Coordinate (km)')
plot_edges(3)
fig.savefig('hta.png')
