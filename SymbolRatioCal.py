from B_ratio import B_pixel_ratio,main
from PIL import Image

def Symbol_ratio_cal():
    f_name=["zero.jpg","one.jpg","two.jpg","three.jpg","four.jpg","five.jpg","six.jpg","seven.jpg","eight.jpg","nine.jpg"]
    result = open("results.txt","w")  
    for name in f_name: 
        vect=B_pixel_ratio(name)
        result.write("\n")
        for v in vect:
            if v!=vect[len(vect)-1]:
                temp=str(v)+","
                result.write(temp)
            else:
                temp=str(v)
                result.write(temp)
    result.close()
    
Symbol_ratio_cal()
