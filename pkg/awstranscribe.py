import time
import boto3
import uuid
import requests

def transcribe_file(file_uri):
    job_name = "job-{}".format(uuid.uuid4())
    transcribe_client = boto3.client("transcribe")
    transcribe_client.start_transcription_job(
        TranscriptionJobName=job_name,
        Media={"MediaFileUri": file_uri},
        MediaFormat="wav",
        LanguageCode="en-US",
        Settings= {
            'ShowSpeakerLabels': True,
            'MaxSpeakerLabels': 30
        },
    )

    max_tries = 60
    while max_tries > 0:
        max_tries -= 1
        job = transcribe_client.get_transcription_job(TranscriptionJobName=job_name)
        job_status = job["TranscriptionJob"]["TranscriptionJobStatus"]
        if job_status in ["COMPLETED", "FAILED"]:
            print(f"Job {job_name} is {job_status}.")
            if job_status == "COMPLETED":
                downloadLink = job['TranscriptionJob']['Transcript']['TranscriptFileUri']
                return downloadLink
            break
        else:
            print(f"Waiting for {job_name}. Current status is {job_status}.")
        time.sleep(10)

def download_tr_file(url):
    file_tr = "tr-{}.json".format(uuid.uuid4())
    response = requests.get(url)
    with open(file_tr, mode="wb") as file:
        file.write(response.content)

    return file_tr




