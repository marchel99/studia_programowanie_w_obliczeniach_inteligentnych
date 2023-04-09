import random
from _csv import writer
import numpy as np
import math

def generate_points_on_surface(num_points, width, length):
    points = []
    for i in range(num_points):
        x = random.uniform(-width / 2, width / 2)  
        y = random.uniform(-length / 2, length / 2) 
        z = 0  
        points.append([x, y, z])
    return points

def generate_points_on_surface2(num_points, width, length, height):
    points = []
    for i in range(num_points):
        x = random.uniform(-width / 2, width / 2)  
        y = random.uniform(-length / 2, length / 2)  
        z = random.uniform(0, height)  
        points.append([x, y, z])
    return points

def generate_points_on_cylinder(num_points, radius, height):
    points = []
    for i in range(num_points):
        theta = random.uniform(0, 2 * math.pi)  
        z = random.uniform(0, height)  
        x = radius * math.cos(theta)  
        y = radius * math.sin(theta)  
        points.append([x, y, z])
    return points

if __name__ == '__main__':
    points=generate_points_on_surface(10000,10,10)
    points2=generate_points_on_surface2(10000, 10, 0, 10)
    points3=generate_points_on_cylinder(10000, 10, 10)
    with open('xyz.xyz', 'w', newline='') as csvfile:
        csvwriter = writer(csvfile)
        for point in points:
            csvwriter.writerow(point)
        for point in points2:
            csvwriter.writerow(point)
        for point in points3:
            csvwriter.writerow(point)
