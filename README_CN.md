# py-recycle
> Linux 垃圾回收站

## 截屏
[![asciicast](https://asciinema.org/a/435392.svg)](https://asciinema.org/a/435392)


## 用法
- 将文件移动到回收站: `del file_path`
- 将文件从回收站恢复: `undel file_path` or `undel trash_path`
- 永久删除垃圾文件: `pdel trash_file`
- 打印回收站文件树: `tt`
- 打印回收站文件树调用`less`显示: `tl`
- 示例
    - `del ~/a`, `del /root/a`, `del a`, `del \^a`, `del '^a'`, `del 'a/*/*'`
    - `undel ~/a`, `undel /root/a`, `undel a`, `undel ~/.Trash/root/a`, `del 'a/*/*'`
    - `pdel ~/a`, `pdel /root/a`, `pdel a`, `pdel ~/.Trash/root/a`, `del 'a/*/*'`
    - `tt`, `tt ~`, `tl '*/*'` 
    - `tl`, `tl ~`, `tl '*/*'` 

## 安装
1. `pip install py-recycle`
2. `recycle_init`
    - 如果你的`PATH`中没有Python脚本目录, 执行 `/usr/local/bin/recycle_init 2&> /dev/null || ~/.local/bin/recycle_init`

## 配置
- `VREBOSE`: 是否显示具体操作
- `ENABLE_EMOJI`: 是否启用表情
- `ENABLE_COLOR`: 是否启用颜色
- `TREE_ALL_DIRECTORY_SIZE`: 是否打印所有文件大小
- `TRASH_PATH`: 回收站绝对路径
- `FILE_SIZE_COLORS`: 自定义文件大小单位的颜色

例:

`vim ~/.py_recycle.json`

```Json
{
    "VREBOSE": true,
    "ENABLE_EMOJI": true,
    "ENABLE_COLOR": true,
    "TREE_ALL_DIRECTORY_SIZE": false,
    "TRASH_PATH": "/root/.Trash",
    "FILE_SIZE_COLORS": {
        "文件大小单位": [
            "文件大小<10单位",
            "文件大小<100单位",
            "文件大小<1000单位",
            "文件大小<10000单位"
        ],
        "可选颜色": [
            "black",
            "red",
            "green",
            "orange",
            "blue",
            "magenta",
            "cyan",
            "light_gray",
            "dark_gray",
            "light_red",
            "light_green",
            "yellow",
            "light_blue",
            "light_purple",
            "light_cyan",
            "white"
        ],
         "": [
             "light_gray",
             "light_gray",
             "light_gray",
             "light_gray"
         ],
         "b": [
             "light_gray",
             "light_gray",
             "light_gray",
             "light_gray"
         ],
         "B": [
             "light_gray",
             "light_gray",
             "light_gray",
             "light_gray"
         ],
         "K": [
             "light_gray",
             "light_gray",
             "light_gray",
             "cyan"
         ],
         "M": [
             "cyan",
             "cyan",
             "light_cyan",
             "orange"
         ],
         "G": [
             "orange",
             "orange",
             "yellow",
             "magenta"
         ],
         "T": [
             "magenta",
             "magenta",
             "light_purple",
             "red"
         ],
         "P": [
             "red",
             "red",
             "light_red",
             "light_red"
         ]
    }
}
```

### TODO
- [X] 根据垃圾文件大小显示不同颜色
- [ ] 文件夹路径支持正则, 'del /\d+/a.*?'
