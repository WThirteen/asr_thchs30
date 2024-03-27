import speech_recognition as sr
import wave

def save_as_wav(audio, output_file_path):
    with wave.open(output_file_path, 'wb') as wav_file:
        wav_file.setnchannels(1)  # 单声道
        wav_file.setsampwidth(2)  # 16位PCM编码
        wav_file.setframerate(44100)  # 采样率为44.1kHz
        wav_file.writeframes(audio.frame_data)

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("请说...")
        r.pause_threshold = 1
        audio = r.listen(source)

        output_file_path = "temp_file.wav"
        save_as_wav(audio, output_file_path)

        print("已停止")

if __name__ == "__main__":
    print("start:")
    takeCommand()