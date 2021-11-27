import cv2
from cv2utils.args import make_parser
from cv2utils.camera import make_camera_with_args

def prepare(frame):
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame = cv2.GaussianBlur(frame, (21, 21), 0)
    return frame


def preprocess(frames, raw):
    diff = cv2.absdiff(frames[0], frames[1])
    diff[diff <= thresh] = 0
    diff[diff > thresh] = 1
    return cv2.add(cv2.cvtColor(diff, cv2.COLOR_GRAY2BGR) * raw, raw)


parser = make_parser()
parser.add_argument(
    "-t",
    "--threshold",
    type=int,
    default=15,
    help="The threshold for the glow effect on motion",
)
camera, args = make_camera_with_args(parser=parser, log=False, fps=15, res=(1280, 720))
thresh = args.threshold
camera.stream(prepare=prepare, preprocess=preprocess, frames_stored=2)
