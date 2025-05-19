import speech_recognition as sr

class SpeechToText:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def transcribe(self, file_path):
        with sr.AudioFile(file_path) as source:
            audio_data = self.recognizer.record(source)
            return self.recognizer.recognize_google(audio_data)
