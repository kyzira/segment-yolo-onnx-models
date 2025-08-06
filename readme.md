# Segment YOLO ONNX Models

This project enables easy inference with YOLO models exported to ONNX format.

## Features

- Simple interface for running inference on images using ONNX YOLO models
- Automatic class label loading from `classes.txt`
- Lightweight and easy to integrate

## Requirements

- Python 3.7+
- [onnxruntime](https://pypi.org/project/onnxruntime/)
- [numpy](https://pypi.org/project/numpy/)
- [opencv-python](https://pypi.org/project/opencv-python/)

Install dependencies:

```bash

pip install onnxruntime numpy opencv-python

```

## Usage

1. Place your ONNX model and a `classes.txt` file (one class per line) in the same directory.
2. Use the provided inference script to run predictions.


## `classes.txt` Format

Each class name should be on a separate line:

```
person
car
bicycle
...
```
