from PIL import Image
import math
def B_pixel_ratio(f_name):
    im=Image.open(f_name)
    pixels = im.load()      
    zone_x= math.floor(im.size[0]/3)
    zone_y= math.floor(im.size[1]/3)
    inside_zx= math.floor(zone_x/3)
    inside_zy= math.floor(zone_y/3)
    
    check_x=0
    check_y=zone_y
    x=0
    y=0 
    vect=[]
   
    for  i in range(9): 
        if i==3 or i==6:
            check_x=zone_x
            y=check_y
            x=0
            check_y=check_y+zone_y
        elif i==8:
            check_y=im.size[1]
            check_x=im.size[0]
        else:
            x=check_x
            check_x = check_x+zone_x    
        c=0
        bp=0
        while x <check_x:
            temp_y=y
            while temp_y<check_y:
                c=c+1
                if (pixels[x,temp_y]!=(255,255,255)):#(0,0,0)):
                    bp=bp+1
                temp_y=temp_y+1
            x=x+1
        vect.append(bp/c)    
    im.close()
        
    return vect

def main():
    
    
    while True:
        f_name=(input("Enter the File name or enter Q to end program:"))       
        if (f_name!="Q"):
            vect=B_pixel_ratio(f_name)
            print(vect,"vector of ",f_name)
        else:
            break
    return
