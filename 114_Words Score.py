#Words Score


import re

from functools import reduce
def score_words(words):
    return reduce(lambda x, y: x+y, [2 if (len(re.findall('[aeiouy]',a))%2 == 0) else 1 for a in words], 0)