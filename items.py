import tensorflow as tf
from tensorflow.keras import datasets, layers, models
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import confusion_matrix , classification_report
from google.colab import files
from keras.preprocessing import image
import cv2

#Load the cifar10 dataset.  This dataset includes images from 10 different categories
#in which are commonly used in captcha programs.  It will then segment the data
#into training and testing, as well as reshaping images for con
(x_train, y_train), (x_test, y_test) = datasets.cifar10.load_data()
x_train = x_train / 255
x_test = x_test / 255

y_train = y_train.reshape(-1,)
y_test = y_test.reshape(-1,)

#class categories provided by the cifar10 dataset
class_names = ["airplane", "automobile", "bird","cat","deer","dog","frog","horse","ship","truck"]

#function used to test a data sample from the set
def plot_sample(x,y, index):
  plt.figure(figsize= (15,2))
  plt.imshow(x[index])
  plt.xlabel(classes[y[index]]) #label of image

#testing out a sample
plot_sample(x_train, y_train, 40)


#building the cnn model
cnn = models.Sequential([
  layers.Conv2D(filters=32, kernel_size=(3,3), activation='relu', input_shape=(32,32,3)),
  layers.MaxPooling2D((2,2)),
  layers.Conv2D(filters=64, kernel_size=(3,3), activation='relu', input_shape=(32,32,3)),
  layers.MaxPooling2D((2,2)),
  layers.Flatten(),
  layers.Dense(64, activation='relu'),
  layers.Dense(10, activation='softmax')
])

#compile model and prepare to fit
cnn.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
cnn.fit(x_train, y_train, epochs=10)

#classification report on model accuracy
y_pred = cnn.predict(x_test)
y_pred_classes = [np.argmax(element) for element in y_pred]

print("Classification Report: \n", classification_report(y_test, y_pred_classes))

#evaluating fit
cnn.evaluate(x_test, y_test)
x_test.shape

#testing model prior to using
y_pred = cnn.predict(x_test)
y_pred[:5]

y_classes = [np.argmax(element) for element in y_pred]
y_classes[:5]
y_test[:5]

#save the model for reuse
cnn.save("model.h5")

#now that model is trained, this segment will take a file from autoclicker and check to see
#if it is an image belonging to one of the classifications from the cifar10 dataset
uploaded = files.upload()

# class labels used to display category of image
class_names = ["airplane", "automobile", "bird", "cat", "deer", "dog", "frog", "horse", "ship", "truck"]

for fn in uploaded.keys():
    # selecting image path (alternatively, file path can be coded in)
    path = fn
    img = image.load_img(path, target_size=(32, 32))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    images = np.vstack([x])

    # creating prediction from inserted image
    prediction = cnn.predict(images, batch_size=10)
    print(fn)

    # getting label from prediction result and display to user
    result = [np.argmax(element) for element in prediction]
    result_label = result[0]
    print(result)
    print(result_label)
    print(class_names[result_label])

