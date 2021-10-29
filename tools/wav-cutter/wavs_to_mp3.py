from pydub import AudioSegment

for i in range(1, 43):
    print(i)
    wavFileName = f"./output/wavs/{i}.wav"
    mp3FileName = f"./output/mp3s/{i}.mp3"
    AudioSegment.from_wav(wavFileName).export(mp3FileName, format="mp3")
