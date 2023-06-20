import numpy as np
from keras import Sequential
from keras.layers import Dense
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
import pandas as pd

df = pd.read_csv(r"C:\Users\mrchl\OneDrive\Desktop\Programowanie\PWOI\studia_programowanie_w_obliczeniach_inteligentnych\zad4\texture_features.csv")

X = df.drop('filename', axis=1).values
y = df['filename'].apply(lambda x: x.split('_')[0]).values
label_encoder = LabelEncoder()
y_int = label_encoder.fit_transform(y)


# 2. Wykonać kodowanie 1 z n dla wektora y_int → y_onehot
onehot_encoder = OneHotEncoder(sparse=False)
y_int = y_int.reshape(len(y_int), 1)
y_onehot = onehot_encoder.fit_transform(y_int)

# Podzielić zbiór X oraz wektor etykiet y_onehot na część treningową (70%) i testową (30%)
X_train, X_test, y_train, y_test = train_test_split(X, y_onehot, test_size=0.3)

# d. Tworzenie modelu sieci neuronowej
# 1. Utworzyć obiekt sieci typu Sequential
model = Sequential()

# 2. Dodać dwie warstwy typu Dense
model.add(Dense(10, activation='sigmoid', input_dim=6)) # 6 cech
model.add(Dense(3, activation='softmax')) # 3 klasy

# 3. Skompilować model
model.compile(loss='categorical_crossentropy', optimizer='sgd', metrics=['accuracy'])

# e. Uczenie sieci
model.fit(X_train, y_train, epochs=100, batch_size=10, shuffle=True)

# f. Testowanie sieci
# 1. Przekonwertować wektor y_test oraz y_pred do kodowania całkowitego
y_pred = model.predict(X_test)
y_pred_int = np.argmax(y_pred, axis=1)
y_test_int = np.argmax(y_test, axis=1)

# 2. Na podstawie otrzymanych wektorów etykiet całkowitego wyliczyć macierz pomyłek
cm = confusion_matrix(y_test_int, y_pred_int)
print(cm)
