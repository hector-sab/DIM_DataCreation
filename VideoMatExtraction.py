from MatExtractor import MatExtractor
import cv2

#Workaround for video 
import imageio

class VideoMatExtraction(object):
  """
    mat_file: path of where to find the mat file containing segmentations
    vid_file: path of where to find the original video file
  """
  def __init__(self, mat_file, vid_file):
    self.mat_path = mat_file
    self.vid_path = vid_file
    self.mat = None
    self.vid = None
    self.num_segments = None

    self.__load_files()

    self.frames = []
    self.segments = []

  def __load_files(self):
    self.mat = MatExtractor(self.mat_path)
    #self.vid = cv2.VideoCapture(self.vid_path)
    self.vid = imageio.get_reader(self.vid_path, 'ffmpeg')
    self.num_segments = len(self.mat.segments)

  def extract(self):
    """
      Returns two elements: A list containing the frames, and
      a list containing the segments in np arrays.
    """
    for i in range(self.num_segments):
      #ret, frame = self.vid.read()
      frame = self.vid.get_data(i)
      segment = self.mat.extract_seg(i)

      self.frames.append(frame)
      self.segments.append(segment)

    return(self.frames, self.segments)