import random
import string
from django.utils import timezone


def get_short_url_hash():
    """Generate token for short url from upper case and lower case letters and digits
    
    Return: short url token
    """
    random_hash = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(6))
    return random_hash

def get_ip_address(request):
    """Get user IP address from HTTP request
    
    Keyword arguments:
    request -- HTTP request object HttpRequest
    Return: ip address
    """
    user_ip = request.META.get('HTTP_X_FORWARDED_FOR')
    if user_ip:
        ip = user_ip.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip