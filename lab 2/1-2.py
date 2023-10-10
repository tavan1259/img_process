import numpy as np
import cv2 
from PIL import Image
import matplotlib.pylab as plt
from matplotlib import gridspec

input_image = cv2.imread('chess.jpg', cv2.IMREAD_COLOR)
num_img = np.linspace(0.1,2, 20)

video_writer = cv2.VideoWriter('img_addition1-2.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 1, input_image.shape[:2][::-1])

for a in num_img:
    gamma_adjusted = (input_image / 255.0) ** a * 255
    gamma_adjusted[gamma_adjusted < 0] = 0
    gamma_adjusted[gamma_adjusted > 255] = 255
    adjusted_image = gamma_adjusted.astype(np.uint8)
    video_writer.write(adjusted_image)

video_writer.release()


