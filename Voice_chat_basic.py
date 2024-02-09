import speech_recognition as sr
import keyboard
import pyautogui
import pydirectinput

i=0
t=0
r = sr.Recognizer()


while True:

    with sr.Microphone() as source:
         print('Diz a categoria : ')
         audio = r.listen(source)

    try:
          text = r.recognize_google(audio, language="pt-PT")
          print('You said:{}'.format(text))
          if(text == 'pesquisa'):
              while(t==0):
                   with sr.Microphone() as sources:
                        print('Diz o que queres : ')
                        audio1 = r.listen(sources)
                   try:
                        text1 = r.recognize_google(audio1, language="pt-PT")
                        print('You said:{}'.format(text1))
                        
                        if(text1 == 'YouTube'):
                           keyboard.write('youtube.com')
                           keyboard.press_and_release('enter')
                        
                        elif(text1 == 'Twitch'):
                             keyboard.write('twitch.tv')
                             keyboard.press_and_release('enter')
                           
                        elif(text1 == 'voltar'):
                             t=t+1
                   except:
                          print('Sorry could not recognize your voice')
                          
                  
          
          if(text == 'sair'):
              i=i+1
          if(text == 'stop' or text == 'Stop'):
              keyboard.wait('space')
          if(text == 'mensagem'):
              while(t==0):
                   with sr.Microphone() as sourc:
                        print('Diz o que queres : ')
                        audio2 = r.listen(sourc)
                   try:
                        text2 = r.recognize_google(audio2, language="pt-PT")
                        print('You said:{}'.format(text2))
                        if(text2 == '3D'):
                           keyboard.write('O Render é muito bom')
                           keyboard.press_and_release('enter')
                        elif(text2 == 'como'):
                             keyboard.write('Estamos tramados')
                             keyboard.press_and_release('enter')
                        elif(text2 == 'sim'):
                             keyboard.write('Sim')
                             keyboard.press_and_release('enter')
                        elif(text2 == 'não'):
                             keyboard.write('Não')
                             keyboard.press_and_release('enter')
                        elif(text2 == 'bom dia'):
                             keyboard.write('Bom dia')
                             keyboard.press_and_release('enter')
                        elif(text2 == 'Boa tarde'):
                             keyboard.write('Boa tarde')
                             keyboard.press_and_release('enter')
                        elif(text2 == 'voltar'):
                             t=t+1
                   except:
                          print('Sorry could not recognize your voice')
          if(text == 'saltar' or text == 'Saltar'):
              pydirectinput.keyDown('space')
              pydirectinput.keyUp('space')
          t=0   
            
    except:
          print('Sorry could not recognize your voice')
  
