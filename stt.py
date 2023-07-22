import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print('듣고있어요')
    audio = r.listen(source)

try:
    # 구글 API
    # text = r.recognize_google(audio, language="en-US")
    # print(text)
    text = r.recognize_google(audio, language="ko")
    print(text)

except sr.UnknownValueError:
    print('인식 실패') # 음성인식 실패
except sr.RequestError as e:
    print('요청 실패 : {0}'.format(e)) # API Key, 네트워크 오류