import cv2
import numpy as np

def distanceBetweenPoints(point1, point2, squared):
    # each point RGB channels and so, three dimensions
    if squared:
        return round(((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2 + (point2[2] - point1[2]) ** 2), 2)
    elif not squared:
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
