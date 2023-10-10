import cv2
import numpy as np

image_path = 'poji.jpg'
original_image = cv2.imread(image_path,1)

frame_height, frame_width, _ = original_image.shape 


video_writer = cv2.VideoWriter('img_addition1-1.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 30, (frame_width, frame_height))
adjusted_image = np.copy(original_image)

for number in range(200):
    print("process image: ",number)
    for y in range(adjusted_image.shape[0]):
        for x in range(adjusted_image.shape[1]):
            b, g, r = adjusted_image[y, x]

            if r < 255 :
                r = min(255, r + 1)
            if g < 255 :
              g = min(255, g + 1)
            if b < 255 :
             b = min(255, b + 1)

            adjusted_image[y, x] = (b, g, r)

    video_writer.write(adjusted_image)
video_writer.release()