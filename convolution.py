
#References
#http://machinelearninguru.com/computer_vision/basics/convolution/image_convolution_1.html

import numpy as np
import scipy
from skimage import io, color
from skimage import exposure
import matplotlib.pyplot as plt

from skimage import data, io

#apply convolution
original_image = io.imread('convolution_original_image.png')

#create different kernals
kernel_1 = np.array([[1/3,1/3,1/3],[0,0,0],[0,0,0]])

kernel_2 = np.array([[1/3,0,0],[1/3,0,0],[1/3,0,0]])

kernel_3 = np.array([[1/9,1/9,1/9],[1/9,1/9,1/9],[1/9,1/9,1/9]])

#apply kernal on image
apply_ker1  = scipy.signal.convolve2d(original_image, kernel_1, 'valid')
apply_ker2 = scipy.signal.convolve2d(apply_ker1, kernel_2, 'valid')
apply_ker3 = scipy.signal.convolve2d(original_image, kernel_3, 'valid')

#disply after 1st kernal applied
plt.imshow(apply_ker1, cmap=plt.cm.gray)
plt.axis('off')
plt.show()

#disply after 2nd kernal applied
plt.imshow(apply_ker2, cmap=plt.cm.gray)
plt.axis('off')
plt.show()

#disply after 3rd kernal applied
plt.imshow(apply_ker3, cmap=plt.cm.gray)
plt.axis('off')
plt.show()
















