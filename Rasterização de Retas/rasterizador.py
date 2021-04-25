import matplotlib.pyplot as plt
import numpy as np
import math

def produz_frag(x, y):
    pX = math.floor(x) + 0.5
    pY = math.floor(y) + 0.5

    return pX, pY


def rast(x1, y1, x2, y2, resX, resY):
    x1, x2 = x1 * resX, x2 * resX
    y1, y2 = y1 * resY, y2 * resY

    deltaX = x2 - x1
    deltaY = y2 - y1

    if deltaX != 0 and deltaY != 0:
        m = deltaY / deltaX
    else:
        m = np.inf

    b = y2 - (m * x2)

    x = x1
    y = y1

    xMin = math.floor(min(x1, x2))
    xMax = math.floor(max(x1, x2))

    yMin = math.floor(min(y1, y2))
    yMax = math.floor(min(y1, y2))

    mat = np.zeros((resX, resY), dtype=int)

    pX, pY = produz_frag(x, y)
    mat[math.floor(pX)][math.floor(pY)] = 1

    if deltaX > deltaY:
        for x in range(xMin, xMax):
            y = m * x + b
            pX, pY = produz_frag(x, y)
            mat[math.floor(pX)][math.floor(pY)] = 1
    else:
        for y in range(yMin, yMax):
            x = (y - b) / m
            pX, pY = produz_frag(x, y)
            mat[math.floor(pX)][math.floor(pY)] = 1

    return mat


if __name__ == '__main__':
    matrix = [
        rast(0, 0.2, 0.7, 0.3, 352, 240),
        rast(0, 0.2, 0.7, 0.3, 720, 480),
        rast(0, 0.2, 0.7, 0.3, 1280, 960)
    ]

    fig, figures = plt.subplots(ncols=3, figsize=(10, 10), dpi=300)
    fig = plt.subplots_adjust(wspace=0.3)

    figures[0].set_title('Resolução: 352x240')
    figures[1].set_title('Resolução: 720x480')
    figures[2].set_title('Resolução: 1280x960')

    matrix1 = [
        rast(0.1, 0, 0.75, 0.75, 352, 240),
        rast(0.1, 0, 0.75, 0.75, 720, 480),
        rast(0.1, 0, 0.75, 0.75, 1280, 960)
    ]

    fig1, figures1 = plt.subplots(ncols=3, figsize=(20, 20), dpi=300)
    fig1 = plt.subplots_adjust(wspace=0.3)

    figures1[0].set_title('Resolução: 352x240')
    figures1[1].set_title('Resolução: 720x480')
    figures1[2].set_title('Resolução: 1280x960')

    matrix2 = [
        rast(0, 0.9, 0.6, 0.2, 352, 240),
        rast(0, 0.9, 0.6, 0.2, 720, 480),
        rast(0, 0.9, 0.6, 0.2, 1280, 960)
    ]

    fig2, figures2 = plt.subplots(ncols=3, figsize=(20, 20), dpi=300)
    fig2 = plt.subplots_adjust(wspace=0.3)
        
    figures2[0].set_title('Resolução: 352x240')
    figures2[1].set_title('Resolução: 720x480')
    figures2[2].set_title('Resolução: 1280x960')

    for figure in range(0, len(matrix)):
        figures[figure].imshow(matrix[figure].T,
                               cmap=plt.cm.gray_r,
                               origin="lower")

    for figure in range(0, len(matrix1)):
        figures1[figure].imshow(matrix1[figure].T,
                                cmap=plt.cm.gray_r,
                                origin="lower")

    for figure in range(0, len(matrix2)):
        figures2[figure].imshow(matrix2[figure].T,
                                cmap=plt.cm.gray_r,
                                origin="lower")

    plt.show()