from IBM import *
import spacy
from GenerateQuestions import *

# Takes in a flac file and converts it to a string and write the output
# to a text file
def convertIBM(nothing, filename):
    # Get the string that was converted
    print("Converting " + filename + ".flac to a .txt file")
    string = txtToSpeech("./FlacFiles/" + filename)

    # Writes into a text file
    readFile = open("./TextFiles/" + filename + ".txt", "w")
    readFile.write(string)

    print("Finished converting file to a .txt file")

    # Convert the file to sentences
    convertSTS(filename, string)

    # Convert the sentences to questions
    generateQuestions(filename)

# Takes in a file with a single string in it. 
# Convert the contents of that file to a multi lined sentence file. 
def convertSTS(flacFileName, text):
    print("Converting to sentences")
        
    # Opening the text file to be read from and written to
    writeFile = open("./TextFiles/" + flacFileName + "sentences.txt", "w")

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

    print("Finished Converting")