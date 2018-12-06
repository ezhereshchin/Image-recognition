# import math
from PIL import Image

# def get_chunk(pixelsO,x,y,chunkX,chunkY,oldsizeX,oldsizeY):
#     total=0
#     for i in range (chunkX):
#         for j in range (chunkY):
#             if x*chunkX+i<oldsizeX and y*chunkY+j<oldsizeY:
#                 total+=pixelsO[x*chunkX+i,y*chunkY+j][0]

#     average = round(total/(chunkX*chunkY))
#     average = (average, average, average)
#     return average

# def scale_image(pixelsO,pixelsE,oldsizeX,oldsizeY,newsizeX,newsizeY):
#     chunkX=math.floor(oldsizeX/newsizeX)

#     chunkY=math.floor(oldsizeY/newsizeY)
#     #go through original image chunk by chunk
#     for i in range(newsizeX):
#         for j in range(newsizeY):
#             #calculate average value of the chunk
#             print(pixelsO,i,j,chunkX+min(i,oldsizeX%newsizeX),chunkY+min(j,oldsizeY%newsizeY),oldsizeX,oldsizeY,"pixelsO,i,j,chunkX+min(i,oldsizeX%newsizeX),chunkY+min(j,oldsizeY%newsizeY),oldsizeX,oldsizeY")
#             pixelsE[i,j]=get_chunk(pixelsO,i,j,chunkX+min(i,oldsizeX%newsizeX),chunkY+min(j,oldsizeY%newsizeY),oldsizeX,oldsizeY)


#     print('converted')
#     return

def scale_image(image, newsize):
    newimage = image.resize(newsize)
    print('scaled')
    return newimage
