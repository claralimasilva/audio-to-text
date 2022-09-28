import speech_recognition as sr

# criar um reconhecedor
rec = sr.Recognizer()

# ouvir o audio do microfone
# para escolher qual microfone usar, rode:
# print(sr.Microphone().list_microphone_names())

with sr.Microphone(device_index=0) as microfone:
    rec.adjust_for_ambient_noise(microfone)
    print('Start speaking.')

    audio = rec.listen(microfone)
try:
    #reconhece esse audio e traduz para texto
    texto = rec.recognize_google(audio, language="en-EN")
    print(texto)
except:
    print("Sorry, I can't understand that.")