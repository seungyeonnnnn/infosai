from gtts import gTTS
from playsound import playsound

# text = 'Can I help You?'
# file_name = 'sample.mp3'
# tts_en = gTTS(text=text, lang='en')
# tts_en.save(file_name)

# text = '무엇을 도와드릴까요?'
# file_name = 'sample.mp3'
# tts_ko = gTTS(text=text, lang='ko')
# tts_ko.save(file_name)

with open('sample.txt', 'r', encoding='utf8') as f:
    text = f.read()
file_name = 'sample.mp3'
tts_ko = gTTS(text=text, lang='ko')
tts_ko.save(file_name)

playsound(file_name)