# Quizoom
Hackmit 2020 Project

## Inspiration
#
In the age of online classes, keeping students' attention has become harder and harder. As such some professors assign lecture questions to gauge how attentive students are when watching lecture. Quizoom aims to help both students and teachers by creating quiz questions directly from what was taught during lecture. 

## What it does
#
Quizoom uses the audio from a lecture and finds keywords to generate questions automatically. Quizoom utilizes the IBM Cloud speech-to-text API to convert lectures to text which can be processed. The text is then processed using the RAKE algorithm to identify keywords relating to the lecture. Questions are generated using these keywords as answers. 

![Demo](https://media.giphy.com/media/eea7tFv0fM0hgNIEZN/giphy.gif)

## How To Use It
<ol> 
<li>Run python3 Quizoom.py. </li>
<li>Press start and enter how long the recording should last and then press Start Recording.</li>
<li>The questions will be available shortly and you can press the Quiz button to see them. </li>
<li>Input your answer it press submit to see if you got the question correct or not.</li>
</ol>

## Sources
#
IBM Cloud - Speech to Text APIRake API

Rake-nltk python library

Rake-nltk python library - keyword detection

Spacy python library - Sentence segmentation

#
### Contributors
<ul>
<li>Preetham Sura</li>
<li>Asim Biswal</li>
<li>Uthman Momen</li>
<li>Nikhil Padavala</li>
</ul>

Go Bears!
