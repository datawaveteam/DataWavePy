import os
import sys 
sys.path.append('..')
import DataWave

f = os.getcwd() + "\output.wav"

## Decode while listening to audio
data = DataWave.decode(f, True)

#Decode without listening to audio (A lot faster)
#data = DataWave.decode(f)

print data