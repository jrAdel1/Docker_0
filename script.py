import nltk
from nltk.corpus import stopwords
from collections import Counter

try:
    nltk.data.find('corpora/stopwords.zip')
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('stopwords')
    nltk.download('punkt')
    
stop_words = set(stopwords.words('english'))

with open("random_paragraphs.txt", 'r') as file:
    text = file.read().lower()
# Split the text into individual words using NLTK's word tokenizer
words = nltk.word_tokenize(text)

filtered = [w for w in words if not w in ["(", ")", ",", ".", "\"","\'"]]
filtered_words = [w for w in filtered if w.isalnum() and w not in stop_words]

# Count the frequency of each word
word_freq = Counter(filtered_words)

# Display the word frequency count
for word, count in word_freq.items():
    print(f'{word} : {count}')
    