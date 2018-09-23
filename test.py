from voiceit2 import VoiceIt2
import pyaudio
import wave
print("say hey jarvis you up initiate boot sequence two user stark")
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 9
WAVE_OUTPUT_FILENAME = "auth3.wav"
 
audio = pyaudio.PyAudio()
 
# start Recording
stream = audio.open(format=FORMAT, channels=CHANNELS,
                rate=RATE, input=True,
                frames_per_buffer=CHUNK)
print ("recording...")
frames = []
 
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)
print ("finished recording")
 
 
# stop Recording
stream.stop_stream()
stream.close()
audio.terminate()
 
waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
waveFile.setnchannels(CHANNELS)
waveFile.setsampwidth(audio.get_sample_size(FORMAT))
waveFile.setframerate(RATE)
waveFile.writeframes(b''.join(frames))
waveFile.close()



my_voiceit = VoiceIt2('key_95dc2f49e21d462e9cc03c5a4ba7a076','tok_ff1b7e2e26db42f8b2ee9af8e2e0e109')
my_voiceit.create_voice_enrollment("usr_b9c994a6bc4149968eab59c6c9ca085b", "en-US", "hey jarvis you up initiate boot sequence two user stark", "auth3.wav")


print("say hey jarvis deactivate suit mark one actavation code user stark")
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 9
WAVE_OUTPUT_FILENAME = "auth.wav"
 
audio = pyaudio.PyAudio()
 
# start Recording
stream = audio.open(format=FORMAT, channels=CHANNELS,
                rate=RATE, input=True,
                frames_per_buffer=CHUNK)
print ("recording...")
frames = []
 
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)
print ("finished recording")
 
 
# stop Recording
stream.stop_stream()
stream.close()
audio.terminate()
 
waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
waveFile.setnchannels(CHANNELS)
waveFile.setsampwidth(audio.get_sample_size(FORMAT))
waveFile.setframerate(RATE)
waveFile.writeframes(b''.join(frames))
waveFile.close()



my_voiceit = VoiceIt2('key_95dc2f49e21d462e9cc03c5a4ba7a076','tok_ff1b7e2e26db42f8b2ee9af8e2e0e109')
my_voiceit.create_voice_enrollment("usr_b9c994a6bc4149968eab59c6c9ca085b", "en-US", "hey jarvis deactivate suit mark one actavation code user stark", "auth.wav")


print("say hey jarvis start admin contol override bypass of user stark")
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 9
WAVE_OUTPUT_FILENAME = "auth4.wav"
 
audio = pyaudio.PyAudio()
 
# start Recording
stream = audio.open(format=FORMAT, channels=CHANNELS,
                rate=RATE, input=True,
                frames_per_buffer=CHUNK)
print ("recording...")
frames = []
 
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)
print ("finished recording")
 
 
# stop Recording
stream.stop_stream()
stream.close()
audio.terminate()
 
waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
waveFile.setnchannels(CHANNELS)
waveFile.setsampwidth(audio.get_sample_size(FORMAT))
waveFile.setframerate(RATE)
waveFile.writeframes(b''.join(frames))
waveFile.close()



my_voiceit = VoiceIt2('key_95dc2f49e21d462e9cc03c5a4ba7a076','tok_ff1b7e2e26db42f8b2ee9af8e2e0e109')
my_voiceit.create_voice_enrollment("usr_b9c994a6bc4149968eab59c6c9ca085b", "en-US", "hey jarvis start admin contol override bypass of user stark", "auth4.wav")
