# https://cloud.google.com/text-to-speech/docs/samples/tts-synthesize-text?hl=ko
# ~% pip install google-cloud-texttospeech
import os
# My api key
# os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=r"./chatgptforstt-dffc449bd3f6.json"
# lecturor api key
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=r"./extreme-window-408600-97ebc28b9082.json"

def synthesize_text(text):
    """Synthesizes speech from the input string of text."""
    from google.cloud import texttospeech

    client = texttospeech.TextToSpeechClient()

    input_text = texttospeech.SynthesisInput(text=text)

    # Note: the voice can also be specified by name.
    # Names of voices can be retrieved with client.list_voices().
    voice = texttospeech.VoiceSelectionParams(
        # language_code="en-US",
        # name="en-US-Standard-C",
        language_code="ko-KR",
        # name="ko-KR-Standard-A",
        name="ko-KR-Standard-C",
        ssml_gender=texttospeech.SsmlVoiceGender.FEMALE,
    )

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    response = client.synthesize_speech(
        request={"input": input_text, "voice": voice, "audio_config": audio_config}
    )

    # The response's audio_content is binary.
    with open("output.mp3", "wb") as out:
        out.write(response.audio_content)
        print('Audio content written to file "output.mp3"')

if __name__ == "__main__":
    input_text = "Hello, world"
    input_text = 'Special education for training teachers/instructors in the field of continuing education (first round in 2024)'
    # input_text = "훈련 교/강사 보수교육 전공분야 특별교육 (2024년 1차)"
    synthesize_text(input_text)