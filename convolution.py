from skimage import data, io
import scipy
import numpy as np

#apply convolution
img = io.imread('Lenna_blackandwhite.png')    # Load the image

kernel_1 = np.array([[1/3,0,0],[1/3,0,0],[1/3,0,0]])

kernel_2 = np.array([[1/3,1/3,1/3],[0,0,0],[0,0,0]])

image_sharpen = scipy.signal.convolve2d(img, kernel_1, 'same')
