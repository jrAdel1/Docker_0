FROM python

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir nltk 
# RUN python -m nltk.downloader stopwords

CMD ["python", "script.py"]

