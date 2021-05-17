from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.preprocessing.image import save_img
import os
import numpy as np

image_base_path = 'nabirds/images/'

def load_image(filename):
    # load the image
    img = load_img(filename, target_size=(64, 64))
    # convert to array
    img = img_to_array(img)
    # reshape into a single sample with 3 channels
    img = img.reshape(64,64,3)
    # save_img('images/' + filename[23:], img)
#     img = img.astype('float32')  
#     img = img - [123.68, 116.779, 103.939]  
    return img

def load_images(infos):
    images = []
    for info in infos:
            images.append(load_image(image_base_path + info[0]))

    return np.array(images)