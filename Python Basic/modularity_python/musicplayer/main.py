
from musicplayer import  bar,foo
from musicplayer.audio import read_audio
from tests_module import test_musicplayer

def audio_task():
    audio_call = read_audio.read_audio()
    print(audio_call)

def bar_task():
    bar_call=bar
    print(bar_call.bar_function())

def foo_task():
    print(foo.foo_fucntion())


def test_multiplayer_task():
    test_musicplayer_call=test_musicplayer.test_music_player()
    print(test_musicplayer_call)

if __name__ == '__main__':

    audio_task()
    bar_task()
    foo_task()
    test_multiplayer_task()


   
