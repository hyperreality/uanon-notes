from itertools import zip_longest, tee

def grouper(iterable, n, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)

def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

def rebase_alphabet(ct, ngram=1, alphabet='abcdefghijklmnopqrstuvwxyz', mapping=None):
    if not mapping:
        mapping = {}
    def iterate_chars(ct, ngram, alphabet, mapping):
        i = 0
        for group in grouper(ct, ngram):
            key = group[0]
            # key = ''.join(group)
            if key not in mapping:
                mapping[key] = alphabet[i % len(alphabet)]
                i = i + 1
            yield mapping[key]
    return ''.join([c for c in iterate_chars(ct, ngram, alphabet, mapping)])



ct = """
ovthestyoth3thebthesthæel
"""


def canto_decode(ct):
    key = {
        'ab': 'a',
        'ov': 'b',
        'eb': 'c',
        'el': 'd',
        # 'ab': 'e',
        'ow': 'f',
        'wi': 'g',
        'hæ': 'h',
        'th': 'i',
        'in': 'j',
        'be': 'k',
        'yo': 'l',
        'nd': 'm',
        'no': 'n',
        'rt': 'o',
        'st': 'p',
        'so': 'q',
        'ut': 'r',
        'hw': 's',
        'es': 't',
        'ut': 'u',
        'ut': 'v',
        'hæ': 'w',
        'hw': 'x',
        # 'th': 'y',
        'hw': 'z',
        'æ': 'ae'
    }
    skip_one = False
    skip_two = False
    out = ''
    for a, b in pairwise(ct):
        if skip_one:
            skip_one = False
            continue
        if skip_two:
            skip_one = True
            skip_two = False
            continue
        bigram = ''.join([*a, *b])
        if bigram.lower() in key:
            out += key[bigram.lower()]
            if bigram.lower() == 'es':
                skip_two = True
            else:
                skip_one = True
        elif a == 'æ':
            out += 'ae'
        elif a == ' ':
            out += ' '
        else:
            out += a
    return out


print(canto_decode(ct))
