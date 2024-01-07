# from : https://cloud.google.com/speech-to-text/docs/transcribe-client-libraries#client-libraries-install-python
# Imports the Google Cloud client library
import os
# My api key
# os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=r"./chatgptforstt-dffc449bd3f6.json"
# lecturor api key
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=r"./extreme-window-408600-97ebc28b9082.json"

# Imports the Google Cloud client library
from google.cloud import speech

def run_quickstart() -> speech.RecognizeResponse:
    # Instantiates a client
    client = speech.SpeechClient()

    # The name of the audio file to transcribe
    gcs_uri = "gs://cloud-samples-data/speech/brooklyn_bridge.raw"

    audio = speech.RecognitionAudio(uri=gcs_uri)

    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code="en-US",
    )

    # Detects speech in the audio file
    response = client.recognize(config=config, audio=audio)

    for result in response.results:
        print(f"Transcript: {result.alternatives[0].transcript}")

if __name__ == "__main__":        
    run_quickstart()
    pass