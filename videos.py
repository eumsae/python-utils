import os

import cv2
import numpy as np


def get_frames(video:str, stt_i:int=0, end_i:int=-1, step:int=1):
    cap = cv2.VideoCapture(video)
    cap.set(cv2.CAP_PROP_POS_FRAMES, stt_i)

    n_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    if end_i == -1:
        end_i = n_frames - 1

    if stt_i < 0 and n_frames -1 < stt_i:
        raise ValueError("stt_i < 0 or stt_i > n_frames -1")
    if end_i < 0 and n_frames -1 < end_i:
        raise ValueError("end_i < 0 or end_i > n_frames -1")
    if stt_i > end_i:
        raise ValueError("stt_i > end_i")

    for i in range(stt_i, end_i, step):
        ret, frame = cap.read()
        if not ret:
            cap.release()
            break
        yield i, frame
