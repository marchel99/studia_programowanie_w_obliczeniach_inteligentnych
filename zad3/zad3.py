from PIL import Image, ImageFilter
import os

def cut_texture(img_folder, save_folder, img_size=(512, 512), sample_size=(128, 128)):
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)

    # Iteruje przez wszystkie pliki w folderze z obrazami
    for filename in os.listdir(img_folder):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            img_path = os.path.join(img_folder, filename)
            img = Image.open(img_path)

            # Zmiana rozmiaru obrazu
            img = img.resize(img_size, Image.Resampling.LANCZOS)

            # Liczba próbek wzdłuż x i y
            xnum = img.size[0] // sample_size[0]
            ynum = img.size[1] // sample_size[1]

            for i in range(xnum):
                for j in range(ynum):
                    # Wycinanie próbki
                    box = (i * sample_size[0], j * sample_size[1], (i + 1) * sample_size[0], (j + 1) * sample_size[1])
                    sample = img.crop(box)

                    # Zapis próbki do folderu zapisu
                    sample_filename = f"{filename[:-4]}_sample_{i}_{j}.jpg"
                    sample_path = os.path.join(save_folder, sample_filename)
                    sample.save(sample_path)







# Używanie funkcji
img_folder = r"C:\Users\mrchl\OneDrive\Desktop\Programowanie\PWOI\studia_programowanie_w_obliczeniach_inteligentnych\zad3\FOTO3"
save_folder = r"C:\Users\mrchl\OneDrive\Desktop\Programowanie\PWOI\studia_programowanie_w_obliczeniach_inteligentnych\zad3\FOTO3_samples"
cut_texture(img_folder, save_folder, img_size=(512, 512), sample_size=(128, 128))
