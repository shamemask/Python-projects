import speech_recognition as sr

r = sr.Recognizer()

for index, name in enumerate(sr.Microphone.list_microphone_names()):

    print(index, name)

with sr.Microphone(device_index=1) as source:
    print('Скажите что-нибудь')
    audio = r.listen(source, phrase_time_limit=2, timeout=2)
    query = r.recognize_google(audio, language='ru-RU')  # распознаем речь
    print(query.lower())  # вывод текста
