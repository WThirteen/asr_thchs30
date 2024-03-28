dictionary.pkl 为保存的字

运行asr_translate_test.py 会缺少模型文件。

下载模型文件后，放在同一文件夹即可。

下载地址：
链接：https://pan.baidu.com/s/1y-tEIA34e48t38uSNzV33g 
提取码：asrm

loss曲线：

![Figure_1](https://github.com/WThirteen/asr_thchs30/assets/100677199/b78fbc24-8fcd-414c-84df-13fa5f2e29f7)

这里使用的 librosa==0.7.2
可能会出现

![image](https://github.com/WThirteen/asr_thchs30/assets/100677199/6022f953-e40b-4b9e-9009-24a69d8a6e14)

参考这份博客：

https://blog.csdn.net/qq_39691492/article/details/130829401


修改如下：

![image](https://github.com/WThirteen/asr_thchs30/assets/100677199/14ef3f58-7bb1-4f85-bc58-d49d761a86ae)

