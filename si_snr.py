import librosa
import get_wavinfo
import os
import numpy as np

def sisnr(s_clean, s_noise):
    # 计算信号功率
    signal_power = np.mean(np.abs(s_clean) ** 2)

    # 计算噪声功率
    # 在这个示例中，我们假设噪声信号是带噪声信号减去纯净信号
    noise_signal = s_noise - s_clean
    noise_power = np.mean(np.abs(noise_signal) ** 2)

    # 计算尺度不变信噪比（以分贝为单位）
    SINR_dB = 10 * np.log10(signal_power / noise_power)

    return SINR_dB


# 从WAV文件加载信号数据
input_dir = 'C:/Users/admin/Desktop/Cola_Software_Build_merge/Asteroid/Sanya/test/10.30_1&40'

s1, _ = librosa.load(os.path.join(input_dir, 'Data 1 Target1No 1Cycle No 1Group Depth400m.wav'), sr=125000)
s2, _ = librosa.load(os.path.join(input_dir, 'Data 40 Target40No 10Cycle No 14Group Depth900m.wav'), sr=125000)
mixture, _ = librosa.load(os.path.join(input_dir, 'Data 1 Target1No 1Cycle No 1Group Depth400m_Data 40 Target40No 10Cycle No 14Group Depth900m.wav'), sr=125000)
r1, _ = librosa.load(os.path.join(input_dir, 'Data 1 Target1No 1Cycle No 1Group Depth400m_Data 40 Target40No 10Cycle No 14Group Depth900m_est1.wav'), sr=125000)
r2, _ = librosa.load(os.path.join(input_dir, 'Data 1 Target1No 1Cycle No 1Group Depth400m_Data 40 Target40No 10Cycle No 14Group Depth900m_est2.wav'), sr=125000)

# 计算SISNR值
sisnr_value1 = sisnr(s1, mixture)
sisnr_value2 = sisnr(s1, r1)
sisnr_value = sisnr_value2 - sisnr_value1
print("SISNR值（dB）：", sisnr_value)
