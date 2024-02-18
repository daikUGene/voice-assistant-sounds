# サイトの動作確認のため、ダミーの音声ファイルを生成
# 生成された音声ファイルをsoundsフォルダに移動すること

import wave
import array
import math

def generate_wav(sample_rate, frequency, duration, output_path):
    # 音声データ生成
    data = array.array('h', [int(32767.0 * math.sin(2.0 * math.pi * frequency * t / sample_rate)) for t in range(int(sample_rate * duration))])

    # wavファイルに書き出し
    with wave.open(output_path, 'w') as wave_file:
        wave_file.setnchannels(1)  # モノラル
        wave_file.setsampwidth(2)  # 16bit
        wave_file.setframerate(sample_rate)
        wave_file.writeframes(data.tobytes())

# サンプリング周波数
sample_rate = 44100

generate_wav(sample_rate=sample_rate, frequency=440.0, duration=3.0, output_path="dummy_audio1.wav")
generate_wav(sample_rate=sample_rate, frequency=880.0, duration=5.0, output_path="dummy_audio2.wav")
generate_wav(sample_rate=sample_rate, frequency=1320.0, duration=7.0, output_path="dummy_audio3.wav")
