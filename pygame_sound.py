from gtts import gTTS
from playsound import playsound
import pygame

pygame.init()

text = '지금 갈 수 있어요'
# file_name = 'sample.mp3'
file_name = 'you_can_pass.wma'
tts_ko = gTTS(text=text, lang='ko')
tts_ko.save(file_name)

# with open('sample.txt', 'r', encoding='utf8') as f:
#     text = f.read()
# file_name = 'sample.mp3'
# tts_ko = gTTS(text=text, lang='ko')
# tts_ko.save(file_name)

sound = pygame.mixer.Sound(file_name)
sound.play()

while True:
    pass



# playsound(file_name)