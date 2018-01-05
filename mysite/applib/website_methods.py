from django.conf import settings
import random

def get_static_url():
    static_url = settings.STATIC_URL
    return static_url

def get_static_root():
    static_root = settings.STATIC_ROOT
    return static_root

def get_random_archetype_integer():
    return random.randint(0,2)
