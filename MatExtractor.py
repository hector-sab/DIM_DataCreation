"""
    Extract single segment images from .mat files found in
    the surreal database.

"""
import scipy.io

class MatExtractor(object):
  """
      path: is the full path where the .mat file is located
      self.segments: Contains a list of the segments names
  """
  def __init__(self, path):
    #super(MatExtractor, self).__init__()
    #self.arg = arg
    self.path = path
    self.mat = None
    self.segments = None 
    self.avoid = ['__header__', '__version__', '__globals__']
    self.__load_mat()


  def __load_mat(self):
    """
        Pseudo private class.... called 'name mangling'
        Loads the segmentation mat file of SURREAL database
    """
    print(self.path)
    self.mat = scipy.io.loadmat(self.path)
    self.segments = list(self.mat.keys())
    for dropped in self.avoid:
      self.segments.remove(dropped)

  def extract_seg(self,index):
    """
        index: A number from 0 to n
    """
    index +=1
    name = 'segm_'+str(index)
    return(self.mat[name])