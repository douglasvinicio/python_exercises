#Tocar um mp3 - Yoooo
import pygame
pygame.init()

input ('Quer ouvir uma musica? Yes or No : ')
pygame.mixer.music.load('file001.mp3')
pygame.mixer.music.play()
pygame.event.wait()


