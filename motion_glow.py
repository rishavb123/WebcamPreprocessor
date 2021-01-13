import cv2

from cv2utils.camera import make_camera_with_args

thresh = 5

def prepare(frame):
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame = cv2.GaussianBlur(frame, (21, 21), 0)
    return frame

def preprocess(frames, raw):
    img = frames[1]
    diff = cv2.absdiff(frames[0], frames[1])
    diff[diff <= thresh] = 0
    diff[diff > thresh] = 1
    return cv2.add(cv2.cvtColor(diff, cv2.COLOR_GRAY2BGR) * raw, raw)

camera, args = make_camera_with_args(log=False, fps=15, res=(1280, 720))
camera.make_virtual_webcam(
    prepare=prepare,
    preprocess=preprocess,
    frames_stored=2
)