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

`vim ~/.py_recycle.json`

```Json
{
    "TRASH_PATH": "/root/.Trash",
    "ENABLE_EMOJI": true
}   
```
### Emoji

> 设置`ENABLE_EMOJI`为true启用表情, 默认为true.

```
/root/.Trash/root/git/recycle/Test
├── 📁 2021-02-18_14:52:05620877_4.0K
├── a
│   ├── 📁 2021-02-18_14:51:50932229_4.0K
│   └── 📄 2021-02-18_14:52:01623779_0
├── b
│   ├── 📁 2021-02-18_14:51:50934404_4.0K
│   └── 📄 2021-02-18_14:52:01626129_0
└── c
    ├── 📁 2021-02-18_14:51:50945546_4.0K
    └── 📄 2021-02-18_14:52:01636655_0
```
