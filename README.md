# BilibiliCacheExporter
从b站客户端缓存导出完整视频和ass弹幕的自用脚本  
港澳台番使用脚本配合win10客户端有奇效
# 依赖
- python3
- ffmpeg
- danmaku2ass
# 使用 
``` bash
python3 merge.py 缓存目录
```
将导出在当前目录 
`merge.sh`和`merge.py`同一目录  
merge_android.py用于andoird客户端，可在termux中执行，需注意danmaku2ass安装路径  
merge_uwp.py用于第三方uwp客户端
