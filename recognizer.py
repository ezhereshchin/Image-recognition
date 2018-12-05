from b_ratio import B_pixel_ratio
import math

def  get_distance(a, b):
    la = len(a)
    assert la == len(b)
    total = 0
    for i in range(la):
        total += (a[i]-b[i])**2
    return math.sqrt(total)

def recognize(f_name, known):
    test = B_pixel_ratio(f_name)
    distances=[]
    for i in known:
        distances.append([get_distance(test,i),i])
    distances.sort()
    print(distances[0][1])
