import itertools
import string

# for i in itertools.product(string.ascii_uppercase + string.digits + "!#$&-_+?|", repeat=5):
for i in itertools.product(string.punctuation, repeat=5):
    print("".join(i))
