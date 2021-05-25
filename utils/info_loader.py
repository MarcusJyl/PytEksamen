import random
import numpy as np
import pandas as pd

basePath = "nabirds/"
images = basePath+"images.txt"
train_test_split = basePath+"train_test_split.txt"
classes = basePath+"classes.txt"
image_class_labels = basePath+"image_class_labels.txt"

def load_txt():
    img_dic = {}
    train_dic = {}
    class_dic = {}
    image_class_dic = {}
    
    with open(images) as img_object:
        for line in img_object:
            vals = line.replace('\n', '').split(' ')
            img_dic[vals[0]] = vals[1]
            
    with open(train_test_split) as train_object:
        for line in train_object:
            vals = line.replace('\n', '').split(' ')
            train_dic[vals[0]] = vals[1]
            
    with open(classes) as class_object:
        for line in class_object:
            vals = line.replace('\n', '').split(' ')
            key = vals[0]
            vals.remove(key)
            val = ' '.join(vals)
            class_dic[key] = (val)
            
    with open(image_class_labels) as image_class_object:
        for line in image_class_object:
            vals = line.replace('\n', '').split(' ')
            image_class_dic[vals[0]] = vals[1]
    
    image_infos = []
    for key in img_dic:
        location = img_dic[key]
        isTraining = bool(int(train_dic[key]))
        class_name = class_dic[image_class_dic[key]]
        image_infos.append([location, isTraining, class_name])
    return image_infos

def getTestInfo():
    data = [d for d in load_txt() if d[1] == True]
    return data

def getTrainInfo():
    data = [d for d in load_txt() if d[1] == False]
    return data

def getInfo(amount = -1, traning=False):
    classes = getClasses(amount)
    class_image_id = getImagesByClasses(classes)
    image_id_status = getTrainingStatus(class_image_id)
    image_id_path = getImagePath(class_image_id)

    
    image_infos = []
    for key in image_id_path:
        location = image_id_path[key]
        isTraining = bool(int(image_id_status[key]))
        class_name = classes[class_image_id[key]]

        image_infos.append([location, isTraining, class_name])
    image_infos = np.array(image_infos)
    if(traning):
        return image_infos[image_infos[:,1] == 'True']
    else :
        return image_infos[image_infos[:,1] == 'False']
    return 

def getImagePath(ids):
    image_ids = [key for key in ids.keys()]
    img_dic = {}
    with open(images) as img_object:
        for line in img_object:
            vals = line.replace('\n', '').split(' ')
            # print(vals)
            if(vals[0] in image_ids):
                img_dic[vals[0]] = vals[1]

    return img_dic

def getTrainingStatus(ids):
    image_ids = [key for key in ids.keys()]
    train_dic = {}
    with open(train_test_split) as train_object:
        for line in train_object:
            vals = line.replace('\n', '').split(' ')
            if(vals[0] in image_ids):
                train_dic[vals[0]] = vals[1]
    return train_dic

def getImagesByClasses(classes):
    class_id = [key for key in classes.keys()]
    image_class_dic = {}
    with open(image_class_labels) as image_class_object:
        for line in image_class_object:
            vals = line.replace('\n', '').split(' ')
            if(vals[1] in class_id):
                image_class_dic[vals[0]] = vals[1]
    
    return image_class_dic

def getClasses(amount=-1):
    selected_lines = {}
    with open(classes) as class_object:
        lines = class_object.readlines()
        num_of_lines = len(lines)

        if(amount > 0 & amount < num_of_lines):
            line_nums = sorted(random.sample(range(0, num_of_lines), amount))
            print(line_nums[0])
            lines = [lines[n] for n in line_nums]

        for line in lines:
            vals = line.replace('\n', '').split(' ')
            key = vals[0]
            vals.remove(key)
            val = ' '.join(vals)
            selected_lines[key] = (val)
    return selected_lines


    