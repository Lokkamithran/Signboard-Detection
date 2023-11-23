from keras.models import load_model
import pandas as pd
from PIL import Image
import numpy as np
from sklearn.metrics import accuracy_score

model = load_model("my_model.keras")

y_test = pd.read_csv('Test.csv')
labels = y_test["ClassId"].values
imgs = y_test["Path"].values
data = []

for img in imgs:
   image = Image.open(img)
   image = image.resize((30,30))
   data.append(np.array(image))

X_test = np.array(data)
predict_x = model.predict(X_test)
classes_x = np.argmax(predict_x, axis=1)

print("\nAccuracy: ", accuracy_score(labels, classes_x)*100, "%")
model.save('traffic_classifier.keras')