from PIL import Image
import numpy as np
import pandas as pd

img = Image.open('test.png')
thresh = 200
fn = lambda x : 255 if x > thresh else 0
r = img.convert('L').point(fn, mode='1')
r.save('test_converted.png')

im = Image.open('test_converted.png')
im2arr = np.array(im) # im2arr.shape: height x width x channel

df = pd.DataFrame(im2arr)
df = (df == False)
coordinates = [(x,y) for x,y in zip(*np.nonzero(df.values))]
