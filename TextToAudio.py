import binascii
import sys
import pyaudio
import wave

CHUNK = 10000
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
WAVE_OUTPUT_FILENAME = "output.wav"

a = open(sys.argv[1], 'r')
c = a.read()
ba = int(binascii.hexlify(c), 16)
b = bin(ba)

sample_stream = []
high_note = (b'\xFF'*100 + b'\0'*100) * 50
low_note = (b'\xFF'*50 + b'\0'*50) * 100
for bit in b[2:]:
    if bit == '1':
        sample_stream.extend(high_note)
    else:
        sample_stream.extend(low_note)

sample_buffer = b''.join(sample_stream)

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=1,
                rate=44100,
                output=True)
print("Playing Audio Message.")
stream.write(sample_buffer)


print("Storing Audio Message to file.")
wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(sample_buffer)
wf.close()
p.terminate()
print("Done Storing to file.")
