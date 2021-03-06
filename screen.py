from cv2utils.args import make_parser
from cv2utils.camera import make_camera_with_args, Camera
import mss

def prepare(frame):
    h, w, _ = frame.shape

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
    parser = make_parser()
    parser.add_argument(
        "-m",
        "--monitor",
        type=int,
        default=0,
        help="The monitor index to use"
    )
    args = parser.parse_args()
    camera, args = make_camera_with_args(parser=parser, video=Camera.Monitor(sct, mon=args.monitor))
    camera.make_virtual_webcam(prepare=prepare, webcam_res=(1920, 1080))

'''
4 in width, -0.375 in from right
5.5 in height, 4.6 inches from the top
24.25 inches 
13.375
'''