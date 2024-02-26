import wave

wavFile = r"E:\168数据\output_audio_0730155757.wav"
# wavFile = r"E:\168数据\202307301558-1609\Data 1 Target1No 1Cycle No 1Group Depth100m_Data 10 Target10No 5Cycle No 19Group Depth400m_Data 20 Target20No 5Cycle No 1Group Depth1000m.wav"
f = wave.open(wavFile)
# 音频头 参数
params = f.getparams()
Channels = f.getnchannels()
SampleRate = f.getframerate()
bit_type = f.getsampwidth() * 8
frames = f.getnframes()
# Duration 也就是音频时长 = 采样点数/采样率
Duration = wav_time = frames / float(SampleRate)  # 单位为s

print("音频头参数：", params)
print("通道数(Channels)：", Channels)
print("采样率(SampleRate)：", SampleRate)
print("比特(Precision)：", bit_type)
print("采样点数(frames)：", frames)
print("帧数或者时间(Duration)：", Duration)
