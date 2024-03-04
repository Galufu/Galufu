import speech_recognition as sr
from gtts import gTTS 
import cv2
import os

def recognize_speech():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Say something in English:")
        audio = recognizer.listen(source)

    try:
        english_text = recognizer.recognize_google(audio, language="en-US")
        print("You said:", english_text)
        return english_text
    except sr.UnknownValueError:
        print("Speech recognition could not understand audio")
        return None
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return None

def translate_to_spanish(english_text):
    # You can use a translation API or library here, for simplicity, we'll just prepend "Hola, " to the text.
    chiness_text = "Hola, " + english_text
    return chiness_text

def text_to_speech(text, language="es"):
    tts = gTTS(text=text, lang=language, slow=False)
    tts.save("translation.mp3")
    os.system("start translation.mp3")  # Opens the default audio player to play the translation

def main():
    english_text = recognize_speech()

    if english_text:
        chiness_text = translate_to_spanish(english_text)
        print("Translated to Spanish:", chiness_text)

        text_to_speech(chiness_text)
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    
    cv2.imshow('webcam', frame)
    
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
if __name__ == "__main__":
    main()
