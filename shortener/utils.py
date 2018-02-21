import random
import string

from .models import URL


def encode(custom=None):
    encoded = ''.join([
        random.choice(string.ascii_letters + string.digits) for n in range(6)
    ])
    if custom:
        workon = ''.join(custom.split())
        encoded = workon if not URL.objects.filter(
            shortened=encoded).exists() else None
    return encoded
