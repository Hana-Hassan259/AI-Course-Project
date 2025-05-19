import spacy
from sklearn.feature_extraction.text import TfidfVectorizer

class KeywordOptimizer:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")

    def extract_keywords(self, text, top_n=10):
        vectorizer = TfidfVectorizer(stop_words='english')
        tfidf_matrix = vectorizer.fit_transform([text])
        scores = zip(vectorizer.get_feature_names_out(), tfidf_matrix.toarray()[0])
        sorted_keywords = sorted(scores, key=lambda x: -x[1])
        return sorted_keywords[:top_n]
