'''
load_D -> to read data from a json file
write_D -> to write the inputrd data in the json file
RGB_Seggrigation -> to distribute the R, G, and B values in respective lists
RGB_Conjugation -> to combine all the R, G, and B lists into one lists
read_img -> used to read an image and get the list of the values
show_img -> to plot the image list using matplotlib
cal_M -> used to calculate the filter and the underlying matrices and return a value
filter_apply -> used to apply the filter on a 2D list of the image
pooling -> used for the pooling step of the CNN
'''
import json
import numpy as np
import matplotlib.pyplot as plt

def load_D(img):
    with open(img) as f:
        d = json.load(f)
    return d

def write_D(data,file):
    with open(file, "w") as f:
        json.dump(data, f, indent=4)

def RGB_Seggrigation(d):
    R, G, B, E = [], [], [], []

    # Assuming d is shaped like: [ [ [R,G,B], [R,G,B], ... ] ]
    for row in d:              # iterate over rows
        r_row, g_row, b_row, e_row = [], [], [], []
        for pixel in row:         # each pixel is [R,G,B]
            r_row.append(pixel[0])
            g_row.append(pixel[1])
            b_row.append(pixel[2])
            e_row.append(0)
        R.append(r_row)
        G.append(g_row)
        B.append(b_row)
        E.append(e_row)

    write_D(R,"R_data.json")
    write_D(G,"G_data.json")
    write_D(B,"B_data.json")
    write_D(E,"E_data.json")

    return R,G,B

def RGB_Conjugation(R,G,B):
    d = []
    # Assuming d is shaped like: [ [ [R,G,B], [R,G,B], ... ] ]
    for row in range(len(R)):              # iterate over rows
        pix = []
        r = []
        for pixel in range(len(R[row])):         # each pixel is [R,G,B]
            pix.append(R[row][pixel])
            pix.append(G[row][pixel])
            pix.append(B[row][pixel])
            r.append(pix)
            pix = []
        d.append(r)

    return d

def read_img(image):
    image_array = plt.imread(image)
    return image_array.tolist()

def show_img(data,color):
    match color:
        case "R":
            plt.imshow(data,cmap='Reds')
            plt.show()
        
        case "G":
            plt.imshow(data,cmap='Greens')
            plt.show()

        case "B":
            plt.imshow(data,cmap='Blues')
            plt.show()

        case "F":
            plt.imshow(data)
            plt.show()

def cal_M(sm, fil, r):
    sm1 = sm.tolist()
    sum = 0
    for i in range(r):
        for j in range(r):
            m = sm1[i][j]*fil[i][j]
            sum+=m 
    return sum

def filter_apply(D, fil):

    d = np.array(D)
    
    activation_M = []
    stride = 1
    filt = 3
    Yl = 0
    for a in range(filt,len(d)+1):
        Xl=0
        row = []
        for b in range(filt,len(d)+1):
            sm = d[Yl:a, Xl:b] #The matrix that is scanned by the filter

            #____________Write the filter calculation here_____________
            row.append(cal_M(sm,fil, filt))

            Xl+=stride
        Yl+=stride
        activation_M.append(row)
    
    return activation_M

def pooling(D):
    d = np.array(D)
    
    activation_M = []
    stride = 2
    filt = 2
    Yl = 0
    for a in range(filt,len(d)+1,2):
        Xl=0
        row = []
        for b in range(filt,len(d)+1,2):
            sm = d[Yl:a, Xl:b] #The matrix that is scanned by the filter

            #____________Write the filter calculation here_____________
            row.append(Pool_F(sm))

            Xl+=stride
        Yl+=stride
        activation_M.append(row)
    
    return activation_M

def Pool_F(sm):
    sum = 0
    dem = 0
    for i in sm:
        for j in i:
            sum+=j
            dem+=1
    return sum/dem


