import pyttsx3

class TextToSpeech:
    def __init__(self):
        self.engine = pyttsx3.init()

    def speak(self, text, filename='output_audio.wav'):
        self.engine.save_to_file(text, filename)
        self.engine.runAndWait()
        return filename
