import cv2
from cv2utils.args import make_parser
from cv2utils.camera import make_camera_with_args


def prepare(frame):
    frame = cv2.GaussianBlur(frame, (21, 21), 0)
    return frame


def preprocess(frames, raw):
    # temp = cv2.addWeighted(frames[len(frames) // 2], 0.5, frames[-1], 0.5, 0)
    # return cv2.addWeighted(temp, 0.6, raw, 0.4, 0)
    img = raw
    get_ind = lambda i: total_frames - (i + 1) * len(frames) // echos
    for i in range(echos - 1):
        ind = get_ind(i)
        img = cv2.addWeighted(img, 0.7, frames[ind], 0.3, 0)
    return cv2.addWeighted(img, 0.9, raw, 0.1, 0)



parser = make_parser()
parser.add_argument(
    "-e",
    "--echos",
    type=int,
    default=2,
    help="The number of echos"
)
parser.add_argument(
    "-tf",
    "--total-frames",
    type=int,
    default=100,
    help="The total number of frames stored for the echos"
)
camera, args = make_camera_with_args(parser=parser, log=False, fps=15, res=(1280, 720))
total_frames = args.total_frames
echos = args.echos
camera.make_virtual_webcam(prepare=prepare, preprocess=preprocess, frames_stored=args.total_frames)
