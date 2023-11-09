from argparse import ArgumentParser
from . import charset
from PIL import Image, ImageDraw, ImageFont


def main():
    parser = ArgumentParser()
    parser.add_argument("ttf_file", type=str)
    parser.add_argument("font_size", type=int)
    parser.add_argument("--input_charset_file", "-i", required=True)
    parser.add_argument("--bmp_size", "-s", type=int, nargs=2, default=[1024, 1024])
    parser.add_argument("--margin", "-m", type=int, default=1)
    args = parser.parse_args()

    font = ImageFont.truetype(args.ttf_file, args.font_size)

    chars = charset.parse_charset(args.input_charset_file)
    glyphs = [charset.get_glyph_info(font, c) for c in chars]
    image_size = args.bmp_size
    image = Image.new("L", image_size)
    draw = ImageDraw.Draw(image)

    margin = (args.margin, args.margin)
    image_count = 0
    x = 0
    y = 0
    line_height = 0
    for g in glyphs:
        w = g.bbox[2] - g.bbox[0]
        h = g.bbox[3] - g.bbox[1]
        if w + x > image_size[0]:
            x = 0
            y += line_height
            line_height = 0
            if y + h > image_size[1]:
                image.save(f"output_{image_count:02}.bmp")
                image = Image.new("L", image_size)
                draw = ImageDraw.Draw(image)
                x = 0
                y = 0
                image_count += 1
        draw.text((x - g.bbox[0], y - g.bbox[1]), g.text, "white", font)
        g.image_index = image_count
        g.uv = (x, y)
        x += w + margin[0]
        line_height = max(line_height, h + margin[1])
    image.save(f"output_{image_count:02}.bmp")

    for g in glyphs:
        print(g)


if __name__ == "__main__":
    main()
