import numpy as np
from math import exp
from utils import distanceBetweenPoints, saveOutputImage
from random import randint
import cv2

def kmeans(imageMatrix, clusterCenters, noIterations, height, width):
    noClusters = len(clusterCenters)
    for i in range(noIterations):
        print("{0} iteration".format((i+1))) #debug
        clusterMatrix = calculateclusterMatrix(imageMatrix, clusterCenters, noClusters, height, width)
        saveOutputImage(clusterMatrix, clusterCenters, "output{0}.jpg".format((i+1))) #debug
        clusterCenters = calculateClusterCenters(imageMatrix, clusterMatrix, noClusters, height, width)
    return clusterMatrix, clusterCenters

def calculateclusterMatrix(imageMatrix, clusterCenters, noClusters, height, width):
    clusterMatrix = np.full((height, width), -1)
    for i in range(height):
        for j in range(width):
            tempDistances = []
            for k in range(noClusters):
                tempDistances.append(distanceBetweenPoints(imageMatrix[i][j], clusterCenters[k], True))
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

def pickRandomClusterCenters(imageMatrix, noClusters, height, width):
    clusterCenters = []
    for i in range(noClusters):
        randomHeight = randint(0, height)
        randomWidth = randint(0, width)
        clusterCenters.append(imageMatrix[randomHeight][randomWidth])
    return clusterCenters

def pickSubtractiveClusterCenters(imageMatrix, noClusters, height, width):
    clusterCentersPositions = []
    potentialMatrix = np.full((height, width), 0.)
    for i in range(height):
        for j in range(width):
            for k in range(height):
                for l in range(width):
                    potentialMatrix[i][j] += exp(-1 * 4 * distanceBetweenPoints(imageMatrix[i][j], imageMatrix[k][l], True) / (15 ** 2))
    for k in range(noClusters):
        maxPotentialHeight, maxPotentialWidth = np.unravel_index(potentialMatrix.argmax(), potentialMatrix.shape)
        maxPotential = potentialMatrix[maxPotentialHeight][maxPotentialWidth]
        clusterCentersPositions.append([maxPotentialHeight, maxPotentialWidth])
        potentialMatrix[maxPotentialHeight][maxPotentialWidth] = 0.
        for i in range(height):
            for j in range(width):
                if not [i, j] in clusterCentersPositions:
                    potentialMatrix[i][j] -= maxPotential * exp(-1 * 4 * distanceBetweenPoints(imageMatrix[i][j], imageMatrix[maxPotentialHeight][maxPotentialWidth], True) / (21 ** 2))
    clusterCenters = []
    for i in range(len(clusterCentersPositions)):
        clusterCenters.append(imageMatrix[clusterCentersPositions[i][0]][clusterCentersPositions[i][1]])
    return clusterCenters

def pickFarthestClusterCenters(imageMatrix, noClusters, height, width):
	clusterCenters = []
	distanceMatrix = np.full((height, width), 0.)
	randomHeight = randint(0, height)
	randomWidth = randint(0, width)
	clusterCenters.append(imageMatrix[randomHeight][randomWidth])
	for i in range(height):
		for j in range(width):
			distanceMatrix[i][j] = distanceBetweenPoints(imageMatrix[i][j], imageMatrix[randomHeight][randomWidth], True)
	for k in range(noClusters-1):
		maxDistanceHeight, maxDistanceWidth = np.unravel_index(distanceMatrix.argmax(), distanceMatrix.shape)
		clusterCenters.append(imageMatrix[maxDistanceHeight][maxDistanceWidth])
		for i in range(height):
			for j in range(width):
				distanceMatrix[i][j] = min(distanceMatrix[i,j] , distanceBetweenPoints(imageMatrix[i][j], imageMatrix[maxDistanceHeight][maxDistanceWidth], True))
	return clusterCenters

def kmeansClustering(imageMatrix, noClusters, noIterations, clusteringType):
    height = imageMatrix.shape[0]
    width = imageMatrix.shape[1]
    if clusteringType == "SUBTRACTIVE":
        clusterCenters = pickSubtractiveClusterCenters(imageMatrix, noClusters, height, width)
    elif clusteringType == "RANDOM":
        clusterCenters = pickRandomClusterCenters(imageMatrix, noClusters, height, width)
    elif clusteringType == "FARTHEST":
        clusterCenters = pickFarthestClusterCenters(imageMatrix, noClusters, height, width)
    clusterMatrix, clusterCenters = kmeans(imageMatrix, clusterCenters, noIterations, height, width)
    return clusterMatrix, clusterCenters
