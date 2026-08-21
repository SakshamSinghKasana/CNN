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


def process_channel(channel_data, filters):
    """Apply filters and pooling to a single channel"""
    # Run the first filter
    temp = DSeg.filter_apply(channel_data, filters[0])
    filtered = np.zeros_like(temp, dtype=float)

    # Accumulate over all filters
    for f in filters:
        temp = DSeg.filter_apply(channel_data, f)
        filtered += temp

    filtered = filtered / len(filters)   # average over filters
    
    # Apply ReLU to remove negative values (only keep positive edge responses)
    filtered = np.maximum(filtered, 0)
    
    # Normalize to [0, 255] range
    if filtered.max() >= 255:
        filtered = (filtered/filtered.max()) * 255
    
    return np.uint8(filtered) #DSeg.pooling(np.uint8(filtered))

def main():
    fil = [fil0, fil1, fil2, fil3]
    image_list = DSeg.read_img("images.jpg")
    
    # Normalize image to 0-255 range for better filter performance
    if image_list.max() <= 255:
        image_list = image_list*255

    print(np.max(image_list))

    array_R, array_G, array_B = DSeg.RGB_Seggrigation(image_list)

    # Process each channel
    result_R = process_channel(array_R, fil)
    result_G = process_channel(array_G, fil)
    result_B = process_channel(array_B, fil)

    final_arr = DSeg.RGB_Conjugation(result_R, result_G, result_B)

    # Final normalization to ensure values are in [0, 255]
    final_arr = np.clip(final_arr, 0, 255)

    DSeg.show_img(final_arr, "F")

main()
