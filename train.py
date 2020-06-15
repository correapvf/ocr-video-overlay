import sys
from pathlib import Path
import cv2
import numpy as np
import config as c

npixels = c.w*c.h
samples = np.empty((0, npixels), 'uint8')
responses = []
keys = [i for i in range(48, 58)]

# resize image window to be visible
cv2.namedWindow('char', cv2.WINDOW_NORMAL)
cv2.resizeWindow('char', c.w*10, c.h*10)

def samplef(key):
    global responses, samples
    responses.append(key)
    sample = im.reshape((1, npixels))
    samples = np.append(samples, sample, 0)

print('Press the number of the digit is being displayed\n\
Press Esc to quit\n\
Press Space to ignore digit\n\
Press Enter to set as a blank space')

for path in Path(c.train_folder).glob(c.ext_train):
    # for each image
    img = cv2.imread(str(path))
    cv2.imshow('frame', img)
    
    for n in range(len(c.ifor)):
        # for each number
        
        for j in c.jfor[n]:
            # for each digit
            im = img[c.ifor[n]:c.ifor[n]+c.h, j:j+c.w, c.channel]
            
            cv2.imshow('char', im)
            key = cv2.waitKey(0)
            
            if key == 27:  # escape to quit
                cv2.destroyAllWindows()
                sys.exit()
            elif key == 32: # space to skip to next number
                continue
            elif key == 13 and c.blank: # enter to set as blank space
                samplef(255)
            elif key in keys:
                samplef(int(chr(key)))
                
    if c.blank:
        for n in range(len(c.blankj)):
            j = c.blankj[n]
            i = c.blanki[n]
            im = img[i:i+c.h, j:j+c.w, c.channel]
            samplef(255)

responses = np.array(responses, 'uint8')
responses = responses.reshape((responses.size, 1))
cv2.destroyAllWindows()

np.save('samples.npy', samples)
np.save('responses.npy', responses)

# number of occurrences for each digit
print("number of occurrences for each digit")
unique, counts = np.unique(responses, return_counts=True)
print(np.asarray((unique, counts)).T)
