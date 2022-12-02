ds_path = '/Users/chris/data/'

label_path = 'okutama_action/TrainSetFrames/Labels/MultiActionLabels/3840x2160/'
img_paths = 'okutama_action/TrainSetFrames/*/*/Extracted-Frames-1280x720/*'


import os
import glob
import numpy as np

label_files = glob.glob(os.path.join(ds_path,label_path,'*.txt'))
im_dirs = glob.glob(os.path.join(ds_path,img_paths))

labeld = {}
imd = {}

for f in label_files:
    labeld[os.path.basename(f)[:-4]] = {'label_path':f}
for d in im_dirs:
    imd[os.path.basename(d)] = {'im_path':d}

assert len(imd) == len(labeld)

print(label_files)

framec = 0



for lf in labeld:
    with open(labeld[lf]['label_path'],'rt') as f:
        lfl = f.read().splitlines()
        data = np.zeros([len(lfl),9], dtype=int)
        labels = np.zeros([len(lfl),3], dtype=str)
        for i,l in enumerate(lfl):
            v = l.split(' ')
            v[:9] = [int(vv) for vv in v[:9]]
            if len(v) <= 11:
                v = v + ['']
            v[9:] = v[9].replace('"',''), v[10].replace('"',''), v[11].replace('"','')
            data[i,:] = v[:9]
            labels[i,:] = v[9:]
    print('read '+lf)
    for imi in np.unique(data[:,5]):
        imp = os.path.join(imd[lf]['im_path'], str(imi) + '.jpg')
        