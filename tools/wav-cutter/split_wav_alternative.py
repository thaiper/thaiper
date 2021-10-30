import numpy as np
import soundfile as sf
import matplotlib.pyplot as plt
import math

FILE_NAME = 'input/thabugida.wav'
BACKGROUND = 0.005
BLOCKSIZE = 1024
MIN_SILENCE_GAP_SECONDS = 0.5

sig, sr = sf.read(FILE_NAME)

MIN_SILENCE_GAP_BLOCKS = math.ceil(sr / BLOCKSIZE * MIN_SILENCE_GAP_SECONDS)

rms = [np.sqrt(np.mean(block**2)) for block in
       sf.blocks(FILE_NAME, blocksize=BLOCKSIZE, overlap=0)]

def getSilencePeriods (rms, silence_volume_max=BACKGROUND, min_silence_duration_blocks=MIN_SILENCE_GAP_BLOCKS):
    i = 0
    length = len(rms)
    wasSilent = True
    silencePeriods = []
    lastSilenceStartedAt = 0

    while i < length - min_silence_duration_blocks:
        silent = rms[i] < silence_volume_max
        if silent:
            if wasSilent:
                # just move on, in silence
                pass
            else:
                # silence starts here
                wasSilent = True
                lastSilenceStartedAt = i
        else:
            if wasSilent:
                # silence ends here
                silence_was_long_enough = i - lastSilenceStartedAt >= min_silence_duration_blocks
                if silence_was_long_enough:
                    silencePeriods.append((lastSilenceStartedAt, i))
                else:
                    pass
                wasSilent = False
            else:
                # just move on, keep it loud
                pass
        i += 1

    silence_was_long_enough = i - lastSilenceStartedAt >= min_silence_duration_blocks
    if silence_was_long_enough:
        silencePeriods.append((lastSilenceStartedAt, i))

    return silencePeriods

def getSignalPeriodsFromSilencePeriods (silencePeriods):
    signalPeriods = []
    i = 0
    length = len(silencePeriods)
    while i < length - 1:
        signalPeriods.append((silencePeriods[i][1], silencePeriods[i+1][0]))
        i += 1
    return signalPeriods

def saveTrimmedFiles (signalPeriods, block_size=BLOCKSIZE):
    i = 0
    for sp in signalPeriods:
        trimmed_sig = sig[sp[0] * BLOCKSIZE : sp[1] * BLOCKSIZE]
        sf.write(f'./output/wavs/{i+1}.wav', trimmed_sig, sr)
        i += 1

silencePeriods = getSilencePeriods(rms)
signalPeriods = getSignalPeriodsFromSilencePeriods(silencePeriods)
saveTrimmedFiles(signalPeriods)
