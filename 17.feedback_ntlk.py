
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk
def preprocess_text(text):
    text = text.lower().translate(str.maketrans('', '', string.punctuation))
    words = word_tokenize(text)
    return [word for word in words if word not in stopwords.words('english')]

def analyze_feedback(file_path, top_n):
    df = pd.read_csv(file_path)
    all_feedback = ' '.join(df['feedback'].dropna())
    processed_words = preprocess_text(all_feedback)
    word_freq = Counter(processed_words).most_common(top_n)
    
    print(f"Top {top_n} most frequent words:")
    for word, freq in word_freq:
        print(f"{word}: {freq}")
    
    plt.bar(*zip(*word_freq))
    plt.title(f"Top {top_n} Most Frequent Words")
    plt.xlabel("Words")
    plt.ylabel("Frequency")
    plt.xticks(rotation=45)
    plt.show()

if __name__ == "__main__":
    analyze_feedback('feedback.csv', int(input("Enter the number of top frequent words to display: ")))
