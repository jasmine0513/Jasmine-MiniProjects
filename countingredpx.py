
"""
Jasmine Carrion
jasmine.carrion73@myhunter.cuny.edu
"""

import numpy as np
import matplotlib.pyplot as plt

def count_red_pixels(image):
    red_channel = image[:, :, 0]
    red_pixel_count = np.sum(red_channel > 128)
    return red_pixel_count
if __name__ == "__main__":
    img = plt.imread(input("Enter image file name: "))
    count_red_pixels = count_red_pixels(img)
    print(f"Number of red pixels: {count_red_pixels}")