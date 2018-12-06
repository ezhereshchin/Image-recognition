from B_ratio import B_pixel_ratio,main
from PIL import Image
def Symbol_ratio_cal_for_zero():
    f_name="zero.png"
    result =[]
    vect=B_pixel_ratio(f_name)
    for v in vect:
        result.append(v)
    print(result)
def Symbol_ratio_cal():
    f_name=["zero.png","one.png","two.png","three.png","four.png","five.png","six.png","seven.png","eight.png","nine.png"]
    result = open("results.csv","w") 
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


def test_recognize():
    f_name=["new_zero.png","new_one.png","new_two.png","new_three.png","new_four.png","new_five.png","new_six.png","new_seven.png","new_eight.png","new_nine.png"]
    
    
    known=read_file_vect("results.csv")
    for name in f_name: 
        recognized_char_vect=recognize(name, known)
        print(name,recognized_char_vect)

#Symbol_ratio_cal_for_zero()
#Symbol_ratio_cal()
#test_recognize()
