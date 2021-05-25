import numpy as np
import random
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.preprocessing.image import save_img

import sys
from matplotlib import pyplot
from tensorflow.keras.datasets import cifar10
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import MaxPooling2D
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Flatten
from tensorflow.keras.optimizers import SGD
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.layers import Dropout
from tensorflow.keras.layers import BatchNormalization
from tensorflow.keras.models import load_model
import h5py
import numpy as np
from sklearn.preprocessing import OneHotEncoder


basePath = "nabirds/"
images = basePath+"images.txt"
train_test_split = basePath+"train_test_split.txt"
classes = basePath+"classes.txt"
image_class_labels = basePath+"image_class_labels.txt"

def load_image(filename):
    # load the image
    img = load_img(filename, target_size=(128, 128))
    # convert to array
    img = img_to_array(img)
    # reshape into a single sample with 3 channels
    img = img.reshape(128,128,3)
    # save_img('images/' + filename[23:], img)
#     img = img.astype('float32')  
#     img = img - [123.68, 116.779, 103.939]  
    return img

def get_images():
    img_dic = {}
    with open(images) as img_object:
        for line in img_object:
            vals = line.replace('\n', '').split(' ')
            img_dic[vals[0]] = vals[1]
    return img_dic

def get_training_info():
    train_dic = {}
    with open(train_test_split) as train_object:
        for line in train_object:
            vals = line.replace('\n', '').split(' ')
            train_dic[vals[0]] = vals[1]
    return train_dic

def get_labels ():
    selected_lines = {}
    with open(classes) as class_object:
        lines = class_object.readlines()

        for line in lines:
            vals = line.replace('\n', '').split(' ')
            key = vals[0]
            vals.remove(key)
            val = ' '.join(vals)
            selected_lines[key] = (val)
    return selected_lines

def get_classes():
    image_class_dic = {}
    with open(image_class_labels) as image_class_object:
        for line in image_class_object:
            vals = line.replace('\n', '').split(' ')
            image_class_dic[vals[0]] = vals[1]
    return image_class_dic

def merge_label_image_train():
    classes = get_classes()
    train = get_training_info()
    images = get_images()
    labels = get_labels()


    print(labels)

    encoder = OneHotEncoder()
    one_hot = np.array(encoder.fit_transform([[labels[key]] for key in labels]).toarray())
    i = 0
    for key in labels:
        labels[key] = one_hot[i]
        i += 1

    res = {}
    for key in images:
        if bool(int((train[key]))):
            res[images[key]] = (labels[classes[key]], bool(int((train[key]))))
    return res


def image_generator(files, batch_size= 128):
    images = merge_label_image_train()

    while True:
        # Select files (paths/indices) for the batch
        batch_paths  = np.random.choice(a = files, size = batch_size)
        batch_input  = []
        batch_output = [] 
        # Read in each input, perform preprocessing and get labels          
        for input_path in batch_paths:              
            input = load_image('nabirds/images/' + input_path)
            output = images[input_path][0]
            batch_input += [ input ]
            batch_output += [ output ]          
            # Return a tuple of (input, output) to feed the network             
        batch_x = np.array( batch_input )
        batch_y = np.array( batch_output )
        
        yield batch_x, batch_y 

# image_generator(["",""], )
# print(merge_label_image_train())


def define_model(output_size):  
	model = Sequential()
    #try 224, 248, 496
	model.add(Conv2D(128, (3, 3), activation='relu', kernel_initializer='he_uniform', padding='same', input_shape=(128, 128, 3)))
	model.add(BatchNormalization())
	model.add(Conv2D(128, (3, 3), activation='relu', kernel_initializer='he_uniform', padding='same'))
	model.add(BatchNormalization())
	model.add(MaxPooling2D((2, 2)))
	model.add(Dropout(0.2))
	model.add(Conv2D(256, (3, 3), activation='relu', kernel_initializer='he_uniform', padding='same'))
	model.add(BatchNormalization())
	model.add(Conv2D(256, (3, 3), activation='relu', kernel_initializer='he_uniform', padding='same'))
	model.add(BatchNormalization())
	model.add(MaxPooling2D((2, 2)))
	model.add(Dropout(0.3))
	model.add(Conv2D(512, (3, 3), activation='relu', kernel_initializer='he_uniform', padding='same'))
	model.add(BatchNormalization())
	model.add(Conv2D(512, (3, 3), activation='relu', kernel_initializer='he_uniform', padding='same'))
	model.add(BatchNormalization())
	model.add(MaxPooling2D((2, 2)))
	model.add(Dropout(0.4))
	model.add(Flatten())
	model.add(Dense(512, activation='relu', kernel_initializer='he_uniform'))
	model.add(BatchNormalization())
	model.add(Dropout(0.5))
	model.add(Dense(output_size, activation='softmax'))
	# compile model
	opt = SGD(lr=0.001, momentum=0.9)
	model.compile(optimizer=opt, loss='categorical_crossentropy', metrics=['accuracy'])
	return model



def get_image_path_train():
    train = get_training_info()
    images = get_images()

    res = []
    for key in images:
        if bool(int((train[key]))):
            res.append(images[key])
    return res

# run the test harness for evaluating a model
def run_test_harness(epochs, output_size):
    # define model
	model = define_model(output_size)
	# model = load_model('final_model.h5')
	# create data generator
	# datagen = 
#     featurewise_center=True
	# specify imagenet mean values for centering
# 	datagen.mean = [123.68, 116.779, 103.939]
	# prepare iterator

	# train_it = datagen.flow(images, targets)

	# fit model
	model.fit(image_generator(get_image_path_train()), steps_per_epoch=128, epochs=epochs, verbose=1)
	# save model
	model.save('final_model.h5')

run_test_harness(1000, 555)

# print(get_image_path_train())

i = get_images()
# print([i[key] for key in i])

# for idk in image_generator([i[key] for key in i]):
#     print(idk)
 
# print(merge_label_image_train())

# # entry point, run the test harness
# run_test_harness()

