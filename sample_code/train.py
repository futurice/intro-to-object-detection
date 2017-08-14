"""
This file demos the training of an SVM for object detection.
You should already a have labeled training set in the form of XML file. Use imglab to create one if you have not.
"""

import dlib

options = dlib.simple_object_detector_training_options()
# Enable this option if your object is symmetrical.
# options.add_left_right_image_flips = True
options.C = 5 # Specify penalty parameter, too large - overfit, too small - underfit
options.num_threads = 4
options.be_verbose = True

training_xml_path = os.path.abspath('training.xml')

detector_svm_name = "detector.svm"

# Train SVM
dlib.train_simple_object_detector(training_xml_path, detector_svm_name, options)

# Validate SVM
# Should use a different image set for testing
log.info("Training accuracy: %s" % dlib.test_simple_object_detector(training_xml_path, detector_svm_name))
