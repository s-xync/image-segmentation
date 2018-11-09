from time import time
from utils import getInputImageMatrix, saveOutputImage
from clustering import kmeansClustering

NAME_OF_INPUT_IMAGE = 'input1.jpg'
NAME_OF_OUTPUT_IMAGE = 'output.jpg'
NO_OF_KMEANS_ITERATIONS = 10
NO_OF_CLUSTERS = 3
# CLUSTERING_TYPE --> SUBTRACTIVE, RANDOM, FARTHEST
CLUSTERING_TYPE = "FARTHEST"

def main():
    start = time()
    inputImageMatrix = getInputImageMatrix(NAME_OF_INPUT_IMAGE)
    clusterMatrix, clusterCenters = kmeansClustering(inputImageMatrix, NO_OF_CLUSTERS, NO_OF_KMEANS_ITERATIONS, CLUSTERING_TYPE)
    saveOutputImage(clusterMatrix, clusterCenters, NAME_OF_OUTPUT_IMAGE)
    end = time()
    print("Time taken is {0}s".format((end - start)))
    return

if __name__ == '__main__':
    main()
