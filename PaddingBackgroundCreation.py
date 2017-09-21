import os
import cv2
import random
import numpy as np

class PaddingBackgroundCreation(object):
  """
    Generates all the padding images with respect background
  """
  def __init__(self, bgs_path, save_paths, img, alpha, num_bgs=100):
    """
      save_paths: a list of where are we going to save all three images. I.E. [eps_path,alpha_path,bg_path]
      alpha: matted image
      img: original image
      bgs_path: path where all background images are found
      num_bgs: number of backgrounds to be used for  a image
    """
    self.eps_save_path = save_paths[0]
    if self.eps_save_path[-1]!='/':
      self.eps_save_path = self.eps_save_path+'/'

    self.alpha_save_path = save_paths[1]
    if self.alpha_save_path[-1]!='/':
      self.alpha_save_path = self.alpha_save_path+'/'

    self.bg_save_path = save_paths[2] # Where are we going to save the backgrounds
    if self.bg_save_path[-1]!='/':
      self.bg_save_path = self.bg_save_path+'/'

    self.num_bgs = num_bgs #Number of backgrounds to be use in the generation
    self.bgs_path = bgs_path
    if self.bgs_path[-1]!='/':
      self.bgs_path = self.bgs_path+'/'
    self.bgs = None # list of all background files
    self.__read_bg()
    self.eps = img
    self.alpha = alpha

  def __read_bg(self):
    self.bgs = sorted(os.listdir(self.bgs_path))

  def create_data(self):
    num_bg_fls = len(self.bgs)
    assert num_bg_fls>=self.num_bgs, "Not Enough Backgrounds (%d) for %d "%(num_bg_fls,self.num_bgs)
    choosen_bgs = random.sample(range(0,num_bg_fls-1),self.num_bgs)

    for i, file in enumerate(choosen_bgs):
      background = cv2.imread(self.bgs_path+self.bgs[file])

      rows = background.shape[0]
      cols = background.shape[1]

      #Resize the shortest side to be 640
      if cols<rows:
        new_cols = 1280
        new_rows = int((rows*new_cols)/cols)
      else:
        new_rows = 1280
        new_cols = int((cols*new_rows)/rows)

      new_bg = cv2.resize(background,(new_cols, new_rows), interpolation = cv2.INTER_CUBIC)

      eps_rows = self.eps.shape[0]
      eps_cols = self.eps.shape[1]

      #Add padding to eps and alpha
      dif_rows = int((new_rows-eps_rows)/2)
      dif_cols = int((new_cols-eps_cols)/2)

      new_eps = np.zeros_like(new_bg)
      new_alpha = np.zeros((new_rows,new_cols))

      new_eps[dif_rows:dif_rows+eps_rows,dif_cols:dif_cols+eps_cols,:] = self.eps
      new_alpha[dif_rows:dif_rows+eps_rows,dif_cols:dif_cols+eps_cols] = self.alpha

      cv2.imwrite(self.eps_save_path+str(i)+'.png',new_eps)
      cv2.imwrite(self.alpha_save_path+str(i)+'.png',new_alpha)
      cv2.imwrite(self.bg_save_path+str(i)+'.png',new_bg)