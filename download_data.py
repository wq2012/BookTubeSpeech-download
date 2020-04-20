"""A script to download the WAV files of BookTubeSpeech.

Example usage:
    python3 download_data.py --output_dir=/path_to_download_dir

BookTubeSpeech website:
    https://users.wpi.edu/~jrwhitehill/BookTubeSpeech/index.html

Requirements:
    Install pytube3: pip3 install pytube3 --upgrade
    You must have ffmpeg to convert mp4 to wav
    You must have sox to downsample the wav file
"""
import argparse
import json
import os
import subprocess
from pytube import YouTube


parser = argparse.ArgumentParser(description="Process arguments.")
parser.add_argument(
    "--output_dir", type=str, help="Where to store the output wav files.")
args = parser.parse_args()

video_list = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    "BookTubeSpeechURLs.json")
with open(video_list) as f:
    video_ids = json.loads(f.read())

for video_id in video_ids:
    url = "https://www.youtube.com/watch?v=" + video_id
    YouTube(url).streams.filter(
        only_audio=True, file_extension="mp4")[0].download(
            output_path=args.output_dir, filename=video_id)
    # mp4 to wav conversion
    subprocess.check_call([
        "ffmpeg",
        "-i",
        os.path.join(args.output_dir, video_id + ".mp4"),
        os.path.join(args.output_dir, video_id + "_temp.wav"),
    ])
    # downsample to 16kHz, and keep only the first channel
    subprocess.check_call([
        "sox",
        "-r",
        "16000",
        "-b",
        "16",
        "-e",
        "signed-integer",
        os.path.join(args.output_dir, video_id + "_temp.wav"),
        os.path.join(args.output_dir, video_id + ".wav"),
        "remix",
        "1",
    ])
    subprocess.check_call([
        "rm",
        os.path.join(args.output_dir, video_id + ".mp4"),
        os.path.join(args.output_dir, video_id + "_temp.wav")
    ])
