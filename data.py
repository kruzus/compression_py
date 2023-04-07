from io import BytesIO
import uuid
from PIL import Image
import os
from uuid import uuid4 as v4

import secrets
import string


def generate_random_string(length):
    alphabet = string.ascii_letters + string.digits
    return ''.join(secrets.choice(alphabet) for i in range(length))


def resize_image(file_path):
    output_path = os.path.splitext(file_path)[0] + f"{generate_random_string(64)}{str(v4()).replace('-', '')}.jpg"
    max_width = 1280
    
    with Image.open(file_path) as im:
        if im.height == 0:
            raise ValueError("Image height cannot be zero.")
        width_percent = (max_width / float(im.size[0]))
        height_size = int((float(im.size[1]) * float(width_percent)))
        max_size = (max_width, height_size)
        im.thumbnail(max_size, Image.BICUBIC)
        im.save(output_path, optimize=True, quality=80, format='JPEG')
        return output_path



resize_image("./bifFile.jpeg")
