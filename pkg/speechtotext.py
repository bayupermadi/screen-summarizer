import speech_recognition as sr
from pkg import videotoaudio
from pydub import AudioSegment
from pydub.utils import make_chunks
import whisper

def transcribe(audio_file, lang):
    # recognizer = sr.Recognizer()
    audio_wav = videotoaudio.convert_mp3_to_wav(audio_file)
    # audio = AudioSegment.from_wav(audio_wav)
    # chunk_length_ms = 60000  # 1 menit per potongan
    # chunks = make_chunks(audio, chunk_length_ms)

    # for i, chunk in enumerate(chunks):
    #     chunk_name = f"chunk_{i}.wav"
    #     chunk.export(chunk_name, format="wav")
    #     print(f"Exported {chunk_name}")

    #     with sr.AudioFile(chunk_name) as source:
    #         audio = recognizer.record(source)
    #         text = recognizer.recognize_google(chunk_name, language=lang)
    #         return text

    # Load Whisper model
    model = whisper.load_model("base")  # Anda bisa pakai "tiny", "small", "medium", atau "large"

    # Transcribe audio file
    result = model.transcribe(audio_wav, language=lang)
    print("Transkripsi Bahasa Indonesia:")
    print(result["text"])
