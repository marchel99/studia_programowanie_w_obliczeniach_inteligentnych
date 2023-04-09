import numpy as np
import csv

def fit_plane_ransac(points, num_iterations=50, threshold_distance=0.1, inlier_ratio=0.8):
    n_points = points.shape[0]
    best_inliers = None
    best_model = None
    for n in range(num_iterations):
        # randomly select three points from the point cloud
        sample_indices = np.random.choice(n_points, 3, replace=False)
        sample = points[sample_indices]
        # calculate the normal vector of the plane
        normal = np.cross(sample[1] - sample[0], sample[2] - sample[0])
        normal /= np.linalg.norm(normal)
        # calculate the distance of all points from the plane
        distances = np.abs((points - sample[0]).dot(normal))
        # determine the inliers and outliers based on the threshold distance
        inliers = points[distances < threshold_distance]
        outliers = points[distances >= threshold_distance]
        # if the number of inliers is greater than the inlier ratio, update the best model
        if inliers.shape[0] > inlier_ratio * n_points and (best_inliers is None or inliers.shape[0] > best_inliers.shape[0]):
            best_inliers = inliers
            # calculate the normal vector of the plane based on all inliers
            best_normal = np.cross(best_inliers[1] - best_inliers[0], best_inliers[2] - best_inliers[0])
            best_normal /= np.linalg.norm(best_normal)
            best_model = (best_normal, np.mean(best_inliers, axis=0))
    return best_model

# read the xyz file and store the points as a numpy array
points = []
with open('xyz.txt', 'r') as file:
    reader = csv.reader(file, delimiter=' ')
    for row in reader:
        points.append([float(row[0]), float(row[1]), float(row[2])])
points = np.array(points)

# find three disjoint point clouds using k-means clustering
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=3, random_state=0).fit(points)
labels = kmeans.labels_

# fit a plane to each point cloud using RANSAC and determine if it is horizontal, vertical or neither
for i in range(3):
    cloud = points[labels == i]
    model = fit_plane_ransac(cloud)
    normal = model[0]
    mean_distance = np.abs((cloud - model[1]).dot(normal)).mean()
    if mean_distance < 0.05:
        if np.abs(normal[2]) > 0.9:
            print('Cloud', i+1, 'represents a horizontal plane')
        elif np.abs(normal[0]) > 0.9:
            print('Cloud', i+1, 'represents a vertical plane')
        else:
            print('Cloud', i+1, 'does not represent a horizontal or vertical plane')
    else:
        print('Cloud', i+1, 'does not represent a plane')