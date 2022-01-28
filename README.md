# captcha-clicker
This project contains two files that when working together will automatically recognize images on a screen from a captcha and identify the image classification using a deep learning model.

Programmer: Alex Balayan, Bryan Nguyen
Class: CS478 Intro to Deep Learning - Final Project
Files: auto.py (autoclicker), items.py (cnn model)

PROJECT DESCRIPTION:  This project is split into two components, the autoclicker file and the deep learning model.  The auto.py file contains the autoclicker program that will randomly search various items displayed on a screen and will randomly select images found in various areas.  If a captcha is currently displayed, the clicker will randomly select the images and pass the image file onto the model which will attempt to identify what the image content is.  If the model prediction matches the target choice of the captcha, the autoclicker will then select that image on the screen.

The items.py file contains the model that will attempt to identify the classification of the selected image.  This file uses a convolution neural network of two layers to process an image and fit it with one of the classification categories learned from the Cifar-10 dataset.  The Cifar-10 dataset, provided with integration by Google Tensorflow, will train the model to recognize 10 types of images.  For studying purposes, a focus on planes, trucks, and cars were chosen from the dataset to correlate with commonly used images found in captchas.  After the model is trained and saved, the image that is selected is then passed into the model and evaluated for a match.

Because of the size of the model as well as the dataset integration provided by Google Tensorflow, this project was originally run, complied, and trained as a .ipynb file within Google Collab.  For review purposes on Github and other platforms, this project has been converted into a standard .py file.  It is best recommended that this project be done on a Google Collab notebook for optimal performance and storage for the Cifar-10 dataset.
