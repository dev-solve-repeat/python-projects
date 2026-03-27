#We need to install moviepy - pip install moviepy

from moviepy import VideoFileClip, AudioFileClip

cvt_video = VideoFileClip("ACT Enterprise - Managed ILL-Video.mp4")

ext_audio = cvt_video.audio

ext_audio.write_audiofile("audio_extarcted.mp3")