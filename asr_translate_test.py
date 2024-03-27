from keras.models import load_model
from keras import backend as K
import numpy as np
import librosa
from python_speech_features import mfcc
import pickle
import glob
import os
from save_wav import save_as_wav
from save_wav import takeCommand

# 开始说话
print("start:")
takeCommand()

wavs = glob.glob('temp_file.wav')


with open('dictionary.pkl', 'rb') as fr:
    [char2id, id2char, mfcc_mean, mfcc_std] = pickle.load(fr)

mfcc_dim = 13
# 加载模型
model = load_model('asr_old.h5')
index = np.random.randint(len(wavs))

audio, sr = librosa.load(wavs[index])
# energy = librosa.feature.rmse(audio)
energy = librosa.feature.rms(audio)
frames = np.nonzero(energy >= np.max(energy) / 5)
indices = librosa.core.frames_to_samples(frames)[1]
audio = audio[indices[0]:indices[-1]] if indices.size else audio[0:0]
X_data = mfcc(audio, sr, numcep=mfcc_dim, nfft=551)
X_data = (X_data - mfcc_mean) / (mfcc_std + 1e-14)


pred = model.predict(np.expand_dims(X_data, axis=0))
pred_ids = K.eval(K.ctc_decode(pred, [X_data.shape[0]], greedy=False, beam_width=10, top_paths=1)[0][0])
pred_ids = pred_ids.flatten().tolist()

words=''
judge=0
for i in pred_ids:
    if i != -1:
        judge=1
        words=words+id2char[i]
if judge==1:
    print(words)
else:
    print("未检测到")

# 删除临时音频文件
os.remove("temp_file.wav")