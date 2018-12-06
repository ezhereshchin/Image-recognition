from PIL import Image

class pix():
    def __init__(self,x,y,reg ):
        self.x = x
        self.y = y
        self.region = reg
        return 

    def get_reg(self):
        return self.region

    def set_reg(self, reg):
        self.region = reg
        return
    
    def get_pos(self):
        return self.x , self.y

class region():
    def __init__(self, myid):
        self.myid = myid
        self.pixels = []
        self.top = 0
        self.bot = 0
        self.left = 0
        self.right = 0
        self.count = 0
        return

    def get_pixels(self):
        return self.pixels

    def get_limits(self):
        return self.top, self.bot, self.left, self.right 

    def add_pixel(self, pix):
        self.pixels.append(pix)
        x,y = pix.get_pos()
        self.top = min(y, self.top)
        self.bot = max(y, self.bot)
        self.left = min(x, self.left)
        self.right =max(x, self.right)
        self.count += 1
    
    def merge_regions(self, region):
        for i in region.get_pixels:
            i.set_reg(self)
        self.pixels.extend(region)
        t,b,l,r = region.get_limits()
        self.top = min(t, self.top)
        self.bot = max(b, self.bot)
        self.left = min(l, self.left)
        self.right =max(r, self.right)
        return
    
    def get_count(self):
        return self.count

def find_regions(image):
    pixels = image.load()
    width, height = image.size
    matrix = [[None for x in range(width)] for y in range(height)] 
    regions = []
    counter = 0
    for j in range(height):
        for i in range(width):
            matrix[i][j] = pix(i,j,None)
 
            if pixels[i,j][0] == 0:
                if i - 1 >= 0:
                    leftR = matrix[i-1][j].get_reg()
                    if j-1 >= 0:
                        topLR = matrix[i-1][j-1].get_reg()
                if j-1 >0:
                    topR = matrix[i][j-1].get_reg()
                if j-1 >0 and i+1< width:
                    topRR = matrix[i+1][j-1].get_reg()

                if leftR:
                    matrix[i][j].set_reg(leftR)
                    leftR.add_pixel(matrix[i][j])
                    if topRR and leftR is not topRR:
                        topRR.merge_regions(leftR)
                        regions.remove(leftR)
                        leftR=topRR
                    if topR and leftR is not topR:
                        topR.merge_regions(leftR)
                        regions.remove(leftR)
                        leftR=topR
                elif topRR:
                    matrix[i][j].set_reg(topRR)
                    topRR.add_pixel(matrix[i][j])
                    if topLR and topRR is not topLR:
                        topLR.merge_regions(topRR)
                        regions.remove(topRR)
                        topRR=topLR
                elif topR:
                    matrix[i][j].set_reg(topR)
                    topR.add_pixel(matrix[i][j])
                elif topLR:
                    matrix[i][j].set_reg(topLR)
                    topLR.add_pixel(matrix[i][j])
                else:
                    new_reg = region(counter)
                    regions.append(new_reg)
                    counter +=1
                    matrix[i][j].set_reg(new_reg)
                    new_reg.add_pixel(matrix[i][j])
    counts = []        
    for i in regions:
        counts.append(i.get_count())
    return counts, regions
