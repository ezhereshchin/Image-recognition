from B_ratio import B_pixel_ratio,main
from PIL import Image

def Symbol_ratio_cal():
    f_name=["zero.jpg","one.jpg","two.jpg","three.jpg","four.jpg","five.jpg","six.jpg","seven.jpg","eight.jpg","nine.jpg"]
    result = open("results.txt","w") 
    for name in f_name: 
        vect=B_pixel_ratio(name)
        for v in range(len(vect)):
            if v!=len(vect)-1:              
                result.write(str(vect[v]) + ",")
            else:
                result.write(str(vect[v]) + "\n")
    result.close()

def read_file_vect(f_name):
    saved_result=open(f_name,"r")
    known=[]
    for line in saved_result:
        temp=(line.rstrip()).split(",")
        temp_l=[]
        for t in temp:
            temp_l.append(float(t))
        known.append(temp_l)

    saved_result.close()
    return known
#Symbol_ratio_cal()


def main():
    f_name=["new_zero.jpg","new_one.jpg","new_two.jpg","new_three.jpg","new_four.jpg","new_five.jpg","new_six.jpg","new_seven.jpg","new_eight.jpg","new_nine.jpg"]
    
    
    known=read_file_vect("results.txt")
    for name in f_name: 
        recognized_char_vect=recognize(name, known)
        print(name,recognized_char_vect,"test")
