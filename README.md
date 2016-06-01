PNG图片透明处理
===========================
之前看过一张图片, 显示的是一个男孩在一个房间里, 但是点开后是一个星空.
试着拿Python实现了下.

****

需要两张**大小相同**的图片  
放在与py一个目录下  
分别改名为 hou.jpg qian.jpg  
qian为未点开显示的图片  
hou为点开后显示的图片  
qian的亮度最好大于hou的亮度,否则效果不好.  
运行后生成out为结果.  

****
前景图 
```
![](https://github.com/647-coder/png_python/blob/master/qian.jpg "前景图")
```
后景图  
```
![](https://github.com/647-coder/png_python/blob/master/hou.jpg "后景图")
```
合成后  
```
![](https://github.com/647-coder/png_python/blob/master/out.png "合成图")
```