import speech_recognition as sr
# import pyaudio

# for index, name in enumerate(sr.Microphone.list_microphone_names()):
#     print(index, name)

r = sr.Recognizer()


def speech():
    with sr.Microphone(device_index=1) as source:
        print('Скажите что-нибудь')
        try:
            audio = r.listen(source, phrase_time_limit=2, timeout=2)
            query = r.recognize_google(audio, language='ru-RU')
        except (sr.WaitTimeoutError, sr.UnknownValueError):
            return None
        else:
            return query.lower()
