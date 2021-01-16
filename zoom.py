import argparse
import cv2
from cv2utils.args import make_parser
from cv2utils.camera import make_camera_with_args


def prepare(frame):
    return frame


def preprocess(frames, raw):
    img = raw
    h, w, c = img.shape
    img = img[py:py+ph, px:px+pw]
    return cv2.resize(img, (w, h))


def pos_type(s):
    try:
        a = [float(n) for n in s[1:-1].split(",")]
        assert len(a) == 4
        return tuple(a)
    except:
        raise argparse.ArgumentTypeError("Must format position as (x,y,w,h). Remember no spaces!")


parser = make_parser()
parser.add_argument(
    "-p",
    "--pos",
    type=pos_type,
    default=(0, 0, 1, 1),
    help="The position to use in the format: (x,y,w,h)"
)

camera, args = make_camera_with_args(parser=parser)
pos = args.pos
w, h = camera.get_res()
pix_pos = (int(pos[0] * w), int(pos[1] * h), int(pos[2] * w), int(pos[3] * h))
px, py, pw, ph = pix_pos
webcam_res = (pix_pos[2], pix_pos[3])
camera.make_virtual_webcam(prepare=prepare, preprocess=preprocess, frames_stored=1, webcam_res=webcam_res)
