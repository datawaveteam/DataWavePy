import binascii
import pyaudio
import wave
import sys

CHUNK = 10000
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
HIGH_NOTE_HEX = binascii.hexlify((b'\xFF'*100 + b'\0'*100) * 50)
LOW_NOTE_HEX = binascii.hexlify((b'\xFF'*50 + b'\0'*50) * 100)
b = '0b'
wf = wave.open("output.wav", 'rb')

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                output=True)

data = wf.readframes(CHUNK)

print("Playing output.wav")
while data != '':
	stream.write(data)
	b += binascii.hexlify(data)
	data = wf.readframes(CHUNK)

print("Done playing")
b = b.replace(HIGH_NOTE_HEX, str(1))
b = b.replace(LOW_NOTE_HEX, str(0))
n = int(b, 2)
print binascii.unhexlify('%x' % n)
print("Writing to outputMessage.txt")
stream.stop_stream()
stream.close()

p.terminate()