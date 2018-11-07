import numpy as np
from utils import distanceBetweenPoints, saveOutputImage
import cv2

def kmeans(imageMatrix, clusterCenters, noIterations):
    noClusters = len(clusterCenters)
    height = imageMatrix.shape[0]
    width = imageMatrix.shape[1]
    for i in range(noIterations):
        clusterMatrix = calculateclusterMatrix(imageMatrix, clusterCenters, noClusters, height, width)
        clusterCenters = calculateClusterCenters(imageMatrix, clusterMatrix, noClusters, height, width)
        print("{0} iteration".format((i+1)))#debug
        saveOutputImage(clusterMatrix, clusterCenters, "output{0}.jpg".format((i+1))) #debug
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
    for i in range(noClusters):
        clusterCenters[i] /= noPixelsPerCluster[i]
    return clusterCenters
