from moviepy.editor import *
import uuid
import subprocess
import os

def convert_video_to_mp3(video_file_path):
    output_file = "{}.mp3".format(uuid.uuid4())
    try:
        # Load the video file
        video = VideoFileClip(video_file_path)
        
        # Extract the audio
        audio = video.audio
        
        # Write the audio to an mp3 file
        audio.write_audiofile(output_file)
        return output_file
        
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
    
def convert_mp3_to_wav(input_file):
    output_file = "{}.wav".format(uuid.uuid4())
    try:
        # Run the ffmpeg command
        subprocess.run(['ffmpeg', '-i', input_file, '-acodec', 'pcm_s16le', '-ar', '16000', output_file], check=True)
        print(f"Conversion successful: {output_file}")
        return output_file
    except subprocess.CalledProcessError as e:
        print(f"Error during conversion: {e}")
    except FileNotFoundError:
        print("Error: ffmpeg is not installed or not found in the system PATH.")