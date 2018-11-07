import numpy as np
from utils import distanceBetweenPoints
import cv2

def kmeans(imageMatrix, clusterCenters, noIterations):
    noClusters = len(clusterCenters)
    clusterMatrix = calculateclusterMatrix(imageMatrix, clusterCenters, noClusters)
    return clusterMatrix, clusterCenters

def calculateclusterMatrix(imageMatrix, clusterCenters, noClusters):
    height = imageMatrix.shape[0]
    width = imageMatrix.shape[1]
    clusterMatrix = np.full((height, width), -1)
    for i in range(height):
        for j in range(width):
            tempDistances = []
            for k in range(noClusters):
                tempDistances.append(distanceBetweenPoints(imageMatrix[i][j], clusterCenters[k]))
            clusterMatrix[i][j] = tempDistances.index(min(tempDistances))
    return clusterMatrix
