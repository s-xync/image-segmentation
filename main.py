import cv2
from utils import pickRandomClusterCenters
from kmeans import kmeans
from utils import distanceBetweenPoints

NO_OF_KMEANS_ITERATIONS = 10
NO_OF_CLUSTERS = 3

def main():
    # without giving a flag, imread will take in only
    # RGB channels and will leave transperancy out
    inputImageMatrix = cv2.imread('input.jpg')
    clusterCenters = pickRandomClusterCenters(inputImageMatrix, NO_OF_CLUSTERS)
    kmeans(inputImageMatrix, NO_OF_KMEANS_ITERATIONS, NO_OF_CLUSTERS)
    print(distanceBetweenPoints([2,2,4],[1,2,3]))
    return



if __name__ == '__main__':
    main()
