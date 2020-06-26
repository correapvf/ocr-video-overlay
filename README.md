# OCR for low resolution video overlay

### A script to extract information (e.g. time, coordinates, depth, etc) from a video overlay. 

This script was designed for low resolution videos (SD), where digits are below 15x15 pxs size, often connected with each other and bearing a bad contrast with the background.

<img alt="overlay example" src=./docs/overlay_example.png width="350">

In these conditions, others OCRs methods (e.g. [tesseract](https://github.com/tesseract-ocr/tesseract)) usually fail to recognize the digits. Otherwise, you should check [ViTexOCR](https://www.sciencebase.gov/catalog/item/58dd56ace4b02ff32c685954), a nice implementation in python using tesseract to extract overlay information from videos.<br>
The font of the overlay should be monospaced for better results, as you have manually input the positions for each digit.<br>
The script uses K-Nearest Neighbors (kNN) classification algorithm from opencv to recognize the digits.

### Usage

Read and edit `config.py` to insert the positions of each digit and number you want to recognize. You can use any image editor in a extracted frame to get these positions.<br>
Note: the upperleft pixel must start at (0,0)

See an example below, followed by how the code in `config.py` should be made for two numbers. The pixels coordinates that must be informed are the yellow dots.

<img src=./docs/overlay_example2.png width="500">

```
h = 10 # height of the digits 
w = 7 # width of the digits
latj = [50,60,70,80,90,100,120,130] # X position for each lat digit
lati = 8 # Y position for lat digits
longj = [50,60,70,80,90,100,110,130,140] # X position for each long digit
longi = 26 # Y position for long digits
jfor = [latj, longj] # put each number in these lists - X values
ifor = [lati, longi] # put each number in these lists - Y values
```

Run `train.py` to train the model using a set of extracted frames. You have to manually inform the digit is being displayed.

Run `ocr.py` to recognize the digits on the video overlay. It should generate a csv for each video with the numbers recognized and a flag, indicating the number of digits that were recognized with a low reliability.

#### Requirements
- Python3
- numpy, pandas and opencv
