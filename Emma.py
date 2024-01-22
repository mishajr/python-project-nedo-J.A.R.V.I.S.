

# pip install SpeechRecognition
# pip install pyaudio
# pip install PyAutoGUI




import speech_recognition
import pyautogui as pg

sr = speech_recognition.Recognizer()
sr.pause_threshold = 0.5


def Error():
    print("Невідома помилка,перезапуск")
    listen_command_voice()


def listen_command_voice():
     
        try: 
            with speech_recognition.Microphone() as mic: 
                sr.adjust_for_ambient_noise(source=mic,duration=0.5) 
                audio = sr.listen(source=mic)
                query = sr.recognize_google(audio_data = audio,language='uk-UA').lower()
            return query
        except: 
            speech_recognition.UnknownValueError: Error()
               
        
        
             
             
def google_chrome_youTube():
    pg.hotkey('winleft')
    pg.typewrite('google')
    pg.hotkey(['enter'])
    pg.click(691,595, duration= 0.8)
    pg.typewrite('https://www.youtube.com/')
    pg.hotkey(['enter'])




    



def youTube():
    pg.hotkey('ctrl','t')
    pg.typewrite('https://www.youtube.com/')
    pg.hotkey(['enter'])
        
def youTubeMusic():
    pg.hotkey('ctrl','t')
    pg.typewrite('https://music.youtube.com/watch?v=k7kzc3Nof08&list=PL_5pb5gNwMYbcgI2CTk5LYPDlcR3Eekc-')
    pg.hotkey(['enter'])
    


def google_chrome():
    pg.hotkey('winleft')
    pg.typewrite('google')   
    pg.hotkey(['enter']) 
    pg.click(691,595, duration= 0.7)

def exitWindow():
    pg.hotkey('ctrl','w')
    
    
    
def control_panel():
    pg.hotkey('winleft','r')
    pg.typewrite('control\n')
    
    pg.click(720,320,duration= 0.6)
    pg.click(709,649,duration= 0.6)
    
    
def openWindow():
    pg.hotkey('ctrl','t')






# pg.prompt("red","rere")



# pg.alert("Привіт я помічник ПК,Емма","ПОВІДОМЛЕНЯ!")

while True:
    
    
    print("я вас слухаю")
    voice = listen_command_voice()
    print(voice)
    if voice == "панель керування":
        control_panel()
    if voice == "запусти google":
        google_chrome()
    if voice == "запусти youtube":
        google_chrome_youTube()
    if voice == "відкрий youtube": 
        youTube()
    if voice == "відкрий youtube music":
        youTubeMusic()
    if voice == "відкрий вкладку":
        openWindow()
    if voice == "закрий вкладку":
        exitWindow()
        
        
    else:
        
        print("слухаю")
    
        
       