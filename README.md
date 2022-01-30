# py-recycle
> recycle for linux

[中文](./README_CN.md)

## Screenshot
[![asciicast](https://asciinema.org/a/435392.svg)](https://asciinema.org/a/435392)


## Usage
- move file to trash directory: `del file_path`
- recover file from trash directory: `undel file_path` or `undel trash_path`
- permanently delete file: `pdel trash_file`
- print trash tree: `tt`
- print trash tree with `less`: `tl`
- example
    - `del ~/a`, `del /root/a`, `del a`, `del \^a`, `del '^a'`, `del 'a/*/*'`
    - `undel ~/a`, `undel /root/a`, `undel a`, `undel ~/.Trash/root/a`, `del 'a/*/*'`
    - `pdel ~/a`, `pdel /root/a`, `pdel a`, `pdel ~/.Trash/root/a`, `del 'a/*/*'`
    - `tt`, `tt ~`, `tl '*/*'` 
    - `tl`, `tl ~`, `tl '*/*'` 

## Installation
1. `pip install py-recycle`
2. `recycle_init`
    - If you did not add python script location to `PATH`, execute `/usr/local/bin/recycle_init 2&> /dev/null || ~/.local/bin/recycle_init`

## Configuration
- `VERBOSE`: Show operations
- `ENABLE_EMOJI`: Enable emoji
- `ENABLE_COLOR`: Enable color
- `TREE_ALL_DIRECTORY_SIZE`: Print all file or directory size
- `TRASH_PATH`: Recycle bin absolute path
- `FILE_SIZE_COLORS`: Customize the color of file size units

Example:

`vim ~/.py_recycle.json`

```Json
{
    "VERBOSE": true,
    "ENABLE_EMOJI": true,
    "ENABLE_COLOR": true,
    "TREE_ALL_DIRECTORY_SIZE": false,
    "TRASH_PATH": "/root/.Trash",
    "FILE_SIZE_COLORS": {
        "file size unit": [
            "file size < 10unit",
            "file size < 100unit",
            "file size < 1000unit",
            "file size < 10000unit"
        ],
         "choice of color": [
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
[X]show different color by trash file size
[ ]folder path support regex, 'del /\d+/a.*?'
