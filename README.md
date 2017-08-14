Introduction to Object Detection
===

> This is a starting template to learn how to build an object detector. We want to detect images of a specific object from digital photographs. In order to achieve this goal, we shall employ the help from [opencv3](http://opencv.org/), a computer vision library, for image manipulation, and [dlib](http://dlib.net/), a machine learning library.

### Important notes
- OSX users should install x11.
- The recommended programming language is Python. However, it is possible to adapt to C++ easily.
- It is highly recommended to use `Anaconda` over `pip`, since packages from pip can have missing components.
- Use python 2.7 or 3.5, because opencv3 is not prepackaged for python 3.6 on OSX.
- Download Anaconda from [here](https://www.continuum.io/downloads).
- Install Anaconda

### Setup environment
1. Create and activate python 3.5
```bash
conda create --name object-detection python=3.5
source activate object-detection
```
2. Install `opencv3` and `dlib`
```bash
conda install --name object-detection -c menpo opencv3 dlib
```

3. Cleanup (optional, in case you want to recreate your python environment)
```bash
source deactivate
conda remove --name object-detection --all
```

### Challenge instruction
You are to build an image object detector (that detects object images in photograph). In order for your detector to work, you need to teach your detector how to recognize a certain object (e.g. a car, a house, a dog, a cat, ...). The steps to teach your detector are as follow:
1. Find an image source of photographs of your object (Google, Bing, DuckduckGo).
2. Manually label your object in the photographs with `imglab` (provided).
3. Create an SVM from the labeled data (this is when you start coding).
4. Use the trained SVM as your object detector.

##### How to use `imglab`
- Register images to label
```bash
imglab -c training.xml <training image source directory>
imglab -c testing.xml <testing image source directory>
```

- Label images
```bash
imglab training.xml
```
