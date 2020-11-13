import io
from urllib.request import urlopen
from PIL import Image, ImageDraw
import numpy as np


def get_and_process_image(url):
    img = io.BytesIO(urlopen(url).read())
    pillow_img = Image.open(img).convert("RGB")
    pillow_img = pillow_img.resize(size=(400, 400))
    np_image = np.array(pillow_img)

    h, w = pillow_img.size
    # Create same size alpha layer with circle
    alpha = Image.new("L", pillow_img.size, 0)
    draw = ImageDraw.Draw(alpha)
    draw.pieslice([0, 0, h, w], 0, 360, fill=255)

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

    # Non test code
    data_bytes_io = io.BytesIO(cropped_image)
    return data_bytes_io
