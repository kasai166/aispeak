import geminitalk
#import emotion
import speakout
import speakin

while True:
    InText=speakin.speak()
    print(f'input:{InText}')
    if(InText=="終了"):
        break
    text=geminitalk.talk(InText)
    print(f'output:{text}')
    speakout.text_to_voice(text)
#emotion.emo(str(text))