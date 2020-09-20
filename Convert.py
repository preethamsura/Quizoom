from IBM import *
import spacy

# Takes in a flac file and converts it to a string and write the output
# to a text file
def convertIBM(nothing, filename):
    # Get the string that was converted
    print("Converting " + filename + ".flac to a .txt file")
    string = txtToSpeech("./FlacFiles/" + filename)

    # Writes into a text file
    file1 = open("./TextFiles/" + filename + ".txt", "w")
    file1.write(string)

    # Close the file
    file1.close

# Takes in a file with a single string in it. 
# Convert the contents of that file to a multi lined sentence file. 
def convertSTS(flacFileName):
    print("Converting to sentences")
        
    # Opening the text file to be read from and written to
    readFile = open("./TextFiles/" + flacFileName + ".txt", "r")
    writeFile = open("./TextFiles/" + flacFileName + "sentences.txt", "w")

    # Convert the string to sentences
    nlp = spacy.load('en_core_web_sm')
    text = readFile.read()
    text_sentences = nlp(text)

    # Writes the sentence into the text file with the proper formatting.
    for sentence in text_sentences.sents:
        # Convert to string with proper formatting
        stringVar = str(sentence.text) + ".\n"
        writeFile.write(stringVar)

    # Close the files
    readFile.close
    writeFile.close

    print("Finished Converting")