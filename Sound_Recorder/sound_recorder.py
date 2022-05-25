import sounddevice as sd
from scipy.io.wavfile import write
print("This is Sound Recorder made by Aryaman.")
print("Press enter to continue...")
input()
fs = 44100
seconds = int(input("How many seconds to record? "))
recording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
sd.wait()
write('recording.wav', fs, recording)
print("Your recording has been saved.")