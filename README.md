# Data creation for Deep Image Matting

The purpose of the content of this repository is to easily prepare the data to train the [Deep Image Matting Network](https://github.com/Joker316701882/Deep-Image-Matting) coded by Ge Zheng. The main class (DataCreation2.py) uses the [SURREAL Database](https://github.com/gulvarol/surreal) for the EPS and alpha images, and an [Unannotated Database](http://host.robots.ox.ac.uk/pascal/VOC/databases.html#VOC2006) for the backgrounds. However, I have created classes for the main tasks, so you would just need to use `PaddingBackgroundCreation.py` someone would want to use other sources.

Deep Image Matting paper [here](https://arxiv.org/pdf/1703.03872.pdf)


## How to run it

Just run python in the commandline and use the code below. Don't forget to change the folders directory.

```python

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
```

## How it works

There's 4 files that will do the trick.

`DataCreation2.py` is the main file for generating the data from the SURREAL database.

`MatExtractor.py` extracts the alpha images from the segm.mat files. Each segm.mat file has a whole lot of alphas

`VidMatExtractor.py` extracts the correspondig alpha and eps from the segm.mat and .mp4 files.

`PaddingBackgroundCreation.py` creates the 3 necesary images for training our model (eps, alpha, bg). NOTE: the parameter num_bgs referes to how many backgrounds we are going to use for each  eps image. So it randomnly samples num_bgs images from the BG_DIR and combine them with the alpha and eps images. Therefore, if we use `num_bgs=100` for each `eps`/`alpha` image we are going to have 100 images.

## Folders Structure

The SURREAL Folder Structure is as follow, but the code above just works at level 4 (run0, run1, etc) and uses the mp4 and segm.mat files.

```
.
└── data
    ├── cmu
    │   ├── test
    │   │   ├── run0
    │   │   │   ├── 40_06_c0001_depth.mat
    │   │   │   ├── 40_06_c0001_info.mat
    │   │   │   ├── 40_06_c0001.mp4
    │   │   │   ├── 40_06_c0001_segm.mat
    │   │   │   ├── 40_06_c0002_depth.mat
    │   │   │   ├── 40_06_c0002_info.mat
    │   │   │   ├── 40_06_c0002.mp4
    │   │   │   ├── 40_06_c0002_segm.mat
    │   │   │   ├── 40_06_c0003_depth.mat
    │   │   │   ├── 40_06_c0003_info.mat
    │   │   │   ├── 40_06_c0003.mp4
    │   │   │   └── 40_06_c0003_segm.mat
    │   │   ├── run1
    │   │   └── run2
    │   └── train
    │       ├── run0
    │       ├── run1
    │       └── run2
    └── h36m
        ├── test
        │   ├── run0
        │   ├── run1
        │   └── run2
        └── train
            ├── run0
            ├── run1
            └── run2
```

The backgrounds folder just contain all the possible backgrounds to be used in our training

```
.
├── 983
├── 984
├── 985
├── 986
├── 987
├── 988
├── 989
├── 99
├── 990
├── 991
├── 992
├── 993
├── 994
├── 995
├── 996
├── 997
├── 998
└── 999
```

The output directory generates the structure shown below:

```
.
├── alpha1280
│   ├── 0 # folder for alpha image 0
│   │   ├── 0.png # alpha image 0 with background 0
│   │   ├── 1.png # alpha image 0 with background 1
│   │   ├── 2.png # alpha image 0 with background 2
│   │   ├── 3.png # alpha image 0 with background 3
│   │   ├── 4.png # alpha image 0 with background 4
│   │
│   ├── 1 # folder for alpha image 1
│   ├── 2
│   ├── 3
│   ├── 4
│   .
│   .
│   .
│
├── bg
│   ├── 0 # backgrounds for eps/alpha image 0
│   │   ├── 0.png # background 0
│   │   ├── 1.png # background 1
│   │   ├── 2.png # background 2
│   │   ├── 3.png # background 3
│   │   ├── 4.png # background 4
│   │
│   ├── 1
│   ├── 2
│   ├── 3
│   ├── 4
│   .
│   .
│   .
│
└── eps1280
    ├── 0 # folder for eps image 0
    │   ├── 0.png # alpha image 0 with background 0
    │   ├── 1.png # alpha image 0 with background 1
    │   ├── 2.png # alpha image 0 with background 2
    │   ├── 3.png # alpha image 0 with background 3
    │   ├── 4.png # alpha image 0 with background 4
    │
    ├── 1
    ├── 2
    ├── 3
    ├── 4
    .
    .
    .
```