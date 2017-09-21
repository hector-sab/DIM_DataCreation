from VideoMatExtraction import VideoMatExtraction
import os
import cv2
"""
  This version saves just the image extracted from the video and the mat files containing the segments

  Example:
  from DataCreation import DataCreation
  create = DataCreation(ipath='/data/DataBases/SURREAL/SURREAL/data/cmu/train/run0/01_01/', opath='/data/HectorSanchez/TestDC')
  create.create_data()
"""
class DataCreation(object):
  def __init__(self,ipath, opath):
    """
      ipath: path where all the SURREAL mat and mp4 files are
      opath: where the results should be saved
    """
    self.ipath = ipath
    if self.ipath[-1]!='/':
      self.ipath = self.ipath+'/'
    self.opath = opath
    if self.opath[-1]!='/':
      self.opath = self.opath+'/'
    self.videos = [] # Names of videos
    self.mats = [] #Names of mat files

    self.__read_path()

  def __read_path(self):
    """
       Read the files in the path directory, saving only those 
       being a mp4 file, or a segment mat file.
    """

    files = sorted(os.listdir(self.ipath))
    
    for file in files:
      if '.mp4' in file:
        self.videos.append(file)
      elif 'segm.mat' in file:
        self.mats.append(file)

  def create_data(self):
    #about assert https://stackoverflow.com/questions/5142418/what-is-the-use-of-assert-in-python
    num_vids = len(self.videos)
    num_segms = len(self.mats)
    ERROR_MSG = 'Number of videos is different to number of segment files:'
    assert len(self.videos)==len(self.mats), '%s %d != %d \n in folder %s'%(ERROR_MSG,num_vids,num_segms,self.ipath)

    # Checks if output dir exists
    if not os.path.exists(self.opath):
      os.makedirs(self.opath)

    for video,mat in zip(self.videos, self.mats):
      group_name = video.replace('.mp4','')
      group_dir = self.opath+group_name+'/'
      # Checks if group dir exists
      if not os.path.exists(group_dir):
        os.makedirs(group_dir)

      img_path =group_dir+'imgs/'
      seg_path = group_dir+'segs/'

      
      # Checks if final output dir exists
      if not os.path.exists(img_path):
        os.makedirs(img_path)
      if not os.path.exists(seg_path):
        os.makedirs(seg_path)

      print(self.ipath+mat)
      print(self.ipath+video)
      extract = VideoMatExtraction(mat_file=self.ipath+mat,
                                   vid_file=self.ipath+video)
      frames,segments = extract.extract()

      for i,(segment,frame) in enumerate(zip(segments,frames)):
        #Resize to width = 640
        segment = self.__adjust_size(segment)
        frame = self.__adjust_size(frame)

        alpha = self.__create_alpha(segment)

        cv2.imwrite(img_path+str(i)+'.png',frame)
        cv2.imwrite(seg_path+str(i)+'.png',alpha)

  def __create_alpha(self,segment):
    alpha = (segment>0)*255
    alpha = alpha.astype(float)
    return(alpha)

  def __adjust_size(self,img):
    """
      Adjust the image so the biggest side is 640px
    """
    rows = img.shape[0]
    cols = img.shape[1]

    if cols>rows:
      new_cols = 640
      new_rows = int((rows*new_cols)/cols)
    else:
      new_rows = 640
      new_cols = int((cols*new_rows)/rows)

    new_img = cv2.resize(img,(new_cols, new_rows), interpolation = cv2.INTER_CUBIC)

    return(new_img)

