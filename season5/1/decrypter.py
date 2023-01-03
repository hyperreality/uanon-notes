from Crypto.Cipher import AES
import hashlib
import os
from tqdm import tqdm

def decrypt_file(key, filename, size):
    output_filename = os.path.splitext(filename)[0] + '.png'
    with open(filename, 'rb') as inputfile:
        enc_file = inputfile.read()
        enc_body = enc_file[16:]
        iv = enc_file[:16]

    decryptor = AES.new(key, AES.MODE_CBC, IV=iv)
    dec_message = decryptor.decrypt(enc_body[:size])

    if b"PNG" or b"\xff\xd8" in dec_message[:8]:
        print(dec_message[:48])
        print("Hit")
        print(filename)
        print(key)

        with open(output_filename, 'wb') as outputfile:
            outputfile.write(dec_message)


def pad(key):
    return (key + (' ' * (32 - len(key.encode('utf8'))))).encode('utf8')[:32]

decrypt_file(pad("Jan Hendrik Schön"), "i1.enc", 9999999999)
decrypt_file(pad("Craig Steven Wright"), "i2.enc", 999999999)
decrypt_file(pad("Shinichi Mochizuki"), "i3.enc", 9999999999)
decrypt_file(pad("Gerald Cotten"), "i4.enc", 9999999999)
decrypt_file(pad("Albert Gonzalez"), "i5.enc", 9999999999)
decrypt_file(pad("Mo Hailong"), "i6.enc", 9999999999)
