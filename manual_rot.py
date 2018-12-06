from PIL import Image
import math
def rotate(pixelsO, pixelsE, width, height, theta):
    center_x = math.floor(width/2)
    center_y = math.floor(height/2)
    max_size = round(math.sqrt((width-center_x)**2+(height-center_y)**2))+1
    new_center_x = max_size
    new_center_y = max_size
    
    for i in range(width-1):
        for j in range(height-1):
            new_i = round(math.cos(theta) * (i - center_x) - math.sin(theta) * (j - center_y) + new_center_x)
            
            new_j = round(math.sin(theta) * (i - center_x) + math.cos(theta) * (j - center_y)+ new_center_y)
            pixelsE[new_i,new_j] = pixelsO[i,j]
    print('rotated')
    
    #get rid of black dots in image
    for i in range (max_size):
        for j in range (max_size):
            mypix = pixelsE[i,j]
            if mypix[0]==0:
                count = 0
                colour = 0
                for k in [1,-1]:
                    if 0 <= i+k <= max_size-1 and 0 <= j+k <= max_size-1:
                        pixel1 = pixelsE[i+k,j]
                        pixel2 = pixelsE[i,j+k]
                        if pixel1[0] !=0:
                            count += 1
                            colour += pixel1[0]
                        if pixel2 != 0:
                            count += 1
                            colour += pixel1[0]
                if count>=2:
                    colour = math.floor(colour/count)
                    mypix = (colour, colour, colour)
    print('de-dotted')

    return
