#%%
import os
import shutil
import random


# %%
import splitfolders
SOURCE_FOLDER=r"C:\Users\vivek\Desktop\down"
DEST_FOLDER = r"C:\Users\vivek\Desktop\downout"
splitfolders.ratio(SOURCE_FOLDER, output=DEST_FOLDER, seed=1337, ratio=(0.7, 0.2,0.1))
# %%
