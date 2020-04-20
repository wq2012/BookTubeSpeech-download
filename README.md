# BlueTubeSpeech downloader

This is a script that downloads the WAV files of the
[BlueTubeSpeech](https://users.wpi.edu/~jrwhitehill/BookTubeSpeech/index.html)
dataset.

## Requirements
* Install pytube3: `pip3 install pytube3 --upgrade`
* You must have `ffmpeg` to convert mp4 to wav
* You must have `sox` to downsample the wav file

## Example usage

```
python3 download_data.py --output_dir=/path_to_download_dir
```
