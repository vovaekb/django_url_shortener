import random
import string
from django.utils import timezone


def short_url():
    random_hash = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(6))
    return random_hash