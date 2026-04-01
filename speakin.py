import speech_recognition as sr


def speak():
    listener = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            voice_text = listener.recognize_google(voice, language="ja-JP")
            return voice_text
    except:
        print('Sorry, I could not listen')