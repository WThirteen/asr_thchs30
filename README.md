# asr_thchs30
使用THCHS30 中文语音数据集训练了语言模型，并使用该模型进行语音识别。  
本项目仅提供语音识别，而并无训练模型的代码。  
若想训练一个语音识别模型，可参考[Chinese speech recognition | 中文语音识别](https://github.com/WThirteen/asr_AISHELL-3)
## 模型文件
_下载地址：_
链接：https://pan.baidu.com/s/1y-tEIA34e48t38uSNzV33g  
提取码：asrm  
__下载模型文件后，放在同一文件夹即可。__
## loss曲线：  
![Figure_1](https://github.com/WThirteen/asr_thchs30/assets/100677199/b78fbc24-8fcd-414c-84df-13fa5f2e29f7)
## librosa版本问题
这里使用的 *librosa==0.7.2*  
可能会出现  
![image](https://github.com/WThirteen/asr_thchs30/assets/100677199/6022f953-e40b-4b9e-9009-24a69d8a6e14)  
**参考这份博客：**

[解决不联网环境pip安装librosa、numba、llvmlite报错和版本兼容问题](https://blog.csdn.net/qq_39691492/article/details/130829401)  

*修改如下：*  

![image](https://github.com/WThirteen/asr_thchs30/assets/100677199/14ef3f58-7bb1-4f85-bc58-d49d761a86ae)

