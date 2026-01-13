import cv2
import numpy as np

# Checkerboard parameters
ROWS = 7   # number of squares vertically
COLS = 10  # number of squares horizontally
SQUARE_SIZE_PX = 200  # large squares for screen use
# actual object height 20cm, width 13cm, 
# distance between photos 6cm 
# square size 2.5cm by 2.5cm
board = np.zeros((ROWS * SQUARE_SIZE_PX, COLS * SQUARE_SIZE_PX), dtype=np.uint8)

for r in range(ROWS):
    for c in range(COLS):
        if (r + c) % 2 == 0:
            board[
                r*SQUARE_SIZE_PX:(r+1)*SQUARE_SIZE_PX,
                c*SQUARE_SIZE_PX:(c+1)*SQUARE_SIZE_PX
            ] = 255

cv2.imwrite("checkerboard.png", board)
