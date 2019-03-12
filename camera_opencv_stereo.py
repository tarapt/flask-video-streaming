import cv2
import numpy as np
from base_camera import BaseCamera

def merge(left_image, right_image):
    return np.concatenate((left_image, right_image), axis=1)

class Camera(BaseCamera):
    video_source_1 = 1
    video_source_2 = 2 

    @staticmethod
    def set_video_sources(source_1, source_2):
        Camera.video_source_1 = source_1
        Camera.video_source_2 = source_2

    @staticmethod
    def frames():
        camera_1 = cv2.VideoCapture(Camera.video_source_1)
        camera_2 = cv2.VideoCapture(Camera.video_source_2)
        if not camera_1.isOpened() and camera_2.isOpened():
            raise RuntimeError('Could not start the cameras.')

        while True:
            # read current frame
            _, img_1 = camera_1.read()
            _, img_2 = camera_2.read()

            img = merge(img_1, img_2)

            # encode as a jpeg image and return it
            yield cv2.imencode('.jpg', img)[1].tobytes()
