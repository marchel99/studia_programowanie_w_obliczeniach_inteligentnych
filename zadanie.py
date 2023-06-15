import random
import numpy as np
import math



def generate_points_on_surface(num_points, width, length, height=0):
    if height == 0:
        points = np.random.rand(num_points, 3) - 0.5
        points[:, 0] *= width
        points[:, 1] *= length
        points[:, 2] = 0
    else:
        points = np.random.rand(num_points, 3)
        points[:, 0] = (np.random.rand(num_points) - 0.5) * width
        points[:, 1] = (np.random.rand(num_points) - 0.5) * length
        points[:, 2] *= height
    return points.tolist()

def generate_points_on_cylinder(num_points, radius, height):
    thetas = np.random.rand(num_points) * 2 * math.pi
    zs = np.random.rand(num_points) * height
    xs = radius * np.cos(thetas)
    ys = radius * np.sin(thetas)
    points = np.vstack([xs, ys, zs]).T
    return points.tolist()

if __name__ == '__main__':
    points = generate_points_on_surface(10000, 10, 10)
    points2 = generate_points_on_surface(10000, 10, 0, 10)
    points3 = generate_points_on_cylinder(10000, 10, 10)
    with open('xyz.xyz', 'w', newline='') as csvfile:
        csvwriter = writer(csvfile)
        for point in points + points2 + points3:
            csvwriter.writerow(point)