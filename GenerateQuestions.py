from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize 
from summarizer import Summarizer

class GenerateQuestions():
    def __init__(self):
        self.filename = "blah.txt"
        
   
   def extractAnswers(qas, doc):
    answers = []

    senStart = 0
    senId = 0

    for sentence in doc.sents:
        senLen = len(sentence.text)

        for answer in qas:
            answerStart = answer['answers'][0]['answer_start']

            if (answerStart >= senStart and answerStart < (senStart + senLen)):
                answers.append({'sentenceId': senId, 'text': answer['answers'][0]['text']})

        senStart += senLen
        senId += 1
    
    return answers
    
    def removeStopwords(self, filename):
        f = open(filename, "r+")
        text = f.read()
        stop_words = set(stopwords.words('english')) 
        word_tokens = word_tokenize(text)
        filtered_sentence = [w for w in word_tokens if not w in stop_words] 
        filtered_string = ""
        for st in filtered_sentence:
            filtered_string += st
        f.write(filtered_string)

    # Rake implementation
    def generateKeywords(self, filename):
        
         


