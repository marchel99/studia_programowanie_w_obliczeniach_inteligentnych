import os
import numpy as np
import pandas as pd
from skimage import io, color, util
from skimage.feature import greycomatrix, greycoprops

def extract_texture_features(img_folders, csv_path):
   
    distances = [1, 3, 5]
    angles = [0, np.pi/4, np.pi/2, 3*np.pi/4]  # 0, 45, 90, 135 stopni
    properties = ['dissimilarity', 'correlation', 'contrast', 'energy', 'homogeneity', 'ASM']

  
    rows = []

    for img_folder in img_folders:
       
        for filename in os.listdir(img_folder):
            if filename.endswith('.jpg') or filename.endswith('.png'):
                img_path = os.path.join(img_folder, filename)
                img = io.imread(img_path, as_gray=True)

               
                img = util.img_as_ubyte(img)
                img = img // 4

                glcm = greycomatrix(img, distances, angles, levels=64, symmetric=True, normed=True)
                feature_values = [greycoprops(glcm, prop).ravel().mean() for prop in properties]

          
                row = [filename] + feature_values
                rows.append(row)


    df = pd.DataFrame(rows, columns=['filename'] + properties)

    #csv
    df.to_csv(csv_path, index=False)


img_folders = [
    r"C:\Users\mrchl\OneDrive\Desktop\Programowanie\PWOI\studia_programowanie_w_obliczeniach_inteligentnych\zad3\FOTO1_samples",
    r"C:\Users\mrchl\OneDrive\Desktop\Programowanie\PWOI\studia_programowanie_w_obliczeniach_inteligentnych\zad3\FOTO2_samples",
    r"C:\Users\mrchl\OneDrive\Desktop\Programowanie\PWOI\studia_programowanie_w_obliczeniach_inteligentnych\zad3\FOTO3_samples"
]
csv_path = r"C:\Users\mrchl\OneDrive\Desktop\Programowanie\PWOI\studia_programowanie_w_obliczeniach_inteligentnych\zad3\texture_features.csv"
extract_texture_features(img_folders, csv_path)
