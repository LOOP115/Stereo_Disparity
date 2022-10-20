import cv2
import numpy as np
np.set_printoptions(threshold=1000)
groundTruth = cv2.imread('./resources/Dataset/2018-07-09-16-11-56_2018-07-09-16-11-56-702-disparity.png')
print(groundTruth[300])