import DSeg
import numpy as np
fil0 = [
        [1,0,-1],
        [1,0,-1],
        [1,0,-1]
        ]
fil1 = [
        [1,1,0],
        [1,0,-1],
        [0,-1,-1]
        ]
fil2 = [
        [1,1,1],
        [0,0,0],
        [-1,-1,-1]
        ]
fil3 = [
        [0,1,1],
        [-1,0,1],
        [-1,-1,0]
        ]
fil = [fil1,fil2,fil3]

def main():
    image_list = DSeg.read_img("images.jpg")
    list_R, list_G, list_B = DSeg.RGB_Seggrigation(image_list)

    # Run the first filter
    temp = DSeg.filter_apply(list_R, fil[0])
    Flist_R = np.zeros_like(temp, dtype=float)   # <-- use here

    # Accumulate over all filters
    for i in fil:
        temp = DSeg.filter_apply(list_R, i)
        Flist_R += temp

    Flist_R = Flist_R / len(fil)   # average over filters
    DSeg.show_img(DSeg.pooling(Flist_R), 'R')
main()
