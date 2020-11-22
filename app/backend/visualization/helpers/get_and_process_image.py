# -*- coding: utf-8 -*-
"""The module to obtain an image by the URL and process it."""

import io
from urllib.request import urlopen
from PIL import Image, ImageDraw
import numpy as np


def _get_and_process_image(url: str) -> io.BytesIO:
    """
    Get the image by the URL, then crop it into a circle using numpy and Pillow, \
    and return cropped version of the image.

    Args:
         `url`: the URL to the image we need to get and process.
    Returns:
        `io.BytesIO`: the io.BytesIO object that contains processed image.
    """
    img = io.BytesIO(urlopen(url).read())
    pillow_img = Image.open(img).convert("RGB")
    pillow_img = pillow_img.resize(size=(400, 400))
    np_image = np.array(pillow_img)

    height, width = pillow_img.size
    # Create same size alpha layer with circle
    alpha = Image.new("L", pillow_img.size, 0)
    draw = ImageDraw.Draw(alpha)
    draw.pieslice([0, 0, height, width], 0, 360, fill=255)

    # Convert alpha Image to numpy array
    np_alpha = np.array(alpha)

    # Add alpha layer to RGB
    np_image = np.dstack((np_image, np_alpha))

    # Save with alpha
    cropped_image_in_bytes = io.BytesIO()
    cropped_image = Image.fromarray(np_image)
    cropped_image.save(cropped_image_in_bytes, "PNG")
    cropped_image_in_bytes.seek(0)
    cropped_image = cropped_image_in_bytes.read()

    # Return io.BytesIO image with all done manipulations
    data_bytes_io = io.BytesIO(cropped_image)
    return data_bytes_io
