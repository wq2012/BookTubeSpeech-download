# BookTubeSpeech-download

![Python application](https://github.com/wq2012/BookTubeSpeech-download/workflows/Python%20application/badge.svg)

This is a script that downloads the WAV files of the
[BookTubeSpeech](https://users.wpi.edu/~jrwhitehill/BookTubeSpeech/index.html)
dataset.

## Requirements
* Install pytube3: `pip3 install pytube3 --upgrade`
* You must have `ffmpeg` to convert mp4 to wav
* You must have `sox` to downsample the wav file

## Example usage

```
python3 download_data.py --output_dir=/path_to_download_dir
```

## Notes

Some videos may have become unavailable since the publication of the [original paper](https://users.wpi.edu/~jrwhitehill/PhamLiWhitehill_ICASSP2020.pdf), e.g. deleted by the creator.

As of 2020.04.20, this script can download 8021 (out of 8450) WAV files successfully.