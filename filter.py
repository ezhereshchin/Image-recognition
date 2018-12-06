from fractions import Fraction


def getFilter():
    #Enter 3x3 operator
    row1 = input("").split(" ")
    row_int1 = []
    for i in row1:
        row_int1.append(float(Fraction(i)))
    row2 = input("").split(" ")
    row_int2 = []
    for i in row2:
        row_int2.append(float(Fraction(i)))
    row3 = input("").split(" ")
    row_int3 = []
    for i in row3:
        row_int3.append(float(Fraction(i)))
    return row_int1 + row_int2 + row_int3


def applyFilter(pixel, filterArray, i, j, width, height):
    x = i - 1
    y = j - 1
    xflag = False
    yflag = False
    if x < 0:
        x = 0
    elif x + 2 == width:
        xflag = True
    if y < 0:
        y = 0
    elif y + 2 == height:
        yflag = True

    newPixel = 0
    newPixel += pixel[x, y][0] * filterArray[0]
    newPixel += pixel[x + 1, y][0] * filterArray[1]
    if xflag:
        newPixel += pixel[x + 1, y][0] * filterArray[2]
    else:
        newPixel += pixel[x + 2, y][0] * filterArray[2]
    newPixel += pixel[x, y + 1][0] * filterArray[3]
    newPixel += pixel[x + 1, y + 1][0] * filterArray[4]
    if xflag:
        newPixel += pixel[x + 1, y + 1][0] * filterArray[5]
    else:
        newPixel += pixel[x + 2, y + 1][0] * filterArray[5]
    if yflag:
        newPixel += pixel[x, y + 1][0] * filterArray[6]
        newPixel += pixel[x + 1, y + 1][0] * filterArray[7]
        if xflag:
            newPixel += pixel[x + 1, y + 1][0] * filterArray[8]
        else:
            newPixel += pixel[x + 2, y + 1][0] * filterArray[8]
    else:
        newPixel += pixel[x, y + 2][0] * filterArray[6]
        newPixel += pixel[x + 1, y + 2][0] * filterArray[7]
        if xflag:
            newPixel += pixel[x + 1, y + 2][0] * filterArray[8]
        else:
            newPixel += pixel[x + 2, y + 2][0] * filterArray[8]
            newPixel = int(round(newPixel))
    newPixel = (newPixel, newPixel, newPixel)
    return newPixel


def filter_pixels(orig, pixelsO, pixelsE):
    filterArray = getFilter()
    width, height = orig.size
    #width = int(round(width))
    #height = int(round(height))


    for i in range(width-1):
        for j in range(height-1):
          pixelsE[i, j] = applyFilter(pixelsO, filterArray, i, j, width, height)
