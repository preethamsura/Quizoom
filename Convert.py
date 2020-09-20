from IBM import *
import spacy
from GenerateQuestions import *

# Takes in a flac file and converts it to a string and write the output
# to a text file
def convertIBM(nothing, filename):
    # Get the string that was converted
    print("Converting " + filename + ".flac questions")
    string = txtToSpeech("./FlacFiles/" + filename)

    # Writes into a text file
    readFile = open("./TextFiles/" + filename + ".txt", "w")
    readFile.write(string)

    # Convert the file to sentences
    convertSTS(filename, string)

    # Convert the sentences to questions
    generateQuestions(filename)

    print("Finished converting " + filename + ".flac to questions")

# Takes in a file with a single string in it. 
# Convert the contents of that file to a multi lined sentence file. 
def convertSTS(flacFileName, text):
    # Opening the text file to be read from and written to
    writeFile = open("./SentenceFiles/" + flacFileName + ".txt", "w")

    # Convert the string to sentences
    nlp = spacy.load('en_core_web_sm')
    text_sentences = nlp(text)

    # Writes the sentence into the text file with the proper formatting.
    for sentence in text_sentences.sents:
        # Convert to string with proper formatting
        stringVar = str(sentence.text) + ".\n"
        writeFile.write(stringVar)

    # Close the files
    writeFile.close