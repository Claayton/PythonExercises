#Ex021.2
#Faça um programa em python que abra e reproduza o áudio de um arquivo mp3.

import playsound
playsound.playsound('ex021.mp3')

#---------------------------------------------------------------------------------------------------------

"""O comandos a seguir não estava funcionando por algum motivo no meu pc no momento em que foi escrito
ainda não descobri o motivo do erro mas um dia descobrirei, por enquanto o que funcionou foi o de cima

import pygame

pygame.mixer.init()
pygame.init()
pygame.mixer.music.load("ex021.mp3")
pygame.mixer.music.play()
pygame.event.wait()"""
