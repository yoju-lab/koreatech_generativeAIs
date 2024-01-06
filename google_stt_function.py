from google.cloud import speech_v1p1beta1 as speech

def transcribe_speech(file_path):
    client = speech.SpeechClient()

    # 음성 파일 열기
    with open(file_path, "rb") as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)

    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code="ko-KR"
    )

    # 음성을 텍스트로 변환
    response = client.recognize(config=config, audio=audio)

    # 변환된 텍스트 출력
    for result in response.results:
        print("Transcript: {}".format(result.alternatives[0].transcript))

# 대상 음성 파일 경로
file_path = "./korea_voice.m4a"

# 음성 파일 변환
transcribe_speech(file_path)
