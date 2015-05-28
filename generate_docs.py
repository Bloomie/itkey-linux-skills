import requests
import random
import string


KEY_ARRAY = [
    'name',
    'second name',
    'age',
    'height',
    'interests',
    'language',
    'location',
    'skills',
    'religion',
    'job',
]


def generate_word(length):
    return ''.join(random.SystemRandom().choice(string.ascii_lowercase) for _ in range(length))


def generate_doc():
    quary_dict = {}
    word_length = random.randint(3, 15)
    key_counter = random.randint(1, 10)
    for i in xrange(0, key_counter):
        quary_dict[KEY_ARRAY[i]] = generate_word(word_length)
    return quary_dict



