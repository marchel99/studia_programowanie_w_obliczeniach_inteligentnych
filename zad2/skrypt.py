import cv2

def load_image(image_path):
    image = cv2.imread(image_path)
    return image

# Przykładowe użycie funkcji
image_path = 'ścieżka/do/obrazu.jpg'
image = load_image(image_path)
