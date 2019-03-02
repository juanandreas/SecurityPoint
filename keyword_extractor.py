import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

DESIRED_POS = ['NN', 'NNP']

def extract_key_words(string):
    # returns a List of keywords, given a string input
    sentences = sent_tokenize(string)
    keywords = []
    for sent in sentences:
        word_tokens = nltk.pos_tag(word_tokenize(sent))
        for word,pos in word_tokens:
            if pos in DESIRED_POS and word not in stopwords.words('english'):
                if word not in keywords:
                    keywords.append(word)
    # print(keywords)
    return keywords


def main():
    string = "On November 13, 2018, OCR received a breach notification report from San Mateo Medical Center (SMMC).  SMMC reported that the breach affected approximately 5,000 individuals.  After an internal investigation, SMMC determined that the report was filed in error, the incident did not amount to a breach and, the incident should not have been reported since no breach occurred.  Based on this information, OCR closed the case."
    keywords = extract_key_words(string)

main()