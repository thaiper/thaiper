import numpy as np
import soundfile as sf
import matplotlib.pyplot as plt

FILE_NAME = 'input/thabugida.wav'
BACKGROUND = 0.005
BLOCKSIZE = 1024

sig, sr = sf.read(FILE_NAME)

rms = [np.sqrt(np.mean(block**2)) for block in
       sf.blocks(FILE_NAME, blocksize=BLOCKSIZE, overlap=0)]

def getTrimLimits (rms, start, length, gaps=0, bg=BACKGROUND, margin=3):
    # print('trim', start, length, bg, margin)
    end = start + length
    fragment = 0
    inside = False
    foundStart = start
    foundEnd = end

    for i in range(start, end):
        v = rms[i]
        if (v > bg):
            if not inside:
                # print('started', i, v)
                if fragment == 0:
                    foundStart = i
                fragment += 1
                inside = True
        elif inside:
            # print('ended', i, v)
            foundEnd = i
            inside = False
            if fragment > gaps:
                break
    result = (
        max(start, foundStart - margin),
        min(end, foundEnd + margin),
    )
    # print('result', result)
    return result

prevEnd = 429 # 0
maxLength = 5 * sr
i = 3 # 0
gap = 0
while prevEnd + maxLength < sig.shape[0]:
    print(i, prevEnd)
    try:
        (s, e) = getTrimLimits(rms, prevEnd, maxLength, gap)
    except IndexError:
        break

    # print(i)
    # print(s*BLOCKSIZE, e*BLOCKSIZE)
    # print(s*BLOCKSIZE / sr, e*BLOCKSIZE / sr)

    trimmed_sig = sig[s*BLOCKSIZE:e*BLOCKSIZE]
    # print(len(trimmed_sig))

    sf.write(f'./output/wavs/{i+1}.wav', trimmed_sig, sr)
    d = input("check the wav file, enter empty string if it's okay, otherwise any non-empty string to make it longer")
    if d == '':
        i += 1
        prevEnd = e
        gap = 0
    else:
        gap += 1
