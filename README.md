# Data creation for Deep Image Matting

The purpose of the content of this repository is to easily prepare the data to train the [Deep Image Matting Network](https://github.com/Joker316701882/Deep-Image-Matting) coded by Ge Zheng. The main class (DataCreation2.py) uses the [SURREAL Database](https://github.com/gulvarol/surreal) for the EPS and alpha images, and an [Unannotated Database](http://host.robots.ox.ac.uk/pascal/VOC/databases.html#VOC2006) for the backgrounds. However, I have created classes for the main tasks, so it could be relatively easy to prepare data from other sources.

Deep Image Matting paper [here](https://arxiv.org/pdf/1703.03872.pdf)


## How it works

Just run python in the commandline and use the following code:

'''python

from DataCreation2 import DataCreation

# Folder where the surreal data is located
SUR_DATA_DIR = '/data/DataBases/SURREAL/SURREAL/data/cmu/train/run0/01_01'

# Output Directory
OUT_DIR = '/data/HectorSanchez/Deep-Image-Matting/data/'

# Backgrounds 
BG_DIR = '/data/HectorSanchez/Deep-Image-Matting/backgrounds/'

for folder in folders:
  print('folder '+folder)
  create = DataCreation(ipath=SUR_DATA_DIR, opath=OUT_DIR, bg_path=BG_DIR)
  create.create_data()
´´´

## SURREAL DataSet Folder Structure


