import csv
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

import string
import operator
import re


def main():
    final_data = read_input_file('practiceFile.csv')
    report = generate_report(final_data)
    write_report(report)


def read_input_file(filename):
    with open(filename, 'r') as f:
        data = [row for row in csv.reader(f)]
        workable_data = data[1][4]
        # print(workable_data)


    # gets rid of any words less than 4 characters
    shortword = re.compile(r'\W*\b\w{1,3}\b')
    workable_data = shortword.sub('', workable_data)

    # split into words
    # nltk.download('punkt')
    tokens = word_tokenize(workable_data)
    # print(tokens)

    # convert to lower case
    tokens = [w.lower() for w in tokens]
    # print(tokens)

    # remove punctuation from each word
    table = str.maketrans('', '', string.punctuation)
    stripped = [w.translate(table) for w in tokens]
    # print(stripped)

    # remove non-alphabetic tokens
    words = [word for word in stripped if word.isalpha()]
    # print(words)

    # filter out stop words and sort
    # nltk.download('stopwords')
    stop_words = set(stopwords.words('english'))
    words = [w for w in words if not w in stop_words]
    words.sort()
    # print(words)

    # a sample frequency distribution
    req = nltk.FreqDist(words)
    # print(req.items())
    # for k,v in req.items():
        # print(str(k) + ': ' + str(v))
    sorted_dictionary = sorted(req.items(), key=operator.itemgetter(1), reverse=True)
    for k, v in sorted_dictionary:
        print(str(k) + ': ' + str(v))


def generate_report(data):
    pass


def write_report(report):
    pass


# Application entry point --> call main()
main()


