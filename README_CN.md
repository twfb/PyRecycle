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
    - `undel ~/a`, `undel /root/a`, `undel a`, `undel /root/.Trash/a`, `del 'a/*/*'`
    - `pdel ~/a`, `pdel /root/a`, `pdel a`, `pdel /root/.Trash/a`, `del 'a/*/*'`
    - `tt`, `tt ~`, `tt '*/*'`
    - `tl`, `tl ~`, `tl '*/*'`

## 注意
- 使用`undel`, `pdel`, `tt`, `tl`时按下tab后命令行提示的文件列表为**当前路径被删除的文件**和**回收站根路径被删除的文件**
    
    ```shell
    $ pwd
    /test
    $ mkdir dir /dir /dir2
    $ del dir /dir /dir2
    mkdir -p /root/.Trash/test/dir
    mv /test/dir /root/.Trash/test/dir/2022-09-02_01:39:06704016_4.0K
    mkdir -p /root/.Trash/dir
    mv /dir /root/.Trash/dir/2022-09-02_01:39:06713729_4.0K
    mkdir -p /root/.Trash/dir2
    mv /dir2 /root/.Trash/dir2/2022-09-02_01:39:06719008_4.0K
    
    $ pdel <tab>
    dir/  dir2/  etc/   home/  mnt/   root/  usr/
    
    $ pdel dir
        Permanently delete /root/.Trash/test/dir ? [N/y] y
    rm -rf /root/.Trash/test/dir/2022-09-02_01:22:26772094_4.0K
    rmdir /root/.Trash/test/dir
    rmdir /root/.Trash/test
    
    $ pdel dir
        Permanently delete /root/.Trash/dir ? [N/y] y
    rm -rf /root/.Trash/dir/2022-09-02_01:22:29299637_4.0K
    rmdir /root/.Trash/dir
    
    $ pdel /dir2
        Permanently delete /root/.Trash/dir2 ? [N/y] y
    rm -rf /root/.Trash/dir2/2022-09-02_01:39:06719008_4.0K
    rmdir /root/.Trash/dir2
    ```

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
