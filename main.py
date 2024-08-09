from pkg import chatgpt, videotoaudio, awstranscribe, config as cf, awss3, chatgpt
import argparse
import os

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
    ## convert video to audio
    audio_file = videotoaudio.convert_video_to_mp3(args.video)

    ## push audio to S3
    if audio_file:
        if awss3.upload(audio_file, config['s3_bucket']):
            file_uri = "s3://{}/{}".format(config['s3_bucket'],audio_file)

    ## transcribe audio 
    url_tr_file = awstranscribe.transcribe_file(file_uri)
    do_tr_file = awstranscribe.download_tr_file(url_tr_file)

    # summary the trascribe to meeting minute
    summ_prepare = chatgpt.prepare(do_tr_file)
    summ_content = chatgpt.generate_meeting_minute(summ_prepare, config['openai_key'])
    chatgpt.save_to_docx(summ_content)

    ## clean the temporary file
    awss3.delete_file(audio_file, config['s3_bucket'])
    os.remove(audio_file)
    os.remove(do_tr_file)
    os.remove(summ_prepare)

if __name__ == "__main__":
    main()