import json 
from os.path import join, dirname 
from ibm_watson import SpeechToTextV1 
from ibm_watson.websocket import RecognizeCallback, AudioSource 
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator 

def txtToSpeech(filename): 
    authenticator = IAMAuthenticator('lnnbtj4cHOBqYk1NAiDdA8psSVXslJCi3cXHbFgYwK2-')  
    service = SpeechToTextV1(authenticator = authenticator) 
        
    service.set_service_url('https://api.us-south.speech-to-text.watson.cloud.ibm.com/instances/b19014e0-909a-475d-8989-02b8b197f15c') 
    
    # Insert local mp3 file path in 
    # place of 'LOCAL FILE PATH'   /FlacToQuestion/audio-file.flac
    with open(join(dirname('__file__'), filename + '.flac'),  
            'rb') as audio_file: 
            dic = json.loads( 
                    json.dumps( 
                        service.recognize( 
                            audio=audio_file, 
                            content_type='audio/flac',    
                            model='en-US_NarrowbandModel', 
                        continuous=True).get_result(), indent=2)) 
    
    # Stores the transcribed text 
    str = "" 
    
    while bool(dic.get('results')): 
        str = dic.get('results').pop().get('alternatives').pop().get('transcript')+str[:] 
        
    print(str) 