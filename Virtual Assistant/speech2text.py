import speech_recognition as sr

def speech_to_text():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
    
    try:
        voice_data = r.recognize_google(audio)
        return voice_data
    
    except sr.UnknownValueError:
        print("Unlknown value error")
    except sr.RequestError:
        print("Request Error")  

    # print(voice_data)


