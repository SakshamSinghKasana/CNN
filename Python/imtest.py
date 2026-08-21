import DSeg
import numpy as np

# inp = input()
# match inp:
#     case "R":
#         DSeg.Show_img(DSeg.load_D("R_data.json"), "R")
#     case "B":
#         DSeg.Show_img(DSeg.load_D("B_data.json"), "B")
#     case "G":
#         DSeg.Show_img(DSeg.load_D("G_data.json"), "G")
#     case "F":
#         DSeg.Show_img(DSeg.load_D("data.json"), "F")
#


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
fil = [fil0]#,fil1,fil2,fil3]

# DSeg.RGB_Seggrigation(DSeg.load_D("data.json"))
# temp_img=np.array(DSeg.load_D("E_data.json"))
# temp_img = temp_img.astype(float)
#
# for f in fil:
#     Red_AM = DSeg.filter_apply(DSeg.load_D("R_data.json"), f)
#     Green_AM = DSeg.filter_apply(DSeg.load_D("G_data.json"), f)
#     Blue_AM = DSeg.filter_apply(DSeg.load_D("B_data.json"), f)
#
#     Activation_M = DSeg.RGB_Conjugation(Red_AM, Green_AM, Blue_AM)
#     #temp_img += np.array(Activation_M)
# final_img = Activation_M #temp_img.tolist()
# DSeg.Show_img(final_img, 'F')
#
# def main():
#

# DSeg.Show_img(DSeg.pooling(DSeg.pooling(DSeg.filter_apply(DSeg.load_D("R_data.json"), fil0))),'R')
DSeg.show_img(DSeg.pooling(DSeg.filter_apply(DSeg.load_D("R_data.json"), fil0)),'R')
