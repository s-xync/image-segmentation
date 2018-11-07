import cv2
import numpy as np
from random import randint

def pickRandomClusterCenters(imageMatrix, noClusters):
    height = imageMatrix.shape[0]
    width = imageMatrix.shape[1]
    clusterCenters = []
    for i in range(noClusters):
        randomHeight = randint(0, height)
        randomWidth = randint(0, width)
        clusterCenters.append(imageMatrix[randomHeight][randomWidth])
    return clusterCenters

def distanceBetweenPoints(point1, point2):
    # each point RGB channels and so, three dimensions
    return round(((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2 + (point2[2] - point1[2]) ** 2) ** 0.5, 2)

def getInputImageMatrix(imageName):
    # without giving a flag, imread will take in only
    # RGB channels and will leave transperancy out
    imageMatrix = cv2.imread(imageName)
    return imageMatrix.astype(float)

def saveOutputImage(clusterMatrix, clusterCenters, imageName):
    height = clusterMatrix.shape[0]
    width = clusterMatrix.shape[1]
    outputImageMatrix = np.full((height, width, 3), 0)
    for i in range(height):
        for j in range(width):
            outputImageMatrix[i][j] = clusterCenters[clusterMatrix[i][j]]
    outputImageMatrix = outputImageMatrix.astype(np.uint8)
    cv2.imwrite(imageName, outputImageMatrix)
    return
