from imageio import imread, imwrite

import numpy as np

N = 5

im = imread('putin.bmp')

h = len(im)
w = len(im[0])
print('width=', w, 'height=', h, range(5), 1//5, 5//5)
im1 = np.empty((h*N, w*N, 3), dtype=np.uint8)

for ix in range(h*N):
    for iy in range(w*N):
        im1[ix][iy] = im[ix//N][iy//N]


imwrite('face.bmp', im1)
