# YOLOv5 Object Detection

This repository contains a Python script for performing object detection using the YOLOv5 model from Ultralytics. The script processes images from a specified directory and detects objects in them using the pre-trained YOLOv5 model.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/SohWeeChen/Execute_YOLO_Detected_Results.git
    ```

2. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Place your images in the `images/` directory.

2. Run the script:

    ```bash
    python main.py
    ```

3. The script will process each image in the `images/` directory and print the names of the detected objects.

## Requirements

- Python 3
- OpenCV (`cv2`)
- Ultralytics YOLOv5

## Acknowledgements

This project utilizes the YOLOv5 model from Ultralytics. For more information, visit their [GitHub repository](https://github.com/ultralytics/yolov5).
