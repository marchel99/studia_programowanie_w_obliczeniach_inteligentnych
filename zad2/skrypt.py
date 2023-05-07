import os
import numpy as np
import pandas as pd
from skimage import io, color, feature
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score


def extract_texture_features(image, size):
    gray_image = color.rgb2gray(image)
    # Reducing bit depth to 6 bits (64 levels)
    gray_image = (gray_image * 63).astype(int)
    glcm = feature.greycomatrix(gray_image, [1, 3, 5], [
                                0, np.pi/4, np.pi/2, 3*np.pi/4], levels=64, symmetric=True)
    features = {
        'dissimilarity': feature.greycoprops(glcm, 'dissimilarity').ravel(),
        'correlation': feature.greycoprops(glcm, 'correlation').ravel(),
        'contrast': feature.greycoprops(glcm, 'contrast').ravel(),
        'energy': feature.greycoprops(glcm, 'energy').ravel(),
        'homogeneity': feature.greycoprops(glcm, 'homogeneity').ravel(),
        'ASM': feature.greycoprops(glcm, 'ASM').ravel()
    }
    return features


def extract_texture_samples(directory, size):
    samples = []
    labels = []
    for category in os.listdir(directory):
        category_dir = os.path.join(directory, category)
        if os.path.isdir(category_dir):
            for filename in os.listdir(category_dir):
                filepath = os.path.join(category_dir, filename)
                image = io.imread(filepath)
                for i in range(0, image.shape[0], size):
                    for j in range(0, image.shape[1], size):
                        if i + size <= image.shape[0] and j + size <= image.shape[1]:
                            sample = image[i:i+size, j:j+size]
                            features = extract_texture_features(sample, size)
                            samples.append(features)
                            labels.append(category)
    return samples, labels


def save_texture_samples_to_csv(samples, labels, output_file):
    data = pd.DataFrame(samples)
    data['Category'] = labels
    data.to_csv(output_file, index=False)


def classify_texture_samples(input_file, test_size):
    data = pd.read_csv(input_file)
    X = data.drop('Category', axis=1).values
    y = data['Category'].values
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=42)
    classifier = KNeighborsClassifier()
    classifier.fit(X_train, y_train)
    y_pred = classifier.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    return accuracy


# Wczytanie kolejnych obrazów i wycięcie fragmentów tekstury
image_directory = 'ścieżka/do/katalogu/z/obrazami'
output_directory = 'ścieżka/do/katalogu/z/wyciętymi/fragmentami'
texture_size = 128
samples, labels = extract
