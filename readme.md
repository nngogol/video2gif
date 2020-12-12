## video 2 gif

### libs to install

Install ffmpeg and python:

```bash
sudo apt install gifsicle ffmpeg
python3 -m pip install click imageio tqdm scikit-image
```

### Usage

```bash
# step 1
# ... record a video ...
# Let input video will be named ifile.mkv

# step 2
# Convert ifile.mkv to jpg frames in shell, by using ffmpeg:
# $ mkdir frames
# $ ffmpeg -i video.mkv frames/%d.jpg

# step 3
# make a final gif, by using this command:
python3 video2gif.py --fps 10 "/path/to/your/folder"
