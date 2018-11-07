from time import time

from utils import pickRandomClusterCenters, getInputImageMatrix, saveOutputImage
from kmeans import kmeans

NAME_OF_INPUT_IMAGE = 'input.jpg'
NAME_OF_OUTPUT_IMAGE = 'output.jpg'
NO_OF_KMEANS_ITERATIONS = 10
NO_OF_CLUSTERS = 3

def main():
    start = time()
    inputImageMatrix = getInputImageMatrix(NAME_OF_INPUT_IMAGE)
    clusterCenters = pickRandomClusterCenters(inputImageMatrix, NO_OF_CLUSTERS)
    assert len(clusterCenters) == NO_OF_CLUSTERS, "No. of cluster centers has to be equal"
    clusterMatrix, clusterCenters = kmeans(inputImageMatrix, clusterCenters, NO_OF_KMEANS_ITERATIONS)
    print(clusterCenters)
    saveOutputImage(clusterMatrix, clusterCenters, NAME_OF_OUTPUT_IMAGE)
    end = time()
    print("Time taken is {0}s".format((end - start)))
    return

if __name__ == '__main__':
    main()
