# Image Segmentation
This source code in this repository is used to segment images using K-Means Clustering.  
There are three ways in which we are handling the picking of initial clusters.  

* Random Cluster Centers  
* K-means++  
* Subtractive Clustering  

Subtractive Clustering is very computationally intensive and is only suitable for very small images.  

K-means++ seems to be working the best as it finds the most probable clusters directly and K-means is used for further fine tuning.  

Random also works good but it needs more iterations. Sometimes, some clusters may not be found because of random initialization.

### SETUP
This source code uses the *opencv-python* library. To install, run the following command.  
`pip3 install opencv-python`  
You would need *python3* and *pip3* to run the above command and *python3* is used as the main programming language in the source code. *numpy* is downloaded automatically using the above command which is also used in our source code.  

### DESCRIPTION
To run the source code, first open *main.py* and edit the following options.  

* NAME_OF_INPUT_IMAGE = 'input1.jpg'  
* NAME_OF_OUTPUT_IMAGE = 'output.jpg'  
* NO_OF_KMEANS_ITERATIONS = 10  
* NO_OF_CLUSTERS = 3  
* CLUSTERING_TYPE = "FARTHEST"  

The last option `CLUSTERING_TYPE` lets you choose the initialization algorithm which have been mentioned in the start.  
After setting the above options, you can run the program using...  
`python3 main.py`  
And you would be able to see all the intermediate images and also the final image.  

The whole source code is distributed among `main.py`, `clustering.py`, `utils.py`.  

In `main.py`, we have the driver program.  

In `utils.py`, we have the most commonly used utility functions like `distanceBetweenPoints`, `getInputImageMatrix`, `saveOutputImage`.  
`distanceBetweenPoints` calculates the distance between two points in color space.  
`getInputImageMatrix` returns a image matrix for a given input image using *opencv*.  
`saveOutputImage` saves a image to the drive using the given image matrix which also uses *opencv*.  

In `clustering.py`, we have the important functions like `kmeans`, `calculateclusterMatrix`, `calculateClusterCenters`, `pickRandomClusterCenters`, `pickSubtractiveClusterCenters`, `pickFarthestClusterCenters`,
`kmeansClustering`.  
The above functions have been descriptively named so as to aid the understanding.  

Project by [SaiKumar Immadi](https://github.com/s-xync), [Rahul Korthiwada](https://github.com/Korthiwada), [Shoaib Ahmed](https://github.com/ahmedshoaib)  
Thanks!!
