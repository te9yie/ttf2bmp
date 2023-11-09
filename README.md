# ttf2bmp

## Usage

```sh
> python -m ttf2bmp -i use_chars.txt Silver.ttf 19 > output.csv

> python -m ttf2bmp -i use_chars.txt -s 512 512 -m 5 Silver.ttf 19 > output.csv
```

```sh
usage: ttf2bmp [-h] --input_charset_file INPUT_CHARSET_FILE [--bmp_size BMP_SIZE BMP_SIZE] [--margin MARGIN] ttf_file font_size

positional arguments:
  ttf_file
  font_size

options:
  -h, --help            show this help message and exit
  --input_charset_file INPUT_CHARSET_FILE, -i INPUT_CHARSET_FILE
  --bmp_size BMP_SIZE BMP_SIZE, -s BMP_SIZE BMP_SIZE
  --margin MARGIN, -m MARGIN
```

- `--input_charset_file` 変換する文字を列挙したファイル
- `--bmp_size` 出力するBMPの大きさ
- `--margin` 出力する文字と文字の間隔

## 出力形式

`Unicode Code Point,Image index,UV X,UV Y,BBOX LEFT,BBOX TOP,BBOX RIGHT,BBOX BOTTOM,ADVANCE`
