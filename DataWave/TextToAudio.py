#!/usr/bin/env python
# coding: utf-8

import binascii
import pyaudio
import wave

CHUNK = 10000
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
HIGH_NOTE = (b'\xFF'*100 + b'\0'*100) * 50
LOW_NOTE = (b'\xFF'*50 + b'\0'*50) * 100
p = pyaudio.PyAudio()
a = ''
c = ''
b = ''
sample_buffer = ''

def initData(f=""):
	global b
	b = bin(int(binascii.hexlify(f), 16))
	createBuffer()

def createBuffer():
	global b, sample_buffer
	sample_stream = []
	for bit in b[2:]:
	    if bit == '1':
	        sample_stream.extend(HIGH_NOTE)
	    else:
	        sample_stream.extend(LOW_NOTE)
	sample_buffer = b''.join(sample_stream)

def listen():
	global p, sample_buffer
	stream = p.open(format=FORMAT,
                channels=1,
                rate=44100,
                output=True)
	stream.write(sample_buffer)


def store(loc="../temp/output.wav"):
	global p, sample_buffer
	wf = wave.open(loc, 'wb')
	wf.setnchannels(CHANNELS)
	wf.setsampwidth(p.get_sample_size(FORMAT))
	wf.setframerate(RATE)
	wf.writeframes(sample_buffer)
	wf.close()

def encode(data, storage='', play=False):
	global p
	initData(data)
	if storage:
		store(storage)
	else:
		store()
		storage = 'DataWave temp folder'
	if play:
		listen()
	p.terminate()
	return "Encoded Audio at: " + storage