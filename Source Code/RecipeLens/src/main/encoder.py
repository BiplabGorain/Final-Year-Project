import os
import tensorflow as tf
import numpy as np
import pickle
import re
from scipy.spatial.distance import cosine

# Load the pre-trained DenseNet201 model
model = tf.keras.applications.DenseNet201(include_top=False, weights='imagenet',
                                          input_shape=(256, 256, 3), pooling='avg', classes=1000)

# Get the directory of the current script
current_dir = os.path.dirname(__file__)

# Adjust the path to encodings.txt
encodings_path = os.path.join(current_dir, '..', 'encodings.txt')
enc_names_path = os.path.join(current_dir, '..', 'enc_names.txt')

# Load the encoded features and recipe names from files
with open(encodings_path, 'rb') as fp:
    enc_list = pickle.load(fp)
    enc_list = np.array(enc_list)  # Convert to NumPy array
with open(enc_names_path, 'rb') as fp:
    names_list = pickle.load(fp)


def get_encodings(img):
    """
    Preprocesses an image and extracts its features using the DenseNet201 model.

    Args:
        img: A PIL image object.

    Returns:
        A 1-D NumPy array representing the image's encoding.
    """

    # Convert the image to a NumPy array
    img_array = tf.keras.preprocessing.image.img_to_array(img)

    # Resize the image to the model's input shape
    img_array = tf.keras.preprocessing.image.smart_resize(
        img_array, size=(256, 256))

    # Expand the dimension for batch processing (even though it's a single image)
    img_array = np.expand_dims(img_array, axis=0)

    # Preprocess the image using the model's preprocessing function
    img_preprocessed = tf.keras.applications.densenet.preprocess_input(
        img_array)

    # Extract the encoding using the pre-trained DenseNet201 model
    encoding = model.predict(img_preprocessed)

    # Flatten the encoding to a 1-D array
    encoding = encoding.flatten()

    return encoding


def get_recipes(img):
    """
    Calculates cosine similarity between the image encoding and the stored encodings,
    and returns a list of top 10 most similar recipe names.
    """
    enc = get_encodings(img)
    similarity_list = []
    recipe_names_list = []
    print("Shape of enc_list:", enc_list.shape)  # Add this line
    print("Shape of enc:", enc.shape)  # Add this line

    # Iterate through each encoding in the stored encodings list
    for i in range(len(enc_list)):
        # Calculate cosine similarity between the current encoding and the image encoding
        similarity = cosine(enc_list[i].flatten(), enc.flatten())
        similarity_list.append(1 - similarity)

    # Sort the similarity list along with corresponding recipe names
    sorted_list = sorted(zip(similarity_list, names_list), reverse=True)

    # Extract top 10 most similar recipe names
    for i in range(len(sorted_list)):
        name_in_list = sorted_list[i][1]
        # Remove numeric suffix from recipe name
        s = re.sub(r'[0-9]+.jpg', "", name_in_list)
        # Add unique recipe names to the list
        if s not in recipe_names_list:
            recipe_names_list.append(s)
            # Stop when 10 unique recipe names are collected
            if len(recipe_names_list) >= 10:
                break

    return recipe_names_list
