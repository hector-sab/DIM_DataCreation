# Data creation for Deep Image Matting

The purpose of the content of this repository is to easily prepare the data to train the [Deep Image Matting Network](https://github.com/Joker316701882/Deep-Image-Matting) coded by Ge Zheng. The main class (DataCreation2.py) uses the [SURREAL Database](https://github.com/gulvarol/surreal) for the EPS and alpha images, and an [Unannotated Database](http://host.robots.ox.ac.uk/pascal/VOC/databases.html#VOC2006) for the backgrounds. However, I have created classes for the main tasks, so it could be relatively easy to prepare data from other sources.

Deep Image Matting paper [here](https://arxiv.org/pdf/1703.03872.pdf)