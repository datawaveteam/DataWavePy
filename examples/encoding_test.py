import os
import sys 
sys.path.append('..')
import DataWave

data = "Hello World"
storage = os.getcwd() + "\output.wav"

#Encode while listening to audio
result = DataWave.encode(data, storage, True)

#Encode without listening to audio (A lot faster)
#result = DataWave.encode(data, storage)

print result