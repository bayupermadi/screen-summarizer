from pkg import videotoaudio, awstranscribe, config as cf
import argparse

# Create an ArgumentParser object
parser = argparse.ArgumentParser(description="Specify the video sources")

# Add arguments
parser.add_argument("--video", help="Sources of screen record to summary")
parser.add_argument("--config", help = "Target config file")

# Parse the arguments
args = parser.parse_args()

# Load config file
config = cf.getConfig(args.config)

def main():
    audio_file = videotoaudio.convert_video_to_mp3(args.video)
    if audio_file:
        print(audio_file)
    print(config['s3_bucket'])
    # file_uri = "s3://test-transcribe/answer2.wav"
    # awstranscribe.transcribe_file("Example-job", file_uri)


if __name__ == "__main__":
    main()