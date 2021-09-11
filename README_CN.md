# Recycle
> Linux 垃圾回收站

## 截屏
![](./example.gif)


## 用法
- 将文件移动到回收站: `del file_path`
- 将文件才回收站恢复: `undel file_path` or `undel trash_path`
- 永久删除垃圾文件: `pdel trash_file`
- 打印回收站文件树: `tt`
- 打印回收站文件树调用`less`显示: `tl`
- 示例
    - `del ~/a`, `del /root/a`, `del a`, `del \^a`, `del "^a"`
    - `undel ~/a`, `undel /root/a`, `undel a`, `undel ~/.Trash/root/a`
    - `pdel ~/a`, `pdel /root/a`, `pdel a`, `pdel ~/.Trash/root/a`
    - `tt`, `tt ~`
    - `tl`, `tl ~`

## 安装
1. `pip install py-recycle`
2. `recycle_init`
    - 如果你的`PATH`中没有Python脚本目录, 执行 `/usr/local/bin/recycle_init 2&> /dev/null || ~/.local/bin/recycle_init`

## 配置
- `ENABLE_EMOJI`: 是否启用表情
- `ENABLE_COLOR`: 是否启用颜色
- `TREE_ALL_DIRECTORY_SIZE`: 是否打印所有文件大小
- `TRASH_PATH`: 回收站绝对路径
- `FILE_SIZE_COLORS`: 自定义文件大小单位的颜色

例:

`vim ~/.py_recycle.json`

```Json
{
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
            "white",
            "black",
            "red",
            "green",
            "orange",
            "blue",
            "magenta",
            "cyan",
            "light_gray",
            "blod white",
            "blod black",
            "blod red",
            "blod green",
            "blod orange",
            "blod blue",
            "blod magenta",
            "blod cyan",
            "blod light_gray"
        ],
        "b": [
            "white",
            "white",
            "white",
            "white"
        ],
        "B": [
            "white",
            "white",
            "white",
            "white"
        ],
        "K": [
            "white",
            "white",
            "white",
            "green"
        ],
        "M": [
            "green",
            "green",
            "blod green",
            "blue"
        ],
        "G": [
            "blue",
            "blue",
            "blod blue",
            "orange"
        ],
        "T": [
            "orange",
            "orange",
            "blood orange",
            "red"
        ],
        "P": [
            "red",
            "red",
            "blood red",
            "blood red"
        ]
    }
}
```

### TODO
[X]根据垃圾文件大小显示不同颜色
