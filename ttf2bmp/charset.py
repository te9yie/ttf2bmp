from PIL import ImageFont


class GlyphInfo:
    def __init__(self, **kwargs):
        self.text = kwargs.get("text")
        self.code = kwargs.get("code")
        self.bbox = kwargs.get("bbox")
        self.advance = kwargs.get("advance")
        self.image_index = 0
        self.uv = (0, 0)

    def __str__(self) -> str:
        return f"{self.code},{self.image_index},{self.uv[0]},{self.uv[1]},{self.bbox[0]},{self.bbox[1]},{self.bbox[2]},{self.bbox[3]},{int(self.advance)}"


def parse_charset(path: str) -> list[str]:
    with open(path, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]


def get_glyph_info(font: ImageFont, text: str) -> GlyphInfo:
    return GlyphInfo(
        text=text, code=ord(text), bbox=font.getbbox(text), advance=font.getlength(text)
    )


if __name__ == "__main__":
    print(parse_charset("ascii.txt"))
