import sys
from util import *
import cv2 as cv
import numpy as np
from optical_flow import OpticalFlow

# Process videos into rgb frame files and optical flow files
# The file format is numpy.array
def main(argv):
    # Check
    if len(argv) > 1:
        if argv[1] != "confirm":
            print("Must confirm by running: python process_videos.py confirm")
            return
    else:
        print("Must confirm by running: python process_videos.py confirm")
        return

    op = OpticalFlow()

    rgb_dir = "../data/rgb/"
    flow_dir = "../data/flow/"
    metadata_path = "../data/metadata.json"
    video_dir = "../data/videos/"

    # Check for saving directories and create if they don't exist
    check_and_create_dir(rgb_dir)
    check_and_create_dir(flow_dir)

    # TODO: load video metadata from ../data/metadata.json
    metadata = load_json(metadata_path)

    # TODO: loop through the metadata to get the file_name
    for video_data in metadata:
        file_name = video_data["file_name"]
        # TODO: Skip this file if ../data/frames/[file_name].npy and ../data/flows/[file_name].npy both exist
        # TODO: for example: if is_file_here(file_path): continue
        if is_file_here(rgb_dir + file_name + ".npy") and is_file_here(flow_dir + file_name + ".npy"): continue
        # TODO: load videos from ../data/videos/[file_name].mp4
        video = str(video_dir + file_name + ".mp4")
        # TODO: process them into rgb frames and optical flows
        rgb_4d_out_p = str(rgb_dir + file_name)
        flow_4d_out_p = str(flow_dir + file_name)
        # TODO: save rgb frames to ../data/frames/[file_name].npy
        # TODO: save optical flows to ../data/flows/[file_name].npy
        op.step(rgb_vid_in_p=video, rgb_4d_out_p=rgb_4d_out_p, flow_4d_out_p=flow_4d_out_p)


if __name__ == "__main__":
    main(sys.argv)