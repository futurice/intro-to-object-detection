Introduction to Object Detection
===

> This is a starting template to learn how to build an object detector. We want to detect images of a specific object from digital photographs. In order to achieve this goal, we shall employ the help from [opencv3](http://opencv.org/), a computer vision library, for image manipulation, and [dlib](http://dlib.net/), a machine learning library.

### Notes
- Slides at [link](https://docs.google.com/presentation/d/1Dbulz6qFBosbt_qwnS3Bx6FQr0FEz04FwlSCOcTJ9jI/edit#slide=id.g251e44bc4d_0_0)
- The recommended programming language is Python. However, it is possible to adapt to C++ easily.
- It is recommended to use a Python virtual environment. Instal `virtualenv` with `pip`.
- The dlib version from pip does not include all dlib features. It is recommended to build dlib from source.

### Setup environment
1. Install `boost-python`
```bash
# OSX
brew install boost-python --with-python3

# Ubuntu
sudo apt-get install libboost-all-dev
```

2. Create virtual python environment (optional)
```bash
virtualenv .env -p python3.6
source .env/bin/activate
```
3. Install dependencies (`opencv3` and `dlib`)
```bash
pip install -r requirements.txt
```

4. Cleanup (optional, in case you want to recreate your python environment)
```bash
deactivate
rm -rf .env
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
