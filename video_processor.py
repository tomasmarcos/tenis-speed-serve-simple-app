import cv2
import PIL


def invert_colors(image_array):
  """
  Convert image_array from BGR to RGB or the other way.
  """
  # same as img = img[:, :, [2,1,0]
  return image_array[:,:,::-1]

def preprocess_frame(frame, rotate_180degrees, reverse_colors):
  """
  Apply preprocessing pipeline to a frame.
  Parameters
    frame: image/frame into np.ndarray format
    rotate_180degrees: bool, perform 180degree rotation
    invert_colors: bool, invert colors (ie from bgr to rgb)
  Returns:
    frame preprocessed
  """
  if rotate_180degrees:
    frame = cv2.rotate(frame, cv2.ROTATE_180)
  if reverse_colors:
    frame = invert_colors(frame)
  return frame

def video_to_frames(video_path, preprocessing_func):
  """
  Convert a video to a sequence of frames
  """
  print("[WARNING] Consider using yield instead of return to not overload memory")
  print("[INFO] Video path is:",video_path)
  cap = cv2.VideoCapture(video_path)
  n_frames_metadata = int( cap.get(cv2.CAP_PROP_FRAME_COUNT) )
  fps = int( cap.get(cv2.CAP_PROP_FPS))
  frames_prep_list = list()
  ret, frame = cap.read()
  while ret:
    height,width, channels = frame.shape
    frame_prep = preprocessing_func(frame)
    frames_prep_list.append(frame_prep)
    ret, frame = cap.read()
  return {"frames_prep_list":frames_prep_list, "n_frames_metadata":n_frames_metadata,"fps":fps}



preprocessing_frame_pipe = lambda frame: preprocess_frame(frame,
                                                          rotate_180degrees = False,
                                                          reverse_colors = True )









