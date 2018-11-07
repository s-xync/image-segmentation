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
    return ((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2 + (point2[2] - point1[2]) ** 2) ** 0.5
