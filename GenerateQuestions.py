from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize 
from rake_nltk import Rake

# Creates the questions and prints them to terminal
def generateQuestions(filename):
    # Convert the filename so that it gets the right file
    filename = "./TextFiles/" + filename + "sentences.txt"
    
    # Get the scored keys from the sentences
    keys = generateKeywords(filename)
    print("Printing out Keys:")
    print(keys)
    print("")
    
    # Processes the keys and attempts to create questions from those keys
    print("Printed Questions:")
    print(processInput(filename, keys))
    print("")

# Takes text input from file and generates questions by extracting keywords and filling with blanks. 
def processInput(filename, keys):
    f = open(filename, "r")
    text = f.read()
    sentenceList = sent_tokenize(text)
    questionList = []
    for sentence in sentenceList:
        keyword = ""
        words = sentence.split(" ")
        for word in words:
            if word in keys:
                keyword = word
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
    #for (score, phrase) in 
    #modify keys to remove all below 2
    return r.get_ranked_phrases()
        
        