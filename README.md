# Frutify-iOS
## iOS application for [Fruit Image Classifier](https://github.com/ShawonAshraf/CSE499Project)

### Description
Binary/ Multiclass image classification of fruits. The trained model can determine whether a fruit is fresh / rotten from the given image. The app can use the camera to take images or, can load an image from the images stored on the device.

### Categories Trained on so far

- Apple(fresh + rotten)
- Mango(fresh + rotten)
- Orange(fresh + rotten)
- Banana(fresh + rotten)

### Screenshots

#### Correct predictions
Real : Fresh, Predicted : Fresh | Real : Fresh, Predicted: Fresh| Real : Fresh, Predicted: Fresh
:------------------------------:| :------------------------------:| :------------------------------:|
![Imgur](https://i.imgur.com/0vGopbq.jpg)| ![Imgur](https://i.imgur.com/khm446d.jpg)| ![Imgur](https://i.imgur.com/So1510V.jpg)

Real : Fresh, Predicted : Fresh | Real : Rotten, Predicted : Rotten | Real : Fresh, Predicted : Fresh|
:------------------------------:| :------------------------------:| :------------------------------:|
![Imgur](https://i.imgur.com/pk6237T.jpg)| ![Imgur](https://i.imgur.com/y2bT0JF.jpg)| ![Imgur](https://i.imgur.com/BrIxqWY.jpg)

#### Wrong predcictions
Real : Fresh, Predicted : Rotten | Real : Fresh, Predicted : Rotten |
:------------------------------:| :------------------------------:|
![Imgur](https://i.imgur.com/a1m0xUL.jpg) | ![Imgur](https://i.imgur.com/icN3mXy.jpg)|



### Dependencies
#### For training

- python 2.7+
- [Anaconda](https://www.anaconda.com/download/)
- [Turi Create](https://github.com/apple/turicreate)
- Detailed package info in the [requirements.txt](https://github.com/ShawonAshraf/Frutify-iOS/blob/master/train_ml_model/requirements.txt) file

#### For app
- Swift 4
- iOS 11.2 SDK / iOS 11.1 SDK
- Xcode 9.2 / 9.1
- macOS 10.13.1+

### Supported devices and platforms
- Any device running iOS 11.1+

### Model evaluation details
Details regarding model evaluation (accuracy, confusion matrix) can be found [here as iPython Notebook](https://github.com/ShawonAshraf/Frutify-iOS/blob/master/train_ml_model/ModelEvaluation.ipynb)

### Usage
Clone the repo or download as a zip
#### For training
- If you don't want to train on a new dataset and want to use what's already available, skip to next part.
- Save your data (images to train on) inside the folder `image_data`
- Loading dataset into a dataframe
```bash
python data_to_df.py
```
- Create model and train
```bash
python predict.py
```
- It'll create a model and mlmodel to use with the iOS application.

#### For app
- Create a Single view iOS app in Xcode with camera view.
- Add the coreml model you got from training or if you skipped training, download the mlmodel from release section of the repo. [link](https://github.com/ShawonAshraf/Frutify-iOS/releases/download/1.0.0b/FrutifyV1_beta.mlmodel)
- Initiate the model inside your swift code and run inference on images captured or in the way you have defined image input on your app.
- If you wish to use the existing app, just import the mlmodel into project directory and build.
- Best if you can test on a device instead of an emulator.


### References

- [Classifying Images with Vision and Core ML](https://developer.apple.com/documentation/vision/classifying_images_with_vision_and_core_ml)
- [Turi Create README](https://github.com/apple/turicreate)
