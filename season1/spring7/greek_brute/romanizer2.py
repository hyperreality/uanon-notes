from romanize import romanize
from transliterate import translit, get_available_language_codes
import sys

with open(sys.argv[1]) as f:
    words = [a.strip() for a in f.readlines()]

for w in words:
    print(translit(w, 'el', reversed=True).upper())
