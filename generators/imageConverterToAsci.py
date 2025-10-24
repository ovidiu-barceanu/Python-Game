# ascii_sprites/ascii_image.py

from PIL import Image

class ASCIIImage:
    # Dense ASCII characters from dark → light
    ASCII_CHARS = "@%#*+=-:. "

    def __init__(self, image_path: str, width: int = 40, transparent_bg: bool = True):
        """
        image_path: path to the PNG
        width: target width in characters
        transparent_bg: treat transparent pixels as spaces
        """
        self.image_path = image_path
        self.width = width
        self.transparent_bg = transparent_bg
        self.ascii_art = self._convert_to_ascii()

    def _scale_image(self, image):
        w, h = image.size
        aspect_ratio = h / w
        new_height = int(aspect_ratio * self.width * 0.55)  # adjust for char aspect ratio
        return image.resize((self.width, new_height))

    def _pixel_to_ascii(self, pixel):
        r, g, b, a = pixel
        if a == 0 and self.transparent_bg:
            return " "
        # convert pixel to grayscale brightness
        brightness = int(0.299*r + 0.587*g + 0.114*b)
        char = self.ASCII_CHARS[int(brightness / 255 * (len(self.ASCII_CHARS)-1))]
        # add ANSI color
        return f"\033[38;2;{r};{g};{b}m{char}\033[0m"

    def _convert_to_ascii(self):
        image = Image.open(self.image_path).convert("RGBA")
        image = self._scale_image(image)
        ascii_str = ""
        for y in range(image.height):
            for x in range(image.width):
                ascii_str += self._pixel_to_ascii(image.getpixel((x, y)))
            ascii_str += "\n"
        return ascii_str

    def print(self):
        """Print the ASCII art to the console."""
        print(self.ascii_art)

    def get(self) -> str:
        """Return the ASCII art as a string (useful for logs)."""
        return self.ascii_art
