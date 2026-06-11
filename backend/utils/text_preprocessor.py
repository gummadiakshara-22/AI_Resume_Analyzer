import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import re
# Run once
nltk.download("stopwords")
nltk.download("wordnet")
nltk.download("omw-1.4")

stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()


def clean_text(text):

    text = text.lower()

    # Remove email
    text = re.sub(r'\S+@\S+', ' ', text)

    # Remove urls
    text = re.sub(r'http\S+|www\S+', ' ', text)

    # Remove phone numbers
    text = re.sub(r'\b\d{10,15}\b', ' ', text)

    # Remove special chars
    text = re.sub(r'[^a-z0-9\s]', ' ', text)

    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text).strip()

    words = []

    for word in text.split():

        if word not in stop_words:

            # Lemmatization
            word = lemmatizer.lemmatize(word)

            words.append(word)

    return " ".join(words)
