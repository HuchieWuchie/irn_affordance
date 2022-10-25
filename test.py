import numpy as np

a = np.load("voc12/cls_labels.npy", allow_pickle=True)

#print(a)
print(a[()][2010002988])
print(a.dtype)
print(type(a))