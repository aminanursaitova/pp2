import pygame
import os

pygame.mixer.music.load('foo.mp3')
pygame.mixer.music.play(0)

pygame.mixer.music.play(-1)

pygame.mixer.music.play() # play once

pygame.mixer.music.queue('next_song.mp3')

pygame.mixer.music.stop()

# SONG_END = pygame.USEREVENT + 1

# pygame.mixer.music.set_endevent(SONG_END)
# pygame.mixer.music.load('song.mp3')
# pygame.mixer.music.play()

# while True:
#     for event in pygame.event.get():
#         if event.type == SONG_END:
#             print("the song ended!")

_songs = ['song_1.mp3', 'song_2.mp3', 'song_3.mp3', 'song_4.mp3', 'song_5.mp3']

_currently_playing_song = None

import random

def play_a_different_song():
    global _currently_playing_song, _songs
    next_song = random.choice(_songs)
    while next_song == _currently_playing_song:
        next_song = random.choice(_songs)
    _currently_playing_song = next_song
    pygame.mixer.music.load(next_song)
    pygame.mixer.music.play()

def play_next_song():
    global _songs
    _songs = _songs[1:] + [_songs[0]] # move current song to the back of the list
    pygame.mixer.music.load(_songs[0])
    pygame.mixer.music.play()

effect = pygame.mixer.Sound('beep.wav')
effect.play()

_sound_library = {}
def play_sound(path):
  global _sound_library
  sound = _sound_library.get(path)
  if sound == None:
    canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
    sound = pygame.mixer.Sound(canonicalized_path)
    _sound_library[path] = sound
  sound.play()