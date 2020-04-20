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
import pytube

def main():
    """The main function."""
    parser = argparse.ArgumentParser(description="Process arguments.")
    parser.add_argument(
        "--output_dir", type=str, help="Where to store the output wav files.")
    args = parser.parse_args()

    video_list = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        "BookTubeSpeechURLs.json")
    with open(video_list) as list_file:
        video_ids = json.loads(list_file.read())

    for i, video_id in enumerate(video_ids):
        print("==== Downloading {}/{}: {}".format(
            i+1, len(video_ids), video_id))
        target_wav = os.path.join(args.output_dir, video_id + ".wav")
        if os.path.exists(target_wav):
            print("==== Skipping existing wav for:", video_id)
            continue
        # Download MP4.
        url = "https://www.youtube.com/watch?v=" + video_id
        try:
            pytube.YouTube(url).streams.filter(
                only_audio=True, file_extension="mp4")[0].download(
                    output_path=args.output_dir, filename=video_id)
        except (pytube.exceptions.VideoUnavailable, pytube.exceptions.RegexMatchError):
            print("==== Skipping unavailable video:", video_id)
            continue
        # MP4 to WAV conversion.
        subprocess.check_call([
            "ffmpeg",
            "-i",
            os.path.join(args.output_dir, video_id + ".mp4"),
            os.path.join(args.output_dir, video_id + "_temp.wav"),
        ])
        # Downsample to 16kHz, and keep only the first channel.
        temp_wav = os.path.join(args.output_dir, video_id + "_temp.wav")
        subprocess.check_call([
            "sox",
            "-r",
            "16000",
            "-b",
            "16",
            "-e",
            "signed-integer",
            temp_wav,
            target_wav,
            "remix",
            "1",
        ])
        # Clean up.
        subprocess.check_call([
            "rm",
            os.path.join(args.output_dir, video_id + ".mp4"),
            temp_wav,
        ])


if __name__ == "__main__":
    main()
