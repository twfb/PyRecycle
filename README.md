# Recycle
> recycle for linux

## Screenshot
![](./example.gif)


## Usage
- del file: `del file_path`
- undel file: `undel file_path` or `undel trash_path`
- permanently delete file: `pdel trash_file`
- trash tree: `tt`
- example
    - `del ~/a`, `del /root/a`, `del a`, `del \^a`, `del "^a"`
    - `undel ~/a`, `undel /root/a`, `undel a`, `undel ~/.Trash/root/a`
    - `pdel ~/a`, `pdel /root/a`, `pdel a`, `pdel ~/.Trash/root/a`
    - `tt`, `tt ~`

## Installation
1. `pip install py-recycle`
2. `/usr/local/bin/recycle_init 2&> /dev/null || ~/.local/bin/recycle_init`

## Configuration

`vim ~/.py_recycle.json`

## Support
- regex
- tree
