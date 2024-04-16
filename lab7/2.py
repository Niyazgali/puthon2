import pygame # type: ignore

pygame.init()
screen = pygame.display.set_mode((400, 400))

SONG_END = pygame.USEREVENT + 1
pygame.mixer.music.set_endevent(SONG_END)
_songs=['foo.mp3','foo1.mp3','foo2.mp3']

def play_next_song():
    global _songs
    _songs = _songs[1:] + [_songs[0]]
    pygame.mixer.music.load(_songs[0])
    pygame.mixer.music.play()
def play_pre_song():
    global _songs
    _songs = _songs[1:] + [_songs[0]]
    pygame.mixer.music.load(_songs[-1])
    pygame.mixer.music.play()
done=False
while not done:
    for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                    pygame.mixer.music.load(_songs[0])
                    pygame.mixer.music.play()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    pygame.mixer.music.stop() 
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                      play_next_song()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                     play_pre_song()
                if event.type == SONG_END:
                    print("the song ended!")
    pygame.display.flip()

    