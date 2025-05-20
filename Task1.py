from transformers import pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import defaultdict
import spacy
import nltk
import os

print("Initializing...")

# Downloading necessary NLTK data if not already present
nltk.download('stopwords')
nltk.download('punkt')

# Load spacy for Named Entity Recognition
try:
    nlp_spacy = spacy.load("en_core_web_sm")
except OSError:
    print("Downloading en_core_web_sm model for spaCy...")
    spacy.cli.download("en_core_web_sm")
    nlp_spacy = spacy.load("en_core_web_sm")

# Initializing pegasus summarizer model
summarizer = pipeline("summarization", model="google/pegasus-cnn_dailymail")

# Function to extract keywords
def extract_keywords_tfidf(text, top_n=7):
    stop_words = set(stopwords.words('english'))
    def preprocess_for_tfidf(t):
        words = word_tokenize(t.lower())
        return [word for word in words if word.isalnum() and word not in stop_words]

    vectorizer = TfidfVectorizer(tokenizer=preprocess_for_tfidf,token_pattern=None)
    tfidf_matrix = vectorizer.fit_transform([text])
    feature_names = vectorizer.get_feature_names_out()

    word_scores = defaultdict(float)
    for col in tfidf_matrix.nonzero()[1]:
        word = feature_names[col]
        word_scores[word] = tfidf_matrix[0, col]

    sorted_keywords = sorted(word_scores.items(), key=lambda item: item[1], reverse=True)
    return [keyword for keyword, score in sorted_keywords[:top_n]]

# Function to extract unique named entities
def extract_named_entities_spacy(text):
    doc = nlp_spacy(text)
    entities = list(set([ent.text for ent in doc.ents]))
    return entities

# Taking user input for article
os.system("clear || cls")
long_article = str(input("Enter Article to summerize : "))

# Preprocessing the text for model
keywords = extract_keywords_tfidf(long_article)
entities = extract_named_entities_spacy(long_article)
enhanced_input_prefix = ""
if keywords:
    enhanced_input_prefix += f"Keywords: {', '.join(keywords)}. "
if entities:
    enhanced_input_prefix += f"Entities: {', '.join(entities)}. "
input_for_pegasus = enhanced_input_prefix + long_article

# Generating the summary with PEGASUS model
try:
    summary = summarizer(input_for_pegasus, max_length=200, min_length=50, num_beams=8, early_stopping=False)[0]['summary_text']
except Exception as e:
    print( f"An error occurred: {e}")
    exit()
final_summary = summary.replace(" .<n>",". ")

# Final Result
print("\nConcise Summary:\n", final_summary)
