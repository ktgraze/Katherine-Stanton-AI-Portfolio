# Lab 09: Object Detection with SSD MobileNet V2
### ITAI 1378 - Computer Vision | Houston City College

![Python](https://img.shields.io/badge/Python-3.x-blue)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange)
![TensorFlow Hub](https://img.shields.io/badge/TensorFlow%20Hub-SSD%20MobileNet%20V2-yellow)
![Platform](https://img.shields.io/badge/Platform-Google%20Colab-lightgrey)

---

## Problem Statement

Image classification tells you what is in an image, but not where. Object detection extends this by localizing objects within an image using bounding boxes alongside class labels and confidence scores. This lab adapts an image classification workflow into a full object detection pipeline, demonstrating how pre-trained models can be applied to real-world datasets under limited computational constraints.

---

## Approach and Methodology

This lab implements an object detection pipeline using a pre-trained SSD MobileNet V2 model loaded from TensorFlow Hub, applied to a subset of the Pascal VOC 2007 dataset.

**1. Dataset Loading**
The Pascal VOC 2007 dataset is loaded using TensorFlow Datasets (`tfds`). A 10% subset of the training and validation splits is used to keep the exercise computationally manageable. The dataset contains 20 object categories including people, animals, and vehicles.

**2. Data Visualization**
Sample images are displayed with ground truth bounding boxes drawn using Matplotlib patches to establish a visual baseline before running the model.

**3. Model Loading**
SSD MobileNet V2 is loaded from TensorFlow Hub. SSD (Single Shot Detector) is a lightweight, efficient architecture well-suited to environments with limited GPU resources. It predicts bounding boxes and class labels in a single forward pass.

**4. Object Detection and Visualization**
The detector is run on sample images. Predicted bounding boxes (red) are displayed alongside ground truth boxes (green) for direct comparison. A confidence threshold of 0.5 is applied to filter low-confidence predictions.

**5. Model Evaluation**
A custom evaluation function computes True Positives, False Positives, and False Negatives using Intersection over Union (IoU) at a threshold of 0.5. Precision and recall are reported across 100 validation samples.

**6. Custom Image Upload**
An interactive upload function allows arbitrary images to be submitted for detection at runtime in Google Colab.

---

## Results and Evaluation

Model performance is evaluated using IoU-based precision and recall on a subset of the Pascal VOC 2007 validation set:

- **True Positives:** Objects correctly detected and localized (IoU >= 0.5, correct class)
- **False Positives:** Detections with poor localization or incorrect class
- **False Negatives:** Ground truth objects missed by the model
- **Confidence Threshold:** 0.5 (predictions below this score are filtered out)
- **IoU Threshold:** 0.5 (standard benchmark threshold for object detection)

Note: Due to the use of a small dataset subset and a lightweight model, precision and recall are lower than would be expected on the full VOC 2007 dataset. The focus of this lab is on understanding the object detection workflow rather than maximizing performance metrics.

---

## Data Sources

**Pascal VOC 2007 (Visual Object Classes)**
Loaded automatically via TensorFlow Datasets:

```python
tfds.load('voc/2007', split='train[:10%]')
```

The dataset contains images annotated with bounding boxes and class labels across 20 object categories. It is a standard benchmark for object detection research.

**Pre-trained Model**
SSD MobileNet V2 loaded from TensorFlow Hub:

```
https://www.kaggle.com/models/tensorflow/ssd-mobilenet-v2/TensorFlow2/ssd-mobilenet-v2/1
```

---

## Requirements and Dependencies

See `requirements.txt` for the full dependency list. Key libraries:

| Library | Purpose |
|---------|---------|
| `tensorflow` | Core deep learning framework |
| `tensorflow-hub` | Loading the pre-trained SSD MobileNet V2 model |
| `tensorflow-datasets` | Loading the Pascal VOC 2007 dataset |
| `numpy` | Array operations |
| `matplotlib` | Bounding box and image visualization |
| `opencv-python` | Image processing utilities |
| `Pillow` | Image loading and format handling |

To run the notebook:

```bash
pip install -r requirements.txt
jupyter notebook L09_Katherine_Stanton_ITAI1378.ipynb
```

Or open directly in Google Colab. GPU runtime is recommended but not required.

---

## Learning Outcomes

This lab clarified the distinction between image classification and object detection, and gave me hands-on experience with the full object detection pipeline from dataset loading to bounding box visualization and evaluation. Implementing the IoU-based evaluation function from scratch deepened my understanding of how localization accuracy is measured independently from classification accuracy. Working with a lightweight pre-trained model under computational constraints also highlighted the practical trade-offs between model size, speed, and detection performance — a consideration that is central to deploying computer vision systems in resource-limited environments.

---
