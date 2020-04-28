###############################################################################
# N.Kozak // Lviv'2020 // ACM // OpenCV faces detection use example by Python #
#    file: acmhw22.py (renamed to main.py)                                    #
###############################################################################
import sys
import cv2 as cv

# to implement a constant in Python
class CONSTANT(object): 
    def __init__(self, CONSTANT): self._CONSTANT = CONSTANT
    @property 
    def CONSTANT(self): return self._CONSTANT

#MAX_FACES_COUNT.CONSTANT - constant value
MAX_FACES_COUNT = CONSTANT(24) 

#PROCESSING_IMAGE_FROM_FILE.CONSTANT - constant value
PROCESSING_IMAGE_FROM_FILE = CONSTANT(True)

def detectFaces(image, face_cascade):
  face_cascade.load('haarcascade_frontalface_alt.xml');
  faces = face_cascade.detectMultiScale(image, 1.1, 2, 0 | cv.CASCADE_SCALE_IMAGE, (30, 30));
  for (x, y, width, height) in faces[0:min(len(faces), MAX_FACES_COUNT.CONSTANT)]:
    image = cv.ellipse(
      image, 
      (x + width // 2, y + height // 2), 
      (width // 2, height // 2), 
      0, 
      0, 
      360, 
      (255, 0, 255), 
      4, 
      8,
      0
    )   
  pass

face_cascade = cv.CascadeClassifier();
if not face_cascade.load('haarcascade_frontalface_alt.xml'):
    print("Could not open haarcascade_frontalface_alt.xml");
    print("Copy this file and try again");
    sys.exit(-1);

if PROCESSING_IMAGE_FROM_FILE.CONSTANT == True:
    image = cv.imread("image.jpg");
    if (image is None) :
        print("Could not open or find the image")
        print("Copy the image file and try again")
        sys.exit(-1);   
        
    detectFaces(image, face_cascade)
	
	#cv.imshow("Detected Face", image);    
    cv.imwrite("image_out.jpg", image);
else:
  cap = cv.VideoCapture(0)
  while True:
    _, image = cap.read()
    detectFaces(image, face_cascade, faces)
    cv.imshow("Detected Face", image);
    cv.waitKey(1);	
#sys.exit();	