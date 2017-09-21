from MatExtractor import MatExtractor
from os import listdir
import copy
import cv2

"""
    Class used to load all files in the folder where exist
    the following structure of files (SURREAL database):

    01_01_c0001.mp4               01_01_c0002.mp4
    01_01_c0001_depth.mat         01_01_c0002_depth.mat
    01_01_c0001_info.mat          01_01_c0002_info.mat
    01_01_c0001_segm.mat          01_01_c0002_segm.mat
            .                             .
            .                             .
            .                             .


    Or at least has the .mp4 or seg.mat files
"""

class DataCreationSurreal(object):
  
  def __init__(self, in_path,ou_path):
    self.in_path = in_path
    self.ou_path = ou_path
    self.files = None
    self.__read_path()

  def __read_path(self):
    self.files = sorted(laistdir(self.in_path))
    files = copy.deepcopy(self.files)

    for file in files:
      if (not '.mp4' in file) and (not 'segm.mat' in file):
        self.files.remove(file)

  def create_data(self):
    i = 0

    while i<(len(self.files)-1):
      #Get video
      video = cv2.VideoCapture(self.in_path+self.files[i]) 
      #Get segments
      segments = MatExtractor(self.in_path+self.files[i+1])
      #Loop and save frames
      num_segments = len(segments.segments)
      for j in num_segments:
        ret, frame = video.read()
        segment = segmets.extract_seg(j)

      i += 2
