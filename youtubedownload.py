# -*- coding: utf-8 -*-
"""Untitled83.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LMRghmP6263uprGkt8jZtKDK6kqzX1Ot
"""

video_url = input('Enter url: ')

# Create an instance of YouTube video
video_instance = pytube.YouTube(video_url)

stream = video_instance.streams.get_highest_resolution()

# download 🚀
stream.download()

import pytube

# Replace 'video_url' with your YouTube video URL
video_url = "https://www.youtube.com/watch?v=2BcU_Dac4EY"

# Create an instance of YouTube video
video_instance = pytube.YouTube(video_url)

# Get the highest resolution stream
stream = video_instance.streams.get_highest_resolution()

# Download the video
stream.download()

!pip install pytube