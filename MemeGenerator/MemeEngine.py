"""Meme engine.

Definition of a class which represent a directory where to generate memes
and gives the ability to make new memes.
"""

from pathlib import Path
from random import randint
from textwrap import wrap

from PIL import Image, ImageDraw, ImageFont


class MemeEngine:
    """Meme engine class.

    This class represent a directory where to generate memes and
    gives the ability to make new memes.
    """

    def __init__(self, output_dir):
        """Initialize the Meme object with an output directory.

        :param output_dir: A path to a directory where to save
        generated memes.
        """
        self._output_dir = str(output_dir)

    @property
    def output_dir(self):
        """Manipulate self.output_dir like a Path object."""
        return Path(self._output_dir)

    @output_dir.setter
    def output_dir(self, out_dir):
        """Change the internal attribute self._output_dir."""
        self._output_dir = str(out_dir)

    def make_meme(self, img_path, text, author, width=500, name=None) -> str:
        """Generate a .png image with a funny text.

        The image is resized to a max size and is saved in output
        directory, defined when object instantiation.

        :param img_path: Path to the input image.
        :param text: Text
        :param author: Author of the text.
        :param width: Max size allowed. The image will be resized with
        the same ratio than the original one.
        :param name: Name for the generated image. If no name is given,
        a random one is assigned.
        :return: A string representing the path to the generated image.
        """
        if not name:
            name = randint(0, 10**6)
        name = str(name)

        with Image.open(img_path) as im:
            ratio = min(width / im.width, width / im.height)
            new_width = int(im.width * ratio)
            new_height = int(im.height * ratio)

            left = (im.width - new_width) // 2
            upper = (im.height - new_height) // 2
            right = left + new_width
            lower = upper + new_height
            img = im.crop((left, upper, right, lower))

            font = ImageFont.truetype('fonts/LilitaOne-Regular.ttf', 20)
            draw = ImageDraw.Draw(img)
            posit = randint(0, new_height-80)
            wrapped_text = '\n'.join(wrap(text, width=40))
            wrapped_text += f'\n- {author} -'
            draw.multiline_text((0, posit), wrapped_text, font=font)

            out_path = self.output_dir.joinpath(name + '.png')
            img.save(out_path)
        return str(out_path)
