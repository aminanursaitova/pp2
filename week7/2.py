# play, stop, next and previous
import pygame
import os
_songs = ['song_1.mp3', 'song_2.mp3', 'song_3.mp3', 'song_4.mp3', 'song_5.mp3']

def is_trying_to_quit(event):
    pressed_keys = pygame.key.get_pressed()
    alt_pressed = pressed_keys[pygame.K_LALT] or pressed_keys[pygame.K_RALT]
    x_button = event.type == pygame.QUIT
    altF4 = alt_pressed and event.type == pygame.KEYDOWN and event.key == pygame.K_F4
    escape = event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
    return x_button or altF4 or escape

def play_next_song():
    global _songs
    _songs = _songs[1:] + [_songs[0]] # move current song to the back of the list
    pygame.mixer.music.load(_songs[0])
    pygame.mixer.music.play()

def play_prev_song():
    global _songs
    _songs = [_songs[-1]] +  _songs[:-1]  # move prev song to the beginning of the list
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


SONG_END = pygame.USEREVENT + 1
play1 = False
        
def run():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    while True:            
        for event in pygame.event.get():
            if is_trying_to_quit(event):
                return              
        pressed = pygame.key.get_pressed()  
        if pressed[pygame.K_SPACE]: 
            play1 = not play1
            if not play1:
                pygame.mixer.music.stop()
            else:
                pygame.mixer.music.play()
        if pressed[pygame.K_RIGHT]: play_next_song()
        if pressed[pygame.K_LEFT]: play_prev_song()

run()

