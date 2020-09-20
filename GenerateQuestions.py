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
    filename = "./SentenceFiles/" + inputFilename + ".txt"
    writefilename = "./QuestionFiles/" + inputFilename + ".txt"
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
    writeFile.write(str(len(questionAnswer)) + "\n")
    for pair in questionAnswer:
        part1 = "Question " + str(num) + ": " + pair[0][:-1]
        part2 = "Ans: " + pair[1]
        writeFile.write(part1 + "\n" + part2 + "\n\n")
        num += 1

    return questionAnswer

    
# Takes text input from file and generates questions by extracting keywords and filling with blanks. 
def processInput(filename, keys):
    # Gets the file and puts its text into text
    f = open(filename, "r")
    text = f.read()

    # Gets the sentences
    sentenceList = sent_tokenize(text)
    questionList = []

    # Extracts the keywords and creates questions
    for sentence in sentenceList:
        # Gets the keyword for this sentence
        keyword = ""
        for phrase in keys:
            index = sentence.find(phrase)
            if index >= 0:
                keyword = phrase
                break

        # Creates the question for the keyword (if it exists) and formats it properly
        # Adds the question/answer pair to the list: questionList
        if (keyword != ""):
            arr = sentence.split(keyword)
            question = arr[0] + " _____ " + arr[1] + "?"
            answer = keyword
            pair = (question, answer)
            questionList.append(pair)

    return questionList


# Rake implementation, generates keywords with scores based on frequency
def generateKeywords(filename):
    # Opens the file
    f = open(filename, "r")
    # Creates the rake object and gets keywords by using that object
    r = Rake(min_length=1, max_length=3)
    r.extract_keywords_from_text(f.read())
    with_score = r.get_ranked_phrases_with_scores()

    # Only returns keywords with a score of 2.5 or more
    filtered_list = []
    for (score, phrase) in with_score:
        if score >= 2.5:
            filtered_list.append(phrase)
    return filtered_list