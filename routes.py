from flask import request, jsonify, send_file
from app.modules.summarizer import Summarizer
from app.modules.generator import ContentGenerator
from app.modules.classifier import Classifier
from app.modules.keyword_optimizer import KeywordOptimizer
from app.modules.tts import TextToSpeech
from app.modules.stt import SpeechToText

def register_routes(app):
    summarizer = Summarizer()
    generator = ContentGenerator()
    classifier = Classifier()
    optimizer = KeywordOptimizer()
    tts = TextToSpeech()
    stt = SpeechToText()

    @app.route('/')
    def index():
        return send_file('frontend/index.html')

    @app.route('/summarize', methods=['POST'])
    def summarize():
        try:
            text = request.json.get('text')
            summary = summarizer.summarize(text)
            return jsonify(summary)
        except Exception as e:
            return jsonify({'error': str(e)}), 400

    @app.route('/generate', methods=['POST'])
    def generate():
        prompt = request.json.get('prompt')
        result = generator.generate(prompt)
        return jsonify(result)

    @app.route('/classify', methods=['POST'])
    def classify():
        text = request.json.get('text')
        result = classifier.classify(text)
        return jsonify(result.tolist())

    @app.route('/keywords', methods=['POST'])
    def keywords():
        text = request.json.get('text')
        result = optimizer.extract_keywords(text)
        return jsonify(result)

    @app.route('/speak', methods=['POST'])
    def speak():
        text = request.json.get('text')
        filename = tts.speak(text)
        return jsonify({"audio_file": filename})

    @app.route('/transcribe', methods=['POST'])
    def transcribe():
        if 'file' not in request.files:
            return jsonify({"error": "No file provided"}), 400
        audio_file = request.files['file']
        file_path = f"temp/{audio_file.filename}"
        audio_file.save(file_path)
        try:
            text = stt.transcribe(file_path)
            return jsonify({"transcription": text})
        except Exception as e:
            return jsonify({"error": str(e)}), 500
