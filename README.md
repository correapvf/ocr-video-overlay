# OCR for video overlay

### A script to extract information (e.g. time, coordinates, depth, etc) from a video overlay. 

This script was designed for low resolution videos (SD), where digits are below 15x15 pxs size, often connected with each other and bearing a bad contrast with the background.

![overlay example](docs/overlay_example.png)

In these conditions, others OCRs methods (e.g. [tesseract](https://github.com/tesseract-ocr/tesseract)) usually fail to recognize the digits. Otherwise, you should check [ViTexOCR](https://www.sciencebase.gov/catalog/item/58dd56ace4b02ff32c685954), a nice implementation in python using tesseract to extract overlay information from videos.<br>
The font of the overlay should be monospaced for better results, as you have manually input the positions for each digit.

### Usage

Read and edit `config.py` to insert the positions of each digit and number you want to recognize. You can use any image editor in a extracted frame to get these positions.<br>
Note: the upperleft pixel must start at (0,0)

Run `train.py` to train the model using a set of extracted frames. You have to manually inform the digit is being displayed.

Run `ocr.py` to recognize the digits on the video overlay. It should generate a csv for each video with the numbers recognized and a flag, indicating the number of digits that were recognized with a low reliability.

#### Requirements
`numpy`, `pandas` and `cv2`<br>
All can be installed using **pip**