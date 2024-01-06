# from : https://cloud.google.com/speech-to-text/docs/transcribe-client-libraries#client-libraries-install-python
# Imports the Google Cloud client library
import os
# My api key
# os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=r"./chatgptforstt-dffc449bd3f6.json"
# lecturor api key
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=r"./extreme-window-408600-97ebc28b9082.json"

# Imports the Google Cloud client library
from google.cloud import speech

def run_quickstart(file_path) -> speech.RecognizeResponse:
    # Instantiates a client
    client = speech.SpeechClient()

    # 음성 파일 열기
    with open(file_path, "rb") as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)

    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        # language_code="en-US",
        language_code="ko-KR",

    )

    # Detects speech in the audio file
    response = client.recognize(config=config, audio=audio)

    for result in response.results:
        print(f"Transcript: {result.alternatives[0].transcript}")

if __name__ == "__main__":    
    # 대상 음성 파일 경로
    file_path = "output.mp3"    
    run_quickstart(file_path)
    pass