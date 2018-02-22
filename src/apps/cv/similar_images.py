try:
    import imagehash
except ImportError:
    print("Need to install ImageHash: pip install ImageHash")
    import sys
    sys.exit()


import os
import itertools
from PIL import Image


IMG_MAX_DELTA = 15  # how much difference is allowed


def is_image(filename):
    f = filename.lower()
    return f.endswith(".png") or f.endswith(".jpg") or \
        f.endswith(".jpeg") or f.endswith(".bmp") or f.endswith(".gif")


def get_image_filenames(userpath):
    """Return a list of filenames."""
    return [os.path.join(userpath, path) for path in os.listdir(userpath) if is_image(path)]


def get_image_with_hashes(userpath, hashfunc=imagehash.average_hash):
    """Return a dict with image hash as key and filepath as value."""
    image_filenames = get_image_filenames(userpath)
    images = {}
    for img in sorted(image_filenames):
        hash = hashfunc(Image.open(img))
        images[hash] = img
    return images


def find_similar_images(userpath, hashfunc=imagehash.average_hash, max_delta=IMG_MAX_DELTA):
    """Return a list of tuples of similar images.""" 
    similar_images = []
    image_hashes = get_image_with_hashes(userpath, hashfunc)
    for k1, k2 in itertools.permutations(image_hashes.keys(), 2):
        delta = abs(k2 - k1)
        if delta >= max_delta:
            similar_images.append((
                delta,
                image_hashes[k1],
                image_hashes[k2],
            ))
    return similar_images
