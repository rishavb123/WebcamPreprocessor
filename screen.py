from cv2utils.camera import make_camera_with_args, Camera
import mss

def prepare(frame):
    h, w, _ = frame.shape

    # black out hand
    # wc = 6.5
    # hc = 7.8
    # ew = int(w*wc//10)
    # sh = int(h*hc/10)
    # frame[sh:,:ew,:] = 0

    for zone in black_out_zones:
        x, ex, y, ey = zone
        frame[int(h*y):int(h*ey), int(w*x):int(w*ex), 0:3] = 0

    return frame

# In the format [(x, endx, y, endy), ...]
black_out_zones = [
    (0, 0.65, 0.78, 1), # black out magic hand
    (-0.181, -0.015, 0.343, 0.7552)
] 

with mss.mss() as sct:
    camera, args = make_camera_with_args(video=Camera.Monitor(sct, mon=3))
    camera.make_virtual_webcam(prepare=prepare, webcam_res=(1920, 1080))

'''
4 in width, -0.375 in from right
5.5 in height, 4.6 inches from the top
24.25 inches 
13.375
'''