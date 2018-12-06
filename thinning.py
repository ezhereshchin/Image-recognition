#references
#http://scikit-image.org/docs/dev/auto_examples/edges/plot_skeleton.html

from skimage.morphology import skeletonize
from skimage import data
import matplotlib.pyplot as plt
from skimage.util import invert
from skimage import data, io

#----------------------------

from skimage.color import rgb2gray
from skimage import data, io
from matplotlib import pyplot as plt
from skimage import novice
import numpy as np
from skimage.io import imsave, imread
import scipy
import os

from skimage import measure
from skimage import filters

#read image
image_ori = io.imread('Numbers.bmp')	

#convert image into greyscale
image = invert(rgb2gray(image_ori))

#perform skeletonization
skeleton = skeletonize(image)

# display results
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(8, 4),
                         sharex=True, sharey=True)
						 				 
ax = axes.ravel()

ax[0].imshow(image, cmap=plt.cm.gray)
ax[0].axis('off')
ax[0].set_title('original', fontsize=20)

ax[1].imshow(skeleton, cmap=plt.cm.gray)
ax[1].axis('off')
ax[1].set_title('skeleton', fontsize=20)

fig.tight_layout()
plt.show()
