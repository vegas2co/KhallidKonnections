from pygame import mixer

mixer.init()
count= 0
'''playlist = ()
for i in playlist():
    mixer.music.load(i[count])
    mixer.music.set_volume(0.7)
    mixer.music.play()
    count =+ 1'''

mixer.music.load('/Users/khallidwilliams/Downloads/supa_cee_hotshit.mp3')
mixer.music.set_volume(0.7)
mixer.music.play()

def playMP3():
  while True:
    print("Press 'p' to pause 'r' to resume ")
    print("Press 'e' to exit the program")
    query = input(">>> ")

    if query == 'p':
      mixer.music.pause()
    elif query == 'r':
      mixer.music.unpause()
    elif query == 'e':
      mixer.music.stop()
      break

playMP3()