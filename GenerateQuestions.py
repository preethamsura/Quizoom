from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize 
from rake_nltk import Rake
import numpy as np
import spacy
nlp = spacy.load('en_core_web_sm')
from spacy.lang.en.stop_words import STOP_WORDS
from collections import OrderedDict

# Creates the questions and prints them to terminal
# Returns the question answer pair to be used in the GUI
def generateQuestions(inputFilename):
    # Convert the filename so that it gets the right file
    filename = "./TextFiles/" + inputFilename + "sentences.txt"
    writefilename = "./TextFiles/Questions" + inputFilename + ".txt"
    writeFile = open(writefilename, "w")
    # Get the scored keys from the sentences
    keys = generateKeywords(filename)
    #print("Printing out Keys:")
    #print(keys)
    #print("")
    
    # Processes the keys and attempts to create questions from those keys
    #print("Printed Questions:")
    num = 1
    questionAnswer = processInput(filename, keys)
    for pair in questionAnswer:
        part1 = "Question " + str(num) + ": " + pair[0][:-1]
        part2 = "Ans: " + pair[1]
        writeFile.write(part1 + "\n" + part2 + "\n\n")
        num += 1

    return questionAnswer

    
# Takes text input from file and generates questions by extracting keywords and filling with blanks. 
def processInput(filename, keys):
    f = open(filename, "r")
    text = f.read()
    sentenceList = sent_tokenize(text)
    questionList = []
    for sentence in sentenceList:
        keyword = ""
        for phrase in keys:
            index = sentence.find(phrase)
            if index >= 0:
                keyword = phrase
                break
        if (keyword != ""):
            arr = sentence.split(keyword)
            question = arr[0] + " _____ " + arr[1] + "?"
            answer = keyword
            pair = (question, answer)
            questionList.append(pair)
    return questionList


# Rake implementation, generates keywords with scores based on frequency
def generateKeywords(filename):
    f = open(filename, "r")
    r = Rake(min_length=1, max_length=3)
    r.extract_keywords_from_text(f.read())
    with_score = r.get_ranked_phrases_with_scores()
    filtered_list = []
    for (score, phrase) in with_score:
        if score >= 2.5:
            filtered_list.append(phrase)
    return filtered_list


def set_dictionary(sentences):
    dictionary = OrderedDict()
    count = 0
    for sentence in sentences:
        for word in sentence:
            if word not in dictionary:
                dictionary[word] = count
                count += 1
    return dictionary


def pairWords(window, text):
    pairs = []
    for sentence in text:
        i = 0
        for word in sentence:
            for j in range(i + 1, i + window):
                if j < len(sentence):
                    pair = (word, sentence[j])
                    if pair not in pairs:
                        pairs.append(pair)
                else:
                    break
            i += 1
    return pairs