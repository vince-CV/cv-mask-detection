import random
import os
import subprocess
import sys

# Create a txt file which contains the path to the images. 


image_dir = "C:/Users/xwen2/Google Drive/Mask Detector/data"
image_dir_save = "/content/drive/My Drive/Mask Detector"
f_val = open("C:/Users/xwen2/Google Drive/Mask Detector/data_test.txt", 'w')
f_train = open("C:/Users/xwen2/Google Drive/Mask Detector/data_train.txt", 'w')

path, dirs, files = next(os.walk(image_dir))
data_size = 0.5 * len(files)

ind = 0
data_test_size = int(0.15 * data_size)

test_array = random.sample(range(int(data_size)), k = data_test_size)

for f in os.listdir(image_dir):
    if(f.split(".")[-1] != "txt"):
        ind += 1

        print(f)
        
        if ind in test_array:
            f_val.write(image_dir_save+'/data/'+f+'\n')
        else:
            f_train.write(image_dir_save+'/data/'+f+'\n')

f_train.close()
f_val.close()