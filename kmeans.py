import numpy as np
from utils import distanceBetweenPoints
import cv2

def kmeans(imageMatrix, clusterCenters, noIterations):
    noClusters = len(clusterCenters)
    height = imageMatrix.shape[0]
    width = imageMatrix.shape[1]
    print(clusterCenters)#debug
    for i in range(noIterations):
        print("\n{0} iteration".format(i))
        clusterMatrix = calculateclusterMatrix(imageMatrix, clusterCenters, noClusters, height, width)
        clusterCenters = calculateClusterCenters(imageMatrix, clusterMatrix, noClusters, height, width)
        print(clusterCenters)#debug
    return clusterMatrix, clusterCenters

def calculateclusterMatrix(imageMatrix, clusterCenters, noClusters, height, width):
    clusterMatrix = np.full((height, width), -1)
    for i in range(height):
        for j in range(width):
            tempDistances = []
            for k in range(noClusters):
                tempDistances.append(distanceBetweenPoints(imageMatrix[i][j], clusterCenters[k]))
            clusterMatrix[i][j] = tempDistances.index(min(tempDistances))
    return clusterMatrix

def calculateClusterCenters(imageMatrix, clusterMatrix, noClusters, height, width):
    clusterCenters = []
    noPixelsPerCluster = []
    for i in range(noClusters):
        clusterCenters.append(np.array([0., 0., 0.]))
        noPixelsPerCluster.append(0)
    for i in range(height):
        for j in range(width):
            clusterCenters[clusterMatrix[i][j]] += imageMatrix[i][j]
            noPixelsPerCluster[clusterMatrix[i][j]] += 1
    print(noPixelsPerCluster) #debug
    for i in range(noClusters):
        clusterCenters[i] /= noPixelsPerCluster[i]
    return clusterCenters
