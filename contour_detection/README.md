# Contour Detection package
This is the package for contour detection.

## Using
The contour detection is used as follows :
1. Compile with make
2. run : ./contourDetection img (threshold) (-d)
    - img is the valid image input
    - threshold an optional argument for the lower threshold to use by the Canny algorithm, it must be an integer in between 0 and 100
    - -d is the option to use dilatation or not (NOTE : IT WAS USED ALL THE TIME IN THE PREVIOUS VERSION).


## Steps of contour detection
 
1. Apply a gaussian blur of size 5*5 on the image in input, with a sigma defined in the .h
 
2. Use openCV Canny algorithm to detect contours (@see http://docs.opencv.org/2.4/doc/tutorials/imgproc/imgtrans/canny_detector/canny_detector.html)
 
3. Apply a dilatation on the result image (@see http://docs.opencv.org/2.4/doc/tutorials/imgproc/erosion_dilatation/erosion_dilatation.html) to get thicker edges
 
4. Call openCV findContours function (@see http://docs.opencv.org/2.4/modules/imgproc/doc/structural_analysis_and_shape_descriptors.html?highlight=findcontours#findcontours)
 
Contours is a vector of vector of points. It is the data structure that contains the list of contours.

Hierarchy is a vector of vectors of 4 integers each.
 	hierarchy[i][0] is the next contour in the same hierarchy level of i
 	hierarchy[i][1] is the previous contour in the same hierarchy level of i
 	hierarchy[i][2] is the first child contour of i
 	hierarchy[i][3] is the parent contour of i

The contours are finally printed on the standard output as a list of points separated by the character '#', one contour per line.


