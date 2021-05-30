from utils import info_loader
from utils import image_loader
from models import model
import numpy as np
from sklearn.preprocessing import OneHotEncoder
from tensorflow.keras.models import load_model

image_info = info_loader.getInfo(traning=False)
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

# model.run_test_harness(images, targets, 1500, len(target_labels))

model = load_model('final_model.h5')
results = model.evaluate(images, targets, batch_size=128)

print("test loss, test acc:", results)

