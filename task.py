from imageio import imread, imwrite
from math import ceil
import numpy as np

N = 5

im = imread('putin.bmp')

h = len(im)
w = len(im[0])
print('width=', w, 'height=', h)
im1 = np.empty((h*N, w*N, 3), dtype=np.uint8)
im2 = np.empty((ceil(h/N)-1, ceil(w/N)-1, 3), dtype=np.uint8)

for ix in range(h*N):
    for iy in range(w*N):
        im1[ix][iy] = im[ix//N][iy//N]

for ix in range(ceil(h/N)-1):
    for iy in range(ceil(w/N)-1):
        sum = [0, 0, 0]
        for k_ix in range(ix*N, ix*N+N):
            for k_iy in range(iy*N, iy*N+N):
                sum[0] += im[k_ix][k_iy][0]
                sum[1] += im[k_ix][k_iy][1]
                sum[2] += im[k_ix][k_iy][2]
        sum[0] //= N*N
        sum[1] //= N*N
        sum[2] //= N*N

        im2[ix][iy] = sum


imwrite('face.bmp', im1)
imwrite('face2.bmp', im2)
