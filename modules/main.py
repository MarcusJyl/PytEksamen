
from utils import info_loader
from utils import image_loader
from models import model
import numpy as np
from sklearn.preprocessing import OneHotEncoder

image_info = info_loader.getInfo()
# print(info_loader.getInfo(2))
img_info_len = len(image_info)
images = np.array(image_loader.load_images(image_info))
print([t for t in image_info[:10]])
targets = [[target] for target in image_info[:,2]]

# print(image_info)
# print(len(targets))
target_labels = np.unique(targets)
encoder = OneHotEncoder()
targets = np.array(encoder.fit_transform(targets).toarray())

# print(targets)
print([t for t in targets[:10]])

model.run_test_harness(images, targets, 1000, len(target_labels))

print(repr(target_labels))
print(len(target_labels))
