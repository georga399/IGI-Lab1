import uuid
from functools import wraps


def get_image_filename(dir: str):

    @wraps(get_image_filename)
    def inner(instance, filename):
        # Get the filename extension
        extension = filename.split('.')[-1]
        # Generate the new filename using the Article's ID
        unique_filename = f'{uuid.uuid4().hex}.{extension}'
        # Return the path to upload the image
        return f'uploads/{dir}/{unique_filename}'

    return inner