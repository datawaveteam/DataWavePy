#!/usr/bin/env python
# coding: utf-8

import binascii
import pyaudio
import wave

CHUNK = 10000
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
HIGH_NOTE_HEX = binascii.hexlify((b'\xFF'*100 + b'\0'*100) * 50)
LOW_NOTE_HEX = binascii.hexlify((b'\xFF'*50 + b'\0'*50) * 100)
p = pyaudio.PyAudio()
b = '0b'
wf = "../temp/output.wav"
data = ''

def initData(f=""):
	global data, wf
	wf = wave.open(f or wf, 'rb')
	data = wf.readframes(CHUNK)

def process_data(stream=None):
	global data, b, wf
	while data != '':
		b += binascii.hexlify(data)
		data = wf.readframes(CHUNK)
		if stream:
			stream.write(data)

def listen():
	global p
	stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                output=True)
	process_data(stream)
	stream.stop_stream()
	stream.close()

def decode(f, play=False):
	global b, p
	initData(f)
	if play:
		listen()
	else:
		process_data()
	p.terminate()
	b = b.replace(HIGH_NOTE_HEX, str(1))
	b = b.replace(LOW_NOTE_HEX, str(0))
	n = int(b, 2)
	return binascii.unhexlify('%x' % n)