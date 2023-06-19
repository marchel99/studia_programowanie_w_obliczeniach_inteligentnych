import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score


data = pd.read_csv(r"C:\Users\mrchl\OneDrive\Desktop\Programowanie\PWOI\studia_programowanie_w_obliczeniach_inteligentnych\zad3\texture_features.csv")



# data['class'] = data['filename'].apply(lambda x: x.split('_')[2])
data['class'] = 'unknown'


X = data[['dissimilarity', 'correlation', 'contrast', 'energy', 'homogeneity', 'ASM']]

y = data['class']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

clf = KNeighborsClassifier(n_neighbors=3)
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"Dokładność klasyfikatora: {accuracy*100:.2f}%")
