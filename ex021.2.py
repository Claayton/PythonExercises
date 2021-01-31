#Ex021.2
#Faça um programa em python que abra e reproduza o áudio de um arquivo mp3.

from pydub import AudioSegment
from pydub.playback import play
print('Radio do Clayton...')
song = AudioSegment.from_mp3("ex021.mp3")
play(song)

#---------------------------------------------------------------------------------------------------------

#Os comandos a seguir não estavam funcionando por algum motivo no meu pc no momento em que foram escritos
#Ainda não descobri o motivo do erro mas um dia descobrirei, por enquanto o que funcionou foi o de cima

#---------------------------------------------------------------------------------------------------------
"""import pygame

pygame.mixer.init()
pygame.init()
pygame.mixer.music.load("ex021.mp3")
pygame.mixer.music.play()
pygame.event.wait()"""

#---------------------------------------------------------------------------------------------------------

"""import playsound
playsound.playsound('ex021.mp3')"""

#---------------------------------------------------------------------------------------------------------
