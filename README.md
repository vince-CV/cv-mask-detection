# cv-mask-detection
Training custom object detector using yolo v3 and v4, along with inference and deployment.

This project will using Kaggle image set: Face Mask Dataset (YOLO format), for training object detector.
<https://www.kaggle.com/aditya276/face-mask-dataset-yolo-format>

### 1. Change Runtime Type ###
Runtime -> Change runtime type -> Select hardware Accelerator as GPU.


### 2. Link Google Drive ###
```python
from google.colab import drive
drive.mount('/content/drive')
```
Enter into the folder:<br>
`%cd /content/drive/My\ Drive/Mask\ Detector`


### 3. Clone DarkNet Repository ###
`!git clone https://github.com/AlexeyAB/darknet.git`


### 4. Compile DarkNet ###
1. Build darknet with OpenCV
2. Build with CUDA enabled
3. Build with cuDNN enabled.

Enter into darknet folder:<br>
`%cd darknet`

`!sed -i 's/OPENCV=0/OPENCV=1/' Makefile`

`!sed -i 's/GPU=0/GPU=1/' Makefile`

`!sed -i 's/CUDNN=0/CUDNN=1/' Makefile`

`print("Building. . . It might take 2-3 minutes")`

`!make &> build_log.txt`

`print("Build Done!")`


### 5. Prepare Dataset Files ###
see `data_prepare.py`. (This file modifies the .txt file directing the images and labels).


### 6. Prepare Configuration File for YOLO Training ###
1. train.cfg
2. test.cfg
3. setup.data
4. class.names

Should modify each file accordingly. See more details in appendix.


### 7. Prepare weights for Convolutional backbone ###
Yolov3 pretrained weights:
https://pjreddie.com/media/files/darknet53.conv.74<br>

Yolov4 pretrained weights: 
https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v3_optimal/yolov4.weights<br>


### 8. Start Training ###
For starting training using darknet, we need to execute the following command. Here we are specifying the:
1. path to the setup file,
2. path to config file,
3. path to convolutional weights file.<br>
`!./darknet detector train ../configuration_v3/setup.data ../configuration_v3/train.cfg ./backup/darknet53.conv.74 -dont_show -map 2> train_log.txt`


## Experiments & Results
![Image](/chart.png)
![Image](/demo.png)
