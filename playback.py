import pygame
import os

pygame.mixer.init()
paused = False

def play_audio(file_path):
    global paused
    paused = False
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

def stop_audio():
    pygame.mixer.music.stop()

def pause_audio():
    global paused
    if paused:
        pygame.mixer.music.unpause()
        paused = False
    else:
        pygame.mixer.music.pause()
        paused = True

def set_volume(vol):
    pygame.mixer.music.set_volume(vol)
