'''
load_D -> to read data from a json file
write_D -> to write the inputrd data in the json file
RGB_Seggrigation -> to distribute the R, G, and B values in respective lists
RGB_Conjugation -> to combine all the R, G, and B lists into one lists
read_img -> used to read an image and get the list of the values
show_img -> to plot the image list using matplotlib
filter_apply -> used to apply the filter on a 2D list of the image
pooling -> used for the pooling step of the CNN
'''
import json
import numpy as np
import matplotlib.pyplot as plt

def load_D(img):
    with open(img) as f:
        d = json.load(f)
    return np.array(d)

def write_D(data_L,file):
    data = data_L.tolist()
    with open(file, "w") as f:
        json.dump(data, f, indent=4)

def RGB_Seggrigation(d):
    R = d[:, :, 0]
    G = d[:, :, 1]
    B = d[:, :, 2]

    write_D(R,"R_data.json")
    write_D(G,"G_data.json")
    write_D(B,"B_data.json")

    return R,G,B

def RGB_Conjugation(R,G,B):
    d = np.stack((R,G,B),axis=-1) #Combines all the arrays into one array ex: (200, 300, 3)
    return d

def read_img(image):
    image_array = plt.imread(image)
    return image_array

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

def filter_apply(D, fil):
    d = np.array(D, dtype=float)
    fil = np.array(fil, dtype=float)
    filt = fil.shape[0]

    H, W = d.shape
    out_h, out_w = H - filt + 1, W - filt + 1

    # Build output array
    activation_M = np.empty((out_h, out_w))

    # Vectorized inner product using broadcasting
    for i in range(out_h):
        for j in range(out_w):
            activation_M[i, j] = np.sum(d[i:i+filt, j:j+filt] * fil)

    return activation_M


def pooling(d, stride=2, filt=2):
    # Ensure dimensions are divisible by filt
    h, w = d.shape
    h_out, w_out = h // filt, w // filt

    # Reshape into blocks of size filt×filt
    d = d[:h_out*filt, :w_out*filt]  # crop if not divisible
    d = d.reshape(h_out, filt, w_out, filt)

    # Take mean over the small blocks
    activation_M = d.mean(axis=(1, 3))

    return activation_M
