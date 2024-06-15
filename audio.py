import sounddevice
import wavio
class Audio:
    def record_audio():
        duration  = 5
        sampleRate = 44100
        file_name = "audio.wav"

        print('Recording...')
        recording = sounddevice.rec(int(duration*sampleRate),samplerate=sampleRate, channels=2, dtype='int16')
        sounddevice.wait()
        print('finished !!')

        wavio.write(file_name,recording,sampleRate,sampwidth=2)
        print('Saved !!')

    def play_audio():
        recording = wavio.read("audio.wav")
        print('Playing...')
        sounddevice.play(recording.data,recording.rate)
        sounddevice.wait()
        print('Audio finished !!')

    
obj = Audio
obj.record_audio()
obj.play_audio()
