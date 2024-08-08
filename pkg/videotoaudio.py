from moviepy.editor import *
import uuid

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