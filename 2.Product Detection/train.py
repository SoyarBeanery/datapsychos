import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import glob
from tqdm import tqdm
from PIL import Image
import pickle


np_images = []
np_labels = []

for label in tqdm(range(0,42)):
    np_images = []
    np_labels = []
    images = glob.glob(f"resized_images/train/{label:02d}/*.jpg")
    for i in range(len(images)):
        image = Image.open(images[i])
        np_image = np.asarray(image)
        np_images.append(np_image/255)
        np_labels.append(label)
    data_x = np.asarray(np_images)
    data_y = np.asarray(np_labels)
    with open(f'pickles/data_x_{label}.npy','wb') as f:
        np.save(f, data_x)
    with open(f'pickles/data_y_{label}.npy','wb') as f:
        np.save(f, data_y)