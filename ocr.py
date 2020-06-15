from pathlib import Path
import cv2
import numpy as np
import pandas as pd
import config as c

# load files from train.py
samples = np.load('samples.npy')
responses = np.load('responses.npy')

# create a list with columns names
npixels = c.w*c.h
names_flag = [i + '_flag' for i in c.names]
cols = ['seconds']
for name, flag in zip(c.names, names_flag):
    cols.append(name)
    cols.append(flag)

# train the model
samples = np.float32(samples)
responses = np.float32(responses)
model = cv2.ml.KNearest_create()
model.train(samples, cv2.ml.ROW_SAMPLE, responses)

for path in Path(c.ocr_folder).rglob(c.ext_train):
    # for each movie
    cap = cv2.VideoCapture(str(path))
    fps = cap.get(cv2.CAP_PROP_FPS)
    t_add = 1/fps
    fps = int(fps*c.time_interval)
    dados = []
    t = 0.0
    i = 0

    rtv = cap.grab()
    while rtv: # movie is open
        if i % fps:
            rtv = cap.grab()
        else:
            # for each frame
            rtv, img = cap.retrieve()
            line = [f'{t:05.1f}']

            for n in range(len(c.ifor)):
                # for each number
                string = ''
                thr = 0

                for j in c.jfor[n]:
                    # for each digit
                    im = img[c.ifor[n]:c.ifor[n]+c.h,j:j+c.w,c.channel]
                    im = im.reshape((1, npixels))
                    im = np.float32(im)

                    retval, results, neigh_resp, dists = model.findNearest(im, k=1)
                    if results[0][0] != 255: # skip if blank space
                        string += str(int(results[0][0]))

                    if dists[0][0] > c.dist_thr:
                        thr += 1

                string = c.ffor[n](string)
                line.append(string)
                line.append(str(thr))

            dados.append(line)

        i += 1
        t += t_add

    # create a data frame and save
    df = pd.DataFrame(dados, columns = cols, dtype = str) 
    df.to_csv(path.with_suffix('.csv'), index=False)
