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
def test_recognize():
    saved_result=open("results.txt","r")
    known=[]
    for line in saved_result:
        temp=(line.rstrip()).split(",")
        print(temp)
        temp_l=[]
        for t in temp:
            temp_l.append(float(t))
        known.append(temp_l)

    print(known,"wegweg")
    f_name= "new_zero.jpg"
    saved_result.close()
    recognize(f_name, known)
