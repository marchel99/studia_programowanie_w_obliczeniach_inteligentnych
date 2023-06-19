import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# wczytanie danych
data = pd.read_csv(r"C:\Users\ziomk\OneDrive\Pulpit\MGR I SEM\Programowanie w obliczeniach inteligentnych\lab3\texture_features.csv")

# etykiety klas
data['class'] = data['filename'].apply(lambda x: x.split('_')[2])

# wyodrębnienie wektorów cech
X = data[['dissimilarity', 'correlation', 'contrast', 'energy', 'homogeneity', 'ASM']]

# wyodrębnienie etykiet klas
y = data['class']

# podział na zbiór treningowy i testowy
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# skalowanie danych
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# uczenie klasyfikatora
clf = KNeighborsClassifier(n_neighbors=3)
clf.fit(X_train, y_train)

# predykcja na zbiorze testowym
y_pred = clf.predict(X_test)

# obliczenie dokładności
accuracy = accuracy_score(y_test, y_pred)
print(f"Dokładność klasyfikatora: {accuracy*100:.2f}%")
