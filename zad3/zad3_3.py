import os
import numpy as np
import pandas as pd
from skimage import io, color, util
from skimage.feature import greycomatrix, greycoprops

def extract_texture_features(img_folder, csv_path):
    # Wartości kierunku i odległości do GLCM
    distances = [1, 3, 5]
    angles = [0, np.pi/4, np.pi/2, 3*np.pi/4]  # 0, 45, 90, 135 stopni
    properties = ['dissimilarity', 'correlation', 'contrast', 'energy', 'homogeneity', 'ASM']

    # DataFrame do przechowywania wyników
    df = pd.DataFrame(columns=['filename'] + properties)

    # Iteracja przez każdy obraz w folderze tekstury
    for filename in os.listdir(img_folder):
        if filename.endswith('.jpg') or filename.endswith('.png'):  # Dodaj tu inne formaty, jeśli są używane
            img_path = os.path.join(img_folder, filename)
            img = io.imread(img_path, as_gray=True)  # Konwersja do skali szarości

            # Zmniejszenie głębi jasności do 5 bitów (64 poziomy)
            img = util.img_as_ubyte(img)
            img = img // 4

            # Obliczanie GLCM i cech
            glcm = greycomatrix(img, distances, angles, levels=64, symmetric=True, normed=True)
            feature_values = [greycoprops(glcm, prop).ravel().mean() for prop in properties]

            # Dodawanie do DataFrame
            series_to_append = pd.Series([filename] + feature_values, index=df.columns)
            df = pd.concat([df, series_to_append.to_frame().T], ignore_index=True)

    # Zapis do pliku csv
    df.to_csv(csv_path, index=False)

# Używanie funkcji
img_folder = r"C:\Users\ziomk\OneDrive\Pulpit\MGR I SEM\Programowanie w obliczeniach inteligentnych\lab3\FOTO1_samples"
csv_path = r"C:\Users\ziomk\OneDrive\Pulpit\MGR I SEM\Programowanie w obliczeniach inteligentnych\lab3\texture_features.csv"
extract_texture_features(img_folder, csv_path)
