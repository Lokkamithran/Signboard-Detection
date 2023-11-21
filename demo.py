from keras.models import load_model
import pandas as pd
from PIL import Image
import numpy as np

model = load_model("my_model.h5")
# print(model.summary())

from sklearn.metrics import accuracy_score
y_test = pd.read_csv('Test.csv')
labels = y_test["ClassId"].values
imgs = y_test["Path"].values
data=[]
for img in imgs:
   image = Image.open(img)
   image = image.resize((30,30))
#    print(image.size)
   data.append(np.array(image))
X_test=np.array(data)
print(X_test.shape)
# pred = model.predict_classes(X_test)
predict_x=model.predict(X_test)
classes_x=np.argmax(predict_x,axis=1)

#Accuracy with the test data
from sklearn.metrics import accuracy_score
print(accuracy_score(labels, classes_x))
# model.save('traffic_classifier.h5')