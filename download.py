import streamlit as st
import os

def download_video(video_url):
    # Command to download the video using youtube-dl
    command = f'youtube-dl {video_url}'
    os.system(command)

# Streamlit app layout
st.title('Video Downloader')

# Input field for video URL
video_url = st.text_input("Enter the video URL:")

# Button to trigger download
if st.button('Download Video'):
    if video_url:
        download_video(video_url)
        st.success("Video is being downloaded!")
    else:
        st.error("Please enter a valid URL.")
