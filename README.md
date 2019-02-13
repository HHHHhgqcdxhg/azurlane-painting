# azurlane-painting test啊啊啊啊啊啊啊啊
碧蓝航线绘图日记画图工具  
如果你不是一名老练的程序员的话,请移步[master分支](https://github.com/HHHHhgqcdxhg/azurlane-painting/tree/master).master分支打包了python环境在里面,对没有python环境的用户来说使用起来比较方便

### api
- 主函数:
    ```__main__.mainFunc()```  
    直接在命令行调用```python __main__.py -h```获取帮助信息
- 生成视频函数:
    ```analyseVideo.makeVideo()```  
    输出的视频没有音频轨道没有原视频对比,请放入其他剪辑软件中自行添加.另,如果w和h调的特别大的话,视频分辨率会超级高.  
    :param input:输入视频的路径  
    :param output:输出视频的路径,请以".avi"结尾  
    :param cutFrames:抽帧频率,比如填1的话,则原视频每一帧都会处理后加入新视频中;填2的话,原视频每2帧会有一帧处理后加入新视频中  
    :param w:横向画板数  
    :param h:纵向画板数  
    :param blur:控制线条加粗,设为0的话不做加粗处理.不为0的话只能填单数,即1,3,5,7等.某些情况下线条加粗比较符合像素风,请按需取用  
    :return:None  
- ```paint.drawN()```  
    :param imgPath:输入图片的路径  
    :param w:横向画板数  
    :param h:纵向画板数  
    :param blur:控制线条加粗,设为0的话不做加粗处理.不为0的话只能填单数,即1,3,5,7等.某些情况下线条加粗比较符合像素风,请按需取用  
    :return: PIL图片对象  


