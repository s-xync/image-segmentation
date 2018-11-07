import cv2
from kmeans import kmeans

NO_OF_KMEANS_ITERATIONS = 10
NO_OF_CLUSTERS = 3

def main():
    # without giving a flag, imread will take in only
    # RGB channels and will leave transperancy out
    input_image = cv2.imread('input.jpg')
    kmeans(input_image, NO_OF_KMEANS_ITERATIONS, NO_OF_CLUSTERS)
    return



if __name__ == '__main__':
    main()
