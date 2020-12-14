#!/usr/bin/python3
#           "Extensions converting"
import os
from pathlib import Path
path2 = './pictures'
for i in range(4):
    file_name = "picture{}.jpg"
    open(os.path.join(path2, file_name.format(i)), 'a').close()
files = os.listdir(path2)
print(files)
for file in files:
    full_path2 = Path(os.path.join(path2, file))
    full_path2.rename(full_path2.with_suffix('.png'))
files = os.listdir(path2)
print(files)
